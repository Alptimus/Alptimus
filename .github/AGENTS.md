---
name: API.log Agent Behaviors
description: "Define agent workflows and capabilities for API.log workspace. Agents behave differently based on task type: blog post creation, course updates, deployment validation, and general code/documentation edits."
---

# Agent Behaviors for API.log

This document specifies how agents should behave when working on different types of tasks in the API.log project. Use these guidelines to ensure consistent, high-quality outputs across all agent interactions.

---

## Default Agent (All Tasks)

**When**: General code edits, documentation updates, file creation, validation tasks  
**Context**: Automatic. Agents load [copilot-instructions.md](.github/copilot-instructions.md) and project structure on every request.

### Default Behaviors

1. **Always test locally first**
   - For MkDocs tasks: Run `mkdocs serve` and inspect rendered output at `http://localhost:8000`
   - For structural changes: Validate `mkdocs.yml` syntax before committing
   - Never push to GitHub without local verification

2. **Enforce frontmatter requirements**
   - Blog posts: Always check for YAML frontmatter with `created` and `modified` dates
   - If missing or malformed, halt and request correction
   - Dates must be in `YYYY-MM-DD` format

3. **Keep navigation in sync**
   - Any new post or course section must be added to `nav:` in `mkdocs.yml`
   - Use relative paths (e.g., `blog/posts/my-post.md`)
   - Preserve existing navigation order

4. **Follow naming conventions**
   - Blog posts: kebab-case (e.g., `my-post-title.md`)
   - Course sections: kebab-case (e.g., `section-1-2.md`)
   - Code blocks: Always include language tags (`` ```python ``, `` ```bash ``, etc.)

5. **Link, don't duplicate**
   - If content exists elsewhere (another post, README, docs), link to it
   - Avoid repeating information across files
   - Use relative markdown links: `[text](path/file.md)`

---

## Blog Post Agent

**When**: Creating or editing blog posts in `docs/blog/posts/`  
**Triggers**: `/new-blog-post`, editing `.md` files matching `docs/blog/posts/**/*.md`  
**Activation**: Automatic via `applyTo` in [blog-posts.instructions.md](.github/instructions/blog-posts.instructions.md)

### Specialized Behaviors

1. **Enforce blog-post.instructions.md**
   - Load [.github/instructions/blog-posts.instructions.md](.github/instructions/blog-posts.instructions.md) immediately
   - Validate YAML frontmatter before proceeding
   - Verify required content structure: H1 title → problem statement → H2 sections → examples

2. **Use `/new-blog-post` prompt for creation**
   - When user says "create a blog post," invoke the [new-blog-post.prompt.md](.github/prompts/new-blog-post.prompt.md) workflow
   - Follow 5-step scaffold: topic → problem statement → outline → code examples → generation
   - Generate file with correct naming and frontmatter

3. **Validate before saving**
   - Check for language tags in all code blocks
   - Verify no unlabeled code blocks
   - Ensure exactly one H1 title (first line after frontmatter)
   - Confirm problem statement is 2-3 sentences
   - Test code examples locally if possible

4. **Update modified date**
   - Always update the `modified` field in YAML frontmatter to today's date
   - Format: `YYYY-MM-DD` (e.g., `2026-03-30`)

---

## Course Update Agent

**When**: Editing course sections in `docs/courses/django/` or `docs/courses/aws/`  
**Context**: Course sections are long-form, may link to external resources, include checkpoint questions

### Specialized Behaviors

1. **Preserve structure**
   - Don't reorder sections without explicit request
   - Keep section numbering (e.g., `section-1-2.md`, `section-3.md`)
   - Respect existing asset organization in `courses/*/assets/`

2. **Link to external resources**
   - Include relevant links to official docs (Django, AWS)
   - Use descriptive link text: `[Django Models](https://docs.djangoproject.com/)`, not "click here"
   - Verify links are valid before saving

3. **Test code snippets**
   - Course code examples should be production-ready or clearly marked as "example only"
   - If including shell commands, test them locally first
   - Always include code block language tags

4. **Update modified date**
   - Like blog posts, update `modified` in YAML frontmatter when making changes

---

## Deployment Agent

**When**: Validating deployment, checking GitHub Actions, reviewing build errors  
**Context**: GitHub Actions workflow is in [.github/workflows/](../.github/workflows/)

### Specialized Behaviors

1. **Pre-deployment checklist**
   - ✅ All files have valid YAML frontmatter (frontmatter must parse)
   - ✅ `mkdocs.yml` syntax is valid (YAML)
   - ✅ All posts/sections are in `nav:` section
   - ✅ No broken internal links (relative paths exist)
   - ✅ Code blocks have language tags
   - ✅ Local `mkdocs serve` runs without warnings

2. **Inspect workflow output**
   - If GitHub Actions fails, check the workflow logs in Actions tab
   - Common failures: missing `modified` date, invalid YAML, syntax errors in code blocks
   - Report specific line numbers and file paths

3. **Rollback guidance**
   - If deployment fails, the previous version remains live
   - Safe to revert and retry after fixing errors

---

## General Workflows

### Creating a New Blog Post

1. User: `/new-blog-post` or "create a new blog post"
2. Agent: Load [new-blog-post.prompt.md](.github/prompts/new-blog-post.prompt.md)
3. Workflow: 5-step scaffold (topic → problem → outline → examples → generate)
4. Output: File in `docs/blog/posts/kebab-case-title.md` with frontmatter + content
5. Next: Add to `mkdocs.yml` nav, test with `mkdocs serve`

### Updating an Existing Blog Post

1. User: "Update [post name]" or edit file directly
2. Agent: Load [blog-posts.instructions.md](.github/instructions/blog-posts.instructions.md)
3. Actions: Edit content, update `modified` date in frontmatter
4. Validation: Test with `mkdocs serve`, verify rendered output
5. Next: Commit and push triggers GitHub Actions → automatic deploy

### Deploying to GitHub Pages

1. **Local test first**: `mkdocs serve` (verify all posts render)
2. **Build static site**: `mkdocs build` (generates `site/` directory)
3. **Commit changes**: Commit markdown files and `.github/` customizations
4. **Push to main**: GitHub Actions automatically runs `mkdocs build` and deploys
5. **Verify**: Check GitHub Pages URL after 1-2 minutes

---

## Tool Usage Guidelines

### Recommended Tool Patterns

- **File edits**: Use `replace_string_in_file` or `multi_replace_string_in_file` (include 3-5 lines of context)
- **Multiple edits**: Batch with `multi_replace_string_in_file` for efficiency
- **File exploration**: Use `read_file`, `file_search`, `grep_search` in parallel
- **Terminal commands**: Use `run_in_terminal` for MkDocs serve/build only; never run destructive commands

### Tools to Avoid

- ❌ Editing files via shell commands (`sed`, `awk`, etc.) — use file tools instead
- ❌ Manual YAML parsing — ensure frontmatter is syntactically valid before saving
- ❌ Creating temporary files for documentation — write directly to final location
- ❌ Running arbitrary shell scripts — only MkDocs build/serve commands

---

## Key Files & Paths

| Purpose | Path |
|---------|------|
| Main workspace guide | [.github/copilot-instructions.md](.github/copilot-instructions.md) |
| Blog post standards | [.github/instructions/blog-posts.instructions.md](.github/instructions/blog-posts.instructions.md) |
| New post workflow | [.github/prompts/new-blog-post.prompt.md](.github/prompts/new-blog-post.prompt.md) |
| Site config | [mkdocs.yml](../../mkdocs.yml) |
| Blog posts | `docs/blog/posts/` |
| Course content | `docs/courses/{django,aws}/` |
| Build artifacts | `site/` (generated, not committed) |
| Deployment workflow | [.github/workflows/deploy.yml](.github/workflows/deploy.yml) |

---

## Questions & Escalation

**If uncertain**:
- Check [copilot-instructions.md](.github/copilot-instructions.md) for project overview
- Review [blog-posts.instructions.md](.github/instructions/blog-posts.instructions.md) for content standards
- Ask the user for clarification instead of guessing

**If something breaks**:
- Always test locally with `mkdocs serve` before pushing
- If GitHub Actions fails, check workflow logs and report the error clearly
- Safe to revert and retry; previous version remains live
