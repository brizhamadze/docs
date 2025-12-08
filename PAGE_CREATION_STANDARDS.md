# Mintlify Page Creation Standards

This document outlines the standards for creating pages in the HealthTech Mintlify documentation.

## 🔴 Critical: Duplicate Title Issue

### The Problem
Mintlify **automatically creates an `<h1>` heading** from the frontmatter `title` field. If you also include a `# Title` in the markdown content, it creates a duplicate large title that looks unprofessional.

### The Solution
**DO NOT** include an h1 heading (`# Title`) in your markdown content. The frontmatter `title` is sufficient.

### ❌ Incorrect Example
```mdx
---
title: 'თორნიკე რაზმაძე'
description: 'Principal Software Engineer'
---

# თორნიკე რაზმაძე  ← REMOVE THIS! Mintlify creates it automatically

<Frame>
  <img src="/images/team/tornike-razmadze.png" alt="თორნიკე რაზმაძე" />
</Frame>
```

### ✅ Correct Example
```mdx
---
title: 'თორნიკე რაზმაძე'
description: 'Principal Software Engineer'
---

<Frame>
  <img src="/images/team/tornike-razmadze.png" alt="თორნიკე რაზმაძე" />
</Frame>

## პოზიცია

**Principal Software Engineer**
```

## 📝 Page Structure Standards

### Frontmatter (Required)
Every page must start with frontmatter:

```mdx
---
title: 'Page Title in Georgian'
description: 'Brief description for SEO and previews'
---
```

### Content Structure
- Start directly with content (no h1)
- Use h2 (`##`) for main sections
- Use h3 (`###`) for subsections
- Use appropriate Mintlify components (`<Card>`, `<Frame>`, `<Note>`, etc.)

## 🎨 Tone Guidelines

### Team Pages
**Style:** Friendly, welcoming, conversational

**Guidelines:**
- Start with "გაიცანით [Name]" (Meet [Name]) or similar welcoming introduction
- Use warm, conversational tone
- Focus on their role at Radium and what visitors should know
- Keep it to 1-2 paragraphs
- Avoid CV-style lists of experience
- Write as if introducing a colleague to visitors

**Example:**
```mdx
## ჩვენი გუნდის წევრი

გაიცანით თორნიკე რაზმაძე - ჩვენი Principal Software Engineer, რომელიც ხელმძღვანელობს HealthTech პლატფორმის ტექნიკურ განვითარებას...
```

### Feature/Guide Pages
**Style:** Professional, clear, instructional

**Guidelines:**
- Use direct, clear language
- Focus on helping users accomplish tasks
- Use imperative mood when appropriate ("დააჭირეთ" not "თქვენ უნდა დააჭიროთ")
- Include examples and practical steps

### Tutorial Pages
**Style:** Encouraging, step-by-step, supportive

**Guidelines:**
- Break down complex tasks into clear steps
- Use encouraging language
- Include tips and best practices
- Show expected outcomes

## 🌐 Language Requirements

**ALL documentation must be in Georgian (ka)**
- ✅ Titles, headings, paragraphs in Georgian
- ✅ Filenames in English (e.g., `tornike-razmadze.mdx`)
- ❌ No English in page content
- ❌ No mixing of languages

## 📋 Checklist for New Pages

Before creating a new page, ensure:

- [ ] Frontmatter includes `title` and `description` in Georgian
- [ ] No duplicate h1 heading in markdown (frontmatter `title` is enough)
- [ ] Content starts directly (no `# Title`)
- [ ] All text content is in Georgian
- [ ] Appropriate tone for page type (team/feature/tutorial)
- [ ] Uses appropriate Mintlify components
- [ ] Image paths are correct (if using images)
- [ ] Navigation entry added to `mint.json` (if needed)

## 🔍 Common Mistakes to Avoid

1. **Duplicate h1** - Most common mistake! Frontmatter `title` creates it automatically
2. **English content** - All content must be in Georgian
3. **Wrong tone** - Team pages should be friendly, not CV-style
4. **Missing frontmatter** - Always include `title` and `description`
5. **Forgetting navigation** - Add page to `mint.json` if it should appear in sidebar

## 📚 Related Documentation

- [Mintlify Documentation Workflow](./.cursor/rules/always_applied_workspace_rules) - Main workflow rules
- [Mintlify Overview](./MINTLIFY_OVERVIEW.md) - Project structure overview

## 🔄 Updating Existing Pages

When updating existing pages:
1. Check if they have duplicate h1 headings
2. Update tone if it's a team page
3. Ensure all content is in Georgian
4. Follow the structure standards above

---

**Last Updated:** December 8, 2025

