---
name: blog-posts
description: "Use when editing or creating blog posts in docs/blog/posts/. Enforce YAML frontmatter requirements, content structure, and writing conventions for API.log posts."
applyTo: "docs/blog/posts/**/*.md"
---

# Blog Post Instructions

These instructions apply when you create or edit blog posts in the `docs/blog/posts/` directory.

## Required YAML Frontmatter

Every blog post **must** start with YAML frontmatter containing publication and modification dates. **Do not proceed** if frontmatter is missing or invalid.

```yaml
---
date:
    created: YYYY-MM-DD
    modified: YYYY-MM-DD
---
```

- `created`: Date the post was first published (format: `YYYY-MM-DD`)
- `modified`: Date the post was last updated (format: `YYYY-MM-DD`, update this whenever you make changes)

**Example**:
```yaml
---
date:
    created: 2025-11-18
    modified: 2026-03-30
---
```

> ⚠️ **Critical**: Frontmatter is required by the MkDocs blog plugin. Missing or malformed dates will break the blog navigation and post listings. Always include both `created` and `modified`.

## File Naming

Use **kebab-case** (lowercase with hyphens) for post filenames:

- ✅ Good: `llamafile_docker.md`, `python-async-patterns.md`, `docker-networking-guide.md`
- ❌ Bad: `LlamafileDocker.md`, `Python Async Patterns.md`, `Docker_Networking_Guide.md`

## Content Structure

Follow this proven structure for all posts:

### 1. H1 Title (Required)
- **Exactly one** H1 title (`# Title`) 
- Must be the first line **after** frontmatter
- Should be clear and descriptive
- Example: `# Run LLMs Anywhere as a Single File with Docker`

### 2. Problem or Context (Required)
- Brief introductory paragraph explaining **why this matters**
- Answer: "What problem does this solve?" or "Why would someone read this?"
- Keep it to 2-3 sentences; readers should immediately understand the relevance
- Example: *"Deploying LLMs can be a hassle on local machines. It involves setting up Python environments, CUDA drivers, and model downloads. But as a developer who switches between OSes, I needed something portable..."*

### 3. Solution/Main Content (H2 Sections)
- Break content into logical sections with **H2 headings** (`## Heading`)
- Common patterns:
  - `## The Solution`
  - `## Prerequisites`
  - `## Step-by-Step Guide`
  - `## Implementation`
  - `## Configuration`
  - `## Troubleshooting`
  - `## Customization Options`
  - `## Conclusion`

- Keep sections focused; if a section is very long (>500 words), split it into subsections (H3)

### 4. Code Blocks (Always Specify Language)
- **Always** include a language identifier after triple backticks:
  ```markdown
  ```python
  # Code here
  ```
  ```

- Common languages: `bash`, `python`, `javascript`, `dockerfile`, `yaml`, `json`, `sql`, `markdown`
- Use `bash` for shell commands and scripts
- Never use unlabeled code blocks (` ``` ` without language)

### 5. Practical Examples
- Include real-world usage examples, not just theory
- Show how to test or verify that something works
- Provide before/after comparisons when helpful

### 6. Conclusion (Recommended)
- Wrap up with key takeaways
- Optional: suggest next steps or related topics
- Example: *"By wrapping a Llamafile in Docker, we've eliminated environment setup entirely..."*

### 7. Excerpt/Teaser (Optional)
- Use the `<!-- more -->` HTML comment to mark the preview cutoff for blog listings
- Everything **before** this comment appears in blog previews
- Place after your introductory problem/context paragraph
- Example:
  ```markdown
  ## The Problem
  
  [Problem description...]
  
  <!-- more -->
  
  ## The Solution
  
  [Detailed solution...]
  ```

## Writing Style & Tone

- **Tone**: Practical, direct, friendly — write as if teaching a colleague
- **Avoid**: Vague theory, "best practices" without examples, overly academic language
- **Aim for**: 500–3,000 words (complete, useful content; not too short, not a novel)
- **Problem → Solution**: Always start with the problem you're solving, then show the solution

## Markdown Formatting

- **Inline code** (backticks): Use for `commands`, `variables`, `file names`, `class names`, `functions()`
  - Example: *"Run `docker build -t my-image .` to build the image"*
  
- **Bold** (double asterisks): Use for key concepts, important terms
  - Example: *"Always verify the **modified** date is updated when you edit a post"*

- **Links**: Use markdown link syntax `[text](url)` for external references
  - Example: `[Read the Docker docs](https://docs.docker.com)`

- **Lists**: Use `-` for unordered, `1.` for ordered (numbered)
  - Keep list items concise
  - Use 4 spaces to indent sub-items

- **Emphasis**: Avoid ALL CAPS for emphasis; use **bold** or *italic* instead

- **Headings**: Use H1 for title only. Use H2 for sections. Use H3 rarely, for subsections only.

## Update Checklist

When you edit an existing post, **always**:

- [ ] Update the `modified` date in frontmatter to today's date (`YYYY-MM-DD`)
- [ ] Review the structure; ensure it still follows the outline above
- [ ] Test locally with `mkdocs serve` and verify the rendered output in a browser
- [ ] Check that code blocks render correctly with syntax highlighting
- [ ] Verify all links are working

## Testing

Before committing changes:

1. **Install dependencies**: `pip install -r requirements.txt` (if not already done)
2. **Serve locally**: `mkdocs serve` — opens dev server at `http://localhost:8000`
3. **Verify your post**:
   - Navigate to the blog section and find your post
   - Check that the title, content, and code blocks render correctly
   - Verify the post appears in the blog navigation and listings
   - Test any links (internal and external)
4. **Stop server**: Press `Ctrl+C` in the terminal

## Further Reference

For complete project guidelines, conventions, and context, see:
- [.github/copilot-instructions.md](../../.github/copilot-instructions.md) — Full workspace instructions
- [mkdocs.yml](../../mkdocs.yml) — Site configuration, theme, and plugins
- [docs/blog/posts/llamafile_docker.md](../../docs/blog/posts/llamafile_docker.md) — Example post (reference implementation)

## Common Pitfalls

- ❌ **Missing frontmatter**: Post will not appear in blog listings or may break navigation
- ❌ **Unlabeled code blocks**: Code will display without syntax highlighting, making it hard to read
- ❌ **Multiple H1 titles**: Confuses the blog plugin and makes navigation unclear
- ❌ **Not updating `modified` date**: Misleads readers about when content was last reviewed/updated
- ❌ **Inconsistent markdown**: Mixes uppercase/lowercase headings, inconsistent link format, etc.
- ❌ **Theory-only content**: Readers want practical, showable solutions — always include examples and commands

## Questions?

Refer to the example post at `docs/blog/posts/llamafile_docker.md` or the workspace instructions at `.github/copilot-instructions.md` for clarification.
