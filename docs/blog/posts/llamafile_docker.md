---
date:
    created: 2025-11-18
    modified: 2026-03-30
---

# Run LLMs Anywhere as a Single File with Docker

## The Problem

Deploying large language models (LLMs) can be a hassle on local machines. It involves setting up Python environments, CUDA drivers, model downloads, and platform-specific quirks. But as a developer who often switches between different machines and operating systems (Ubuntu, Windows, and macOS), I needed something portable. Something that would run the same way everywhere.

## The Solution: A Single Dockerfile

The answer lies in combining Mozilla’s [Llamafiles](https://blog.mozilla.ai/llamafile-returns/) with Docker. *"Each llamafile contains both server code and model weights, making the deployment of an LLM as easy as downloading and executing a single file. It also leverages the popular llama.cpp project for fast model inference."* Wrapping that in Docker gives us a universally portable container that runs the API server with a single command.

<!-- more -->

## Building the Docker Image

We don't need a heavy Python base image. Since Llamafiles are self-contained binaries, we just need a minimal Linux environment capable of downloading and executing the file. Here’s a simple Dockerfile to achieve this:

```Dockerfile
# Use minimal glibc-based image
FROM debian:bookworm-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl ca-certificates binutils && \
    rm -rf /var/lib/apt/lists/*

# Configuration
ENV LLAMAFILE_URL="https://huggingface.co/Mozilla/Llama-3.2-1B-Instruct-llamafile/resolve/main/Llama-3.2-1B-Instruct-Q8_0.llamafile"
ENV LLAMAFILE_NAME="Llama-3.2-1B-Instruct-Q8_0.llamafile"
ENV PORT=1111

# Working directory
WORKDIR /home

# Download and prepare the Llamafile
RUN curl -L "${LLAMAFILE_URL}" -o "${LLAMAFILE_NAME}" && \
    chmod +x "${LLAMAFILE_NAME}"

# Create an entrypoint script
RUN echo '#!/bin/sh\nexec /home/$LLAMAFILE_NAME --server --port $PORT --host 0.0.0.0 -ngl 9999 --nobrowser' > /entrypoint.sh && \
    chmod +x /entrypoint.sh

EXPOSE ${PORT}

ENTRYPOINT ["/entrypoint.sh"]
```

### How It Works

- **Base image**: `debian:bookworm-slim` - tiny, stable glibc environment that runs on most platforms.
- **Dependencies**: installs `curl`, `ca-certificates`, and `binutils`. `curl` downloads the Llamafile; `ca-certificates` keeps HTTPS working; `binutils` helps in case the Llamafile relies on linked binaries.
- **ENV**: defines `LLAMAFILE_URL`, `LLAMAFILE_NAME`, and `PORT` so you can override them at build/run time.
- **WORKDIR**: sets `/home` as the location where the Llamafile is stored and executed.
- **Download & permissions**: `curl -L` fetches the Llamafile and `chmod +x` makes it runnable inside the container.
- **Entrypoint**: creates `/entrypoint.sh` that executes the Llamafile as a server (listening on all interfaces). The flags `--server --port $PORT --host 0.0.0.0` are typical; `-ngl 9999 --nobrowser` are example runtime options - adjust to the Llamafile's CLI if needed.
- **EXPOSE & ENTRYPOINT**: exposes the port and launches the entrypoint automatically.

## Build and Run

Save the Dockerfile, then build your image:

```bash
docker build -t llamafile-docker .
```

This takes a few minutes (the model is ~1.3GB). Once it's done, run it:

```bash
docker run -d -p 1111:1111 --name llamafile-server llamafile-docker
```

That’s it. One build, one run, model served on `localhost:1111`.

## Using Your Local LLM

The Llamafile server provides an OpenAI-compatible API. You can use it with curl, Python, or any tool that speaks OpenAI's format.

Quick Test with curl:

```bash
curl http://localhost:8080/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer no-key" \
-d '{
  "model": "LLaMA_CPP",
  "messages": [
      {
          "role": "system",
          "content": "You are a helpful coding assistant."
      },
      {
          "role": "user",
          "content": "Write a Python function to reverse a string."
      }
    ]
}' | python3 -c '
import json
import sys
json.dump(json.load(sys.stdin), sys.stdout, indent=2)
print()
'
```

The response that's printed should look like the following: 

```json
{
   "choices" : [
      {
         "finish_reason" : "stop",
         "index" : 0,
         "message" : {
            "content" : "Here is a simple Python function to reverse a string:\n\n```python\ndef reverse_string(s):\n    return s[::-1]\n\n# Example usage:\ninput_str = \"Hello, World!\"\nreversed_str = reverse_string(input_str)\nprint(reversed_str)\n```\n\nThis function uses Python's slice notation `[::-1]` to create a reversed copy of the string.",
            "role" : "assistant"
         }
      }
   ],
   "created" : 1704199256,
   "id" : "chatcmpl-Dt16ugf3vF8btUZj9psG7To5tc4murBU",
   "model" : "LLaMA_CPP",
   "object" : "chat.completion",
   "usage" : {
      "completion_tokens" : 38,
      "prompt_tokens" : 78,
      "total_tokens" : 116
   }
}
```

## Troubleshooting Common Issues

### Port Already in Use

**Problem**: `docker run` fails with error: `Error response from daemon: Ports are not available: listen tcp 0.0.0.0:1111: bind: address already in use`

**Solution**: Use a different port. Either modify the `PORT` environment variable during build or map to a different host port:

```bash
docker run -d -p 8888:1111 --name llamafile-server llamafile-docker
```

Then access the API at `http://localhost:8888` instead of `http://localhost:1111`.

To find what's using port 1111 on your machine:

```bash
lsof -i :1111  # Linux/macOS
netstat -ano | findstr :1111  # Windows
```

### Out of Memory Errors

**Problem**: Container crashes with `Segmentation fault` or `CUDA out of memory` errors.

**Solution**: The Llamafile model is 1.3GB+ and requires sufficient system RAM. Allocate more memory to Docker:

1. Update Docker Desktop settings (macOS/Windows):
   - Settings → Resources → Memory: Increase from default (usually 2GB) to 8GB+ if available

2. For Linux, no per-container limit is needed, but ensure your system has sufficient free RAM:

```bash
free -h  # Check available RAM
```

Alternatively, use a smaller model by changing `LLAMAFILE_URL` during build.

### HTTPS/Certificate Errors During Download

**Problem**: Build fails with `curl: (60) SSL certificate problem: unable to get local issuer certificate`

**Solution**: Update CA certificates in the Dockerfile or use an HTTP URL if available:

```dockerfile
RUN apt-get update && apt-get install -y ca-certificates && update-ca-certificates
```

If using an older base image, try upgrading to `debian:bookworm-slim` or add explicit cert handling:

```bash
RUN curl --cacert /etc/ssl/certs/ca-certificates.crt ...
```

### API Endpoint Not Responding

**Problem**: Curl requests to the API fail with `Connection refused` or `No route to host`.

**Solution**: Verify the container is running and listening on the correct port:

```bash
docker ps | grep llamafile  # Check if container is running
docker logs llamafile-server  # Check container logs for startup errors
curl -v http://localhost:1111/v1/models  # Verbose output to debug connection
```

If the port in your curl command doesn't match the mapped port, requests will fail. Verify your `docker run` command maps the port correctly:

```bash
# If you ran: docker run -p 8888:1111 llamafile-docker
# Then access the API at: http://localhost:8888 (not 1111)
```

## Customization Options

Want to use a different model? Update the `LLAMAFILE_URL` and `LLAMAFILE_NAME` build args:

```bash
docker build --build-arg LLAMAFILE_URL="https://huggingface.co/Mozilla/Mixtral-8x7B-Instruct-v0.1-llamafile/resolve/main/mixtral-8x7b-instruct-v0.1.Q4_0.llamafile" LLAMAFILE_NAME="mixtral-8x7b-instruct-v0.1.Q4_0.llamafile" -t custom-llamafile-docker .
```

Want persistent logs? Mount a volume:

```bash
docker run -p 1111:1111 -v $(pwd)/logs:/logs llama-localfile-docker
```

## Why Not Ollama or Other Solutions?

Tools like Ollama, LM Studio, or text-generation-inference are great, but they usually involve more setup work than dropping a single executable into a container.

Ollama, for example, requires installing a host-level service, managing model pulls, and dealing with platform-specific quirks. If you want to ship Ollama inside Docker, you either run it privileged, mount volumes, or build large images that depend on the full Ollama runtime layer.

## Conclusion

By wrapping a Llamafile in Docker, we've eliminated environment setup entirely. You can now deploy this image to a Kubernetes cluster, a friend's laptop, or a cloud VM without worrying about Python versions or CUDA drivers. It just works; **build once, run anywhere**!