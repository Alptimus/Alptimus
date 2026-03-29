# API.log Workspace Instructions

**Project**: A personal developer's blog and documentation site documenting hard-won findings from AI and software development.

---

## Quick Start

1. **Install dependencies**: `pip install -r requirements.txt`
2. **Serve locally**: `mkdocs serve` — opens development server at `http://localhost:8000`
3. **Build static site**: `mkdocs build` — generates production site in `site/` directory

---

## Project Structure

```
docs/
├── index.md              # Home page
└── blog/
    ├── index.md          # Blog landing page
    └── posts/            # Individual blog posts
        └── llamafile_docker.md  # Example: "Run LLMs with Docker"
mkdocs.yml                # Site configuration (Material theme, plugins)
requirements.txt          # Python dependencies (mkdocs-material)
.github/
└── copilot-instructions.md  # This file
```

The site is built with **MkDocs** using the **Material for MkDocs** theme, configured in [mkdocs.yml](../mkdocs.yml).

---

## Blog Post Conventions

For detailed blog post standards (file naming, YAML frontmatter, content structure, writing style, and markup), see [blog-posts.instructions.md](.github/instructions/blog-posts.instructions.md). This applies to all content in `docs/blog/posts/`.

**Quick reference**:
- **Location**: `docs/blog/posts/` directory
- **Naming**: kebab-case (e.g., `my-post-title.md`)
- **Frontmatter**: Required YAML with `created` and `modified` dates
- **Structure**: H1 title, problem context, H2 sections, code blocks (with language tags), practical examples
- **Tone**: Practical, direct, friendly — write as if teaching a colleague

For the full standard and editorial checklist, refer to the [detailed instructions](.github/instructions/blog-posts.instructions.md)

---

## Key MkDocs Configuration

Review [mkdocs.yml](../mkdocs.yml) for:
- **Theme**: Material with features enabled (code copy, navigation footer, search, blog plugin)
- **Markdown extensions**: Syntax highlighting, inline code, snippets, superfences
- **Navigation**: Auto-generated from `nav` section

When adding new posts, manually add them to the `nav` section:
```yaml
nav:
  - Home: index.md
  - Blog:
     - blog/index.md
     - blog/posts/your-new-post.md
```

---

## Common Tasks

### Create a New Blog Post
Use the `/new-blog-post` prompt (or run `new-blog-post.prompt.md`) for a guided workflow that scaffolds structure and guides writing:
1. Provide topic and title
2. Define problem statement
3. Outline main sections
4. Draft code examples and practical content

Alternatively, manual steps:
1. Create file: `docs/blog/posts/your-title.md`
2. Add YAML frontmatter with dates (see [blog-posts.instructions.md](.github/instructions/blog-posts.instructions.md))
3. Write content following the structure
4. Add to `mkdocs.yml` nav section
5. Test locally: `mkdocs serve`

### Update an Existing Post
1. Edit the markdown file
2. Update the `modified` date in frontmatter
3. Test: `mkdocs serve`
4. Rebuild: `mkdocs build`

---

## Deployment & CI/CD

The site automatically deploys to **GitHub Pages** on every push to the `main` branch via [GitHub Actions](.github/workflows/deploy.yml).

### Prerequisites
- GitHub Pages is enabled in repository settings (Settings → Pages → Source: GitHub Actions)
- Repository secrets are configured (if needed; currently using default GITHUB_TOKEN)

### How It Works
1. Push changes to `main` branch
2. GitHub Actions workflow (`.github/workflows/deploy.yml`) triggers automatically
3. Workflow installs dependencies, runs `mkdocs build`, and uploads the `site/` directory
4. Site is deployed to `https://<username>.github.io/<repo>/`

### Local Testing Before Push
Always test your site locally before pushing to avoid deployment failures:

```bash
# Install dependencies (first time only)
pip install -r requirements.txt

# Start local development server
mkdocs serve

# Open http://localhost:8000 in your browser
# Verify that all posts render correctly, links work, code highlighting works
```

Press `Ctrl+C` to stop the server when done.

### Build Static Site
To generate the production site locally (what GitHub Actions does):

```bash
mkdocs build
# Generates site/ directory with all HTML, CSS, JS
```

Review the `site/` directory to inspect the final output before pushing.

### Troubleshooting Deployment Failures

**Workflow fails with Python version error**
- The workflow uses Python 3.11. Ensure `requirements.txt` only contains packages compatible with Python 3.11+.

**MkDocs build fails locally but workflow still runs**
- Check the Actions tab in GitHub to see the full error log. Common issues:
  - Missing dependencies: Run `pip install -r requirements.txt` again
  - Invalid YAML in `mkdocs.yml` or post frontmatter: Check syntax with a YAML validator
  - Missing `modified` date in blog post frontmatter: Required by the blog plugin

**Site doesn't appear at expected URL**
- Verify GitHub Pages is enabled and set to deploy from GitHub Actions (Settings → Pages)
- Check that the workflow completed successfully (Actions tab → latest run)
- Wait 1-2 minutes after workflow succeeds; GitHub Pages may take time to update

**Links are broken after deployment**
- Ensure all markdown links use relative paths (e.g., `[text](docs/file.md)`, not absolute URLs)
- Test locally with `mkdocs serve` to verify links work before pushing

---

## Notes for AI Agents

- **Always test locally** before committing: Run `mkdocs serve` and verify the rendered output
- **Preserve frontmatter**: YAML dates are required for blog plugin functionality
- **Keep post titles unique** to avoid MkDocs navigation conflicts
- **Link, don't duplicate**: If content exists elsewhere (README, another post), link to it instead of repeating
- **Single post per file**: Each markdown file should contain one complete blog post
- **README.md is a template**: The GitHub profile README is not aligned with the project; don't mirror content there

---

## File References

- [mkdocs.yml](../mkdocs.yml) — Site configuration
- [requirements.txt](../requirements.txt) — Python dependencies  
- [Example post](../docs/blog/posts/llamafile_docker.md) — Reference for structure and style
- [Home page](../docs/index.md) — Site homepage
