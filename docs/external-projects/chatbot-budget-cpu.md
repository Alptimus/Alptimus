---
date:
    created: 2026-03-30
    modified: 2026-03-30
---

# LangChain-Free RAG Chatbot: Budget 2024 (Part I)

Building a custom chatbot to interact with complex documents is often unnecessarily complicated. Most tutorials push you toward heavy frameworks like LangChain, Haystack, or LlamaIndex. But these frameworks come with bloat, require numerous dependencies, and often lack practical documentation. This tutorial shows you a better way: build a production-capable RAG (Retrieval-Augmented Generation) chatbot in pure Python with minimal dependencies.

## The Problem

When you want to query large documents (like India's 2024 budget speech), simply feeding the entire document to an LLM hits context length limits. You need intelligent retrieval. Most developers reach for LangChain or similar frameworks, but ask yourself: do I really need all that overhead?

The answer is often no. With raw Python and a few well-chosen libraries, you can build something lighter, more maintainable, and easier to customize.

## The Approach: Framework-Free RAG

This tutorial demonstrates a complete RAG pipeline without heavy frameworks:

- **Document Loading**: Simple Python classes to load and organize your documents
- **Chunking**: Split long documents into overlapping chunks to preserve context
- **Embeddings**: Use TF-IDF (sparse embeddings) for fast, lightweight vector representation
- **Vector Storage**: Store embeddings in FAISS (Facebook AI Similarity Search) for efficient retrieval
- **Inference**: Run open-source LLMs locally using Llamafile (no GPU needed, no API keys)

## Key Technologies

**Llamafile**: Mozilla's open-source project that bundles LLMs into single executables. Game-changer for developers—run LLMs anywhere, CPU or GPU, without installation complexity.

**FAISS**: Facebook's vector search library. Lightweight, fast, and CPU-friendly. Perfect for similarity searches across document chunks.

**TF-IDF**: Classic sparse embedding approach. Lighter than dense embeddings, surprisingly effective for document retrieval, and requires no model downloads.

**Python Standard**: Pure Python with minimal dependencies (docx2txt, scikit-learn, requests). Easy to install, easy to understand, easy to modify.

## What You'll Learn

- How to load and preprocess documents programmatically
- Building a custom document chunking system with overlap for context preservation
- Creating and storing embeddings without cloud APIs or heavy dependencies
- Performing similarity search to find relevant context for user queries
- Integrating with open-source LLMs via Llamafile for CPU-based inference
- Constructing effective prompts to guide model behavior
- Building a complete Q&A system that works offline

## Project Structure

The tutorial walks you through:

1. **Load the Document** — Custom loader for DOCX files
2. **Chunk the Docs** — Create overlapping chunks with configurable size
3. **Create Embeddings** — TF-IDF vectorization and FAISS storage
4. **Similarity Search** — Retrieve top-k relevant chunks for a query
5. **Prompt Engineering** — Structure prompts for accurate answers
6. **Run Llamafile on CPU** — Execute open-source LLM locally
7. **Chat with the Bot** — Complete Q&A workflow

## Example

```python
# Simple usage after setup
query = "Who represented the Budget 2024?"
similar_chunks = index.search(query, k=10)
answer = bot.chat(prompt_template, similar_chunks, query)
# Output: "The Budget 2024 was presented by Finance Minister Nirmala Sitharaman."
```

## Why This Matters

- **No Vendor Lock-in**: Uses open-source tools and local infrastructure
- **Cost Effective**: Zero API costs, no cloud bills
- **Customizable**: Raw Python means you control every part
- **Portable**: Works on any machine with Python installed
- **Educational**: Learn how RAG actually works, not just how to call an API

## Resources

**Full Tutorial**: [Chat with India's Budget 2024 (Part I): LangChain-Free RAG on Local CPU](https://www.aimplabs.org/blogs/chatbot-budget2024/index.html)

**Code & Examples**: [AIMP Labs GitHub Repository](https://github.com/aimplabs)

**Next Step**: Ready to run this on free cloud GPU? See [Part II](chatbot-budget-colab.md) for the Google Colab variant.
