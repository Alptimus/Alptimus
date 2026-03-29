---
name: new-blog-post
description: "Create a new blog post with guided workflow. Helps scaffold structure, define problem statement, outline sections, and draft content. Follows API.log conventions."
---

# Create a New Blog Post

This prompt guides you through creating a complete blog post for API.log, from topic selection through final structure.

## Step 1: Define Your Topic

What topic or problem are you documenting? Be specific and actionable.

**Examples:**
- "Run LLMs locally with Docker"
- "Async patterns in Python for beginners"
- "Debugging memory leaks in Node.js"

*Your topic:*

---

## Step 2: Write the Problem Statement

Explain **why this matters** in 2-3 sentences. What problem does this solve? Who would benefit?

**Example for "Run LLMs with Docker":**
*"Deploying large language models (LLMs) can be a hassle on local machines. It involves setting up Python environments, CUDA drivers, and managing model downloads. As a developer who switches between different operating systems, I needed something portable that runs the same way everywhere."*

*Your problem statement:*

---

## Step 3: Outline Main Sections

What are the key sections (H2 headings) your post will cover? List them:

**Common patterns:**
- `## The Problem` (brief restatement)
- `## The Solution` or `## How to Get Started`
- `## Prerequisites`
- `## Step-by-Step Guide` (or break into smaller sections)
- `## Configuration Options`
- `## Practical Examples` (real-world usage)
- `## Troubleshooting`
- `## Conclusion`

*Your outline (list H2 headings):*

---

## Step 4: Draft Code Examples & Practical Content

For each technical section, outline:
- **What you're showing**: (brief description)
- **Code snippet**: (language: bash, python, dockerfile, etc.)
- **How to test it**: (verification step)

*Your technical sections:*

---

## Step 5: Generate the Blog Post Structure

Once you've answered the above, I'll create:

1. **File**: `docs/blog/posts/your-title.md` (kebab-case naming)
2. **Frontmatter**: YAML with `created` and `modified` dates (today's date: 2026-03-30)
3. **H1 Title**: From your topic
4. **Content structure**: Problem statement → sections → examples → conclusion
5. **Editorial checklist**: Verify code blocks have language tags, links work, examples are clear

---

## Blog Post Standards

Follow these conventions (enforced by [blog-posts.instructions.md](../../.github/instructions/blog-posts.instructions.md)):

### File Naming
- Use **kebab-case** (lowercase with hyphens): `my-post-title.md`

### Required YAML Frontmatter
```yaml
---
date:
    created: YYYY-MM-DD
    modified: YYYY-MM-DD
---
```

### Content Structure
- **One H1 title** (first line after frontmatter)
- **Problem or context paragraph** (2-3 sentences explaining why this matters)
- **H2 sections** for main content (e.g., `## Prerequisites`, `## Step-by-Step Guide`, `## Troubleshooting`)
- **Code blocks with language tags**: Always use ` ```python `, ` ```bash `, ` ```dockerfile `, etc. — never unlabeled code blocks
- **Practical examples**: Real-world usage, not just theory
- **Optional**: `<!-- more -->` comment to mark blog preview cutoff

### Writing Style
- **Tone**: Practical, direct, friendly — write as if teaching a colleague
- **Length**: 500–3,000 words (complete, useful content)
- **Format**: Problem → Solution
- **Code**: Use inline code for `commands`, `variables`, `file names`, `functions()`
- **Bold** for key concepts and important terms
- **Markdown links** for external references: `[text](url)`

---

## Next Steps

Once I generate the post structure:

1. **Add to `mkdocs.yml`**: Add your post to the `nav` section:
   ```yaml
   - blog/posts/your-title.md
   ```

2. **Test locally**:
   ```bash
   mkdocs serve
   # Open http://localhost:8000 and verify the post renders correctly
   ```

3. **Review the editorial checklist** below before finalizing

4. **Push to `main` branch**: Automatic deployment to GitHub Pages

---

## Editorial Checklist

Before publishing, verify:

- [ ] **Frontmatter**: Both `created` and `modified` dates present in `YYYY-MM-DD` format
- [ ] **H1 Title**: Exactly one H1 title, first line after frontmatter, descriptive
- [ ] **Problem/Context**: 2-3 sentences explaining why this matters, right after title
- [ ] **H2 Sections**: All main content has H2 headings (`## Heading`); no orphan paragraphs
- [ ] **Code blocks**: Every code block has a language tag (` ```bash `, ` ```python `, etc.)
- [ ] **Practical examples**: Includes real-world usage, not just theory
- [ ] **Links**: All external links use markdown syntax `[text](url)` and point to valid URLs
- [ ] **Inline code**: Uses backticks for commands, variables, file names, class names
- [ ] **Local test**: Ran `mkdocs serve` and verified rendering in browser
- [ ] **File name**: Uses kebab-case (lowercase with hyphens)
- [ ] **Navigation**: Added entry to `mkdocs.yml` nav section

---

**Ready to create your post?** Provide your answers to Steps 1–4 above, and I'll generate the full markdown file and guide you through publishing.
