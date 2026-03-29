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

### File Naming & Location
- **Location**: `docs/blog/posts/` directory
- **Naming**: Use kebab-case (lowercase with hyphens): `my-guide-title.md`
- **Example**: `llamafile_docker.md`

### YAML Frontmatter
Every blog post must include metadata at the top:

```yaml
---
date:
    created: YYYY-MM-DD
    modified: YYYY-MM-DD
---

# Post Title
```

- `created`: Publication date  
- `modified`: Last update date (update when making changes)

### Content Structure
Follow this proven structure for posts:

1. **H1 Title** (one only, first line after frontmatter)
   ```markdown
   # How to Run LLMs with Docker
   ```

2. **Problem or Context** (brief intro paragraph explaining why this matters)

3. **Step-by-step sections** (H2 headings for major sections)
   ```markdown
   ## Prerequisites
   ## Installation Steps
   ## Configuration
   ## Troubleshooting
   ```

4. **Code blocks** (always specify language)
   ```markdown
   ```bash
   mkdocs serve
   ```
   ```

5. **Practical examples** (real-world usage, not just theory)

6. **Excerpt teaser** (optional, for blog listing preview)
   ```markdown
   <!-- more -->
   ```
   Everything before this comment will appear in blog previews.

### Writing Style

- **Tone**: Practical, direct, friendly — write as if teaching a colleague
- **Length**: 500-3000 words (aim for complete, useful content)
- **Format**: Problem → Solution format; avoid vague or purely theoretical content
- **Code**: Use inline code for `commands`, `variables`, and `terms`
- **Links**: Use markdown links `[text](url)` for references to external resources
- **Emphasis**: Use **bold** for key concepts, `code` for technical terms

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
1. Create file: `docs/blog/posts/your-title.md`
2. Add YAML frontmatter with dates
3. Write content following the structure above
4. Add to `mkdocs.yml` nav section
5. Test locally: `mkdocs serve`

### Update an Existing Post
1. Edit the markdown file
2. Update the `modified` date in frontmatter
3. Test: `mkdocs serve`
4. Rebuild: `mkdocs build`

### Deploy
The site is configured for deployment via [mkdocs.yml](../mkdocs.yml). Push changes to deploy (GitHub Pages or manual hosting).

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
