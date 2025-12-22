# 🎯 Mintlify + Cursor Integration Setup

**Status:** ✅ Complete  
**Last Updated:** December 23, 2025

---

## 📖 Overview

This document explains how the HealthTech documentation integrates with Cursor AI using **Cursor Project Rules** (not MCP, as Mintlify doesn't have an official MCP server).

Based on: [Mintlify Cursor Guide](https://www.mintlify.com/docs/guides/cursor)

---

## ✅ What's Already Set Up

### 1. Cursor Project Rules

**Location:** `.cursor/rules/`

All contributors (and AI agents) automatically get these rules applied:

#### Primary Rule: `mintlify_technical_writing.mdc` ⭐

**Purpose:** Complete Mintlify technical writing standards  
**Scope:** `Radium/RadiumProjects/Tutorials/docs/**/*.mdx`  
**Always Applied:** Yes

**Contains:**
- ✅ Core writing principles
- ✅ Georgian language requirements
- ✅ Complete Mintlify component reference with examples
- ✅ Required page structure (no duplicate H1 rule)
- ✅ Content quality standards
- ✅ Video tutorial workflow
- ✅ Deployment checklist
- ✅ Common mistakes to avoid
- ✅ Example pages

#### Secondary Rule: `docs_workflow.mdc`

**Purpose:** Quick reference and deployment requirements  
**Scope:** `Radium/RadiumProjects/Tutorials/docs/**/*`  
**Always Applied:** Yes

**Contains:**
- Quick reference to main rule
- Video workflow commands
- Deployment requirements

### 2. Documentation Files

**Location:** `Radium/RadiumProjects/Tutorials/docs/`

| File | Purpose |
|------|---------|
| `DOCUMENTATION_INDEX.md` | Single source of truth for navigation |
| `PAGE_CREATION_STANDARDS.md` | Page structure and tone guidelines |
| `MINTLIFY_OVERVIEW.md` | Progress tracking and structure overview |
| `MINTLIFY_CURSOR_SETUP.md` | This file - integration explanation |

### 3. Cursor Commands

**Location:** `.cursor/commands/`

| Command | Purpose |
|---------|---------|
| `/mintlify-docs` | Complete Mintlify documentation guide |
| `/georgian-text` | Generate Georgian text content |

---

## 🎯 How It Works

### For AI Agents

**When working in documentation files:**

1. **Auto-loaded context:**
   - Cursor automatically applies `mintlify_technical_writing.mdc`
   - File glob `**/*.mdx` ensures rule applies to all MDX files
   - `alwaysApply: true` means no manual activation needed

2. **Available knowledge:**
   - Complete Mintlify component reference
   - Georgian language requirements
   - Page structure standards
   - Video workflow commands
   - Deployment procedures

3. **Decision flow:**
   ```
   User requests documentation change
   ↓
   Cursor loads mintlify_technical_writing.mdc
   ↓
   Agent follows standards automatically
   ↓
   Creates/updates page with correct:
   - Georgian language
   - No duplicate H1
   - Proper components
   - Navigation updates
   ↓
   Deploys with required_permissions: ["all"]
   ```

### For Human Contributors

**When editing documentation:**

1. **IDE assistance:**
   - Cursor suggests Mintlify components
   - Autocomplete for Georgian content patterns
   - Lint warnings for common mistakes

2. **Access to examples:**
   - Rule file contains full component examples
   - Can reference existing pages
   - Clear "don't do this" examples

3. **Command palette:**
   - Use `/mintlify-docs` for guidance
   - Use `/georgian-text` to generate content

---

## 📂 File Organization

```
Medspace/
├── .cursor/
│   ├── rules/
│   │   ├── mintlify_technical_writing.mdc  ⭐ PRIMARY
│   │   ├── docs_workflow.mdc               (Quick ref)
│   │   ├── agent_context.mdc               (Workspace context)
│   │   └── business_overview.mdc           (Business context)
│   │
│   └── commands/
│       ├── mintlify-docs.md                 📚 Main command
│       └── georgian-text.md                 🇬🇪 Text generator
│
└── Radium/
    └── RadiumProjects/
        └── Tutorials/
            └── docs/                         📁 DOCUMENTATION ROOT
                ├── DOCUMENTATION_INDEX.md    ⭐ Navigation guide
                ├── MINTLIFY_CURSOR_SETUP.md  ⭐ This file
                ├── PAGE_CREATION_STANDARDS.md
                ├── MINTLIFY_OVERVIEW.md
                ├── mint.json                 (Navigation config)
                ├── index.mdx                 (Landing page)
                │
                ├── getting-started/
                ├── search/
                ├── space-management/
                ├── patients-files/
                ├── dicom-viewer/
                ├── sharing/
                ├── workflows/
                ├── ai-chat/
                ├── blog/
                ├── tutorials/                🎥 Video tutorials
                ├── images/                   🖼️ Assets
                └── videos/                   🎬 Video files
```

---

## 🔄 Rule Loading Logic

### How Cursor Applies Rules

1. **File-based triggering:**
   ```yaml
   globs: Radium/RadiumProjects/Tutorials/docs/**/*.mdx
   ```
   - When you open any `.mdx` file in the docs folder
   - Cursor automatically loads the rule
   - Agent has full context immediately

2. **Always applied:**
   ```yaml
   alwaysApply: true
   ```
   - Rule is active for all relevant files
   - No need to manually activate
   - Consistent across all contributors

3. **Scope control:**
   - Rules only apply to documentation files
   - Other parts of codebase unaffected
   - Keeps context focused and relevant

### Rule Priority

When multiple rules could apply:

1. **Most specific wins:**
   - `mintlify_technical_writing.mdc` (specific to `.mdx`)
   - Takes precedence over general workspace rules

2. **Workspace rules:**
   - `agent_context.mdc` (workspace navigation)
   - `business_overview.mdc` (business context)
   - Always available as background context

---

## 🎨 Comparison: MCP vs Cursor Rules

### Why Not MCP?

Mintlify **doesn't provide an official MCP server**. Their recommended approach is **Cursor Project Rules**.

### Cursor Rules Advantages

| Feature | Cursor Rules | MCP Server |
|---------|--------------|------------|
| **Setup** | ✅ File-based, auto-loads | ⚠️ Requires server setup |
| **Sharing** | ✅ Git-versioned, team-wide | ⚠️ Per-machine config |
| **Context** | ✅ File-scoped, automatic | ⚠️ Manual invocation |
| **Examples** | ✅ Full code examples in rule | ⚠️ Separate docs |
| **Updates** | ✅ Git pull = updated rules | ⚠️ Manual updates |
| **Mintlify Support** | ✅ Officially recommended | ❌ Not available |

### What We've Built

✅ **Cursor Project Rules** (following Mintlify's recommendation)
- File in `.cursor/rules/mintlify_technical_writing.mdc`
- Auto-applies to all `.mdx` files
- Contains complete component reference
- Shared via Git with team

❌ **MCP Server** (not needed)
- Mintlify doesn't provide one
- Rules-based approach is sufficient
- More maintainable for team

---

## 🚀 Using the Setup

### Creating a New Page

**AI Agent workflow:**

1. User says: "Create a page about patient uploads"

2. Cursor automatically loads `mintlify_technical_writing.mdc`

3. Agent follows standards:
   - Checks if large text needed → uses `/georgian-text`
   - Creates MDX file with proper structure
   - No duplicate H1
   - Georgian content
   - Proper components

4. Updates `mint.json` navigation

5. Deploys with `required_permissions: ["all"]`

**Human workflow:**

1. Open Cursor in docs folder

2. Create new `.mdx` file
   - Rule auto-loads
   - Cursor suggests Mintlify components

3. Write content
   - Cursor helps with Georgian patterns
   - Warns about duplicate H1
   - Suggests appropriate components

4. Update `mint.json`

5. Commit and push
   - Auto-deploys to Mintlify

### Generating Georgian Content

**Command:** `/georgian-text`

**Behind the scenes:**
```bash
cd /Users/brair/Documents/CodeBase/Medspace/Radium/RadiumProjects/Tools/GeorgianTextGenerator
source venv/bin/activate
venv/bin/python scripts/generate_docs.py \
  --topic "User's topic" \
  --type explanation \
  --length medium \
  --output /tmp/content.md
```

### Creating Video Tutorials

**Two-stage workflow (from rule):**

```bash
# Stage 1: Generate script
cd /Users/brair/Documents/CodeBase/Medspace/Radium/Scripts/VideoDocs
source .venv/bin/activate
./generate_script_only.sh VIDEO.mov ka VOICE_ID eleven_v3 1.0

# Stage 2: Review, edit, continue
# Edit: VIDEO_script_ka.json
./resume_workflow.sh VIDEO_script_ka.json VIDEO.mov ka VOICE_ID eleven_v3 1.0 yes "Title"
```

---

## 🔍 Verification

### How to Verify Setup is Working

**For AI Agents:**

1. Open any `.mdx` file in `docs/`
2. Check that `mintlify_technical_writing.mdc` is loaded
3. Verify Georgian content patterns recognized
4. Confirm component suggestions appear

**For Humans:**

1. Open Cursor in `docs/` folder
2. Create new `.mdx` file
3. Start typing `<` - should see Mintlify components
4. Write in Georgian - should get contextual help

**Test command:**

Open Cursor command palette:
- Type `/mintlify-docs` - should appear
- Type `/georgian-text` - should appear

---

## 📋 Maintenance

### Updating the Rules

**When to update:**
- New Mintlify components released
- Documentation workflow changes
- New best practices discovered
- Common mistakes patterns identified

**How to update:**

1. Edit `.cursor/rules/mintlify_technical_writing.mdc`
2. Add examples and explanations
3. Update version date in rule
4. Commit and push
5. All team members get update automatically

**Update checklist:**
- [ ] Rule file updated
- [ ] Examples tested
- [ ] Documentation index updated
- [ ] Changelog entry added
- [ ] Team notified

### Keeping in Sync with Mintlify

**Monitor:**
- [Mintlify Changelog](https://mintlify.com/changelog)
- [Mintlify Docs](https://mintlify.com/docs)
- [Mintlify Cursor Guide](https://www.mintlify.com/docs/guides/cursor)

**When Mintlify updates:**
1. Review changes
2. Update rule file if needed
3. Test with existing content
4. Update examples
5. Deploy updates

---

## 🎓 Best Practices

### For Rule Maintenance

1. **Keep examples current:**
   - Test all code examples in rule file
   - Update when Mintlify API changes
   - Add new components as released

2. **Document common mistakes:**
   - Add "don't do this" examples
   - Explain why mistakes happen
   - Provide clear alternatives

3. **Keep structure logical:**
   - Group related components
   - Use clear section headers
   - Provide quick reference tables

### For Team Collaboration

1. **Share updates:**
   - Announce rule updates in team chat
   - Explain major changes
   - Provide migration guides if needed

2. **Gather feedback:**
   - Ask team about pain points
   - Add solutions to rule file
   - Iterate based on real usage

3. **Version control:**
   - Use meaningful commit messages
   - Tag major rule updates
   - Keep changelog updated

---

## 🔗 Related Resources

### Internal Documentation
- [DOCUMENTATION_INDEX.md](./DOCUMENTATION_INDEX.md) - Navigation guide
- [PAGE_CREATION_STANDARDS.md](./PAGE_CREATION_STANDARDS.md) - Structure standards
- [MINTLIFY_OVERVIEW.md](./MINTLIFY_OVERVIEW.md) - Progress tracking

### Cursor Rules Files
- [mintlify_technical_writing.mdc](../.cursor/rules/mintlify_technical_writing.mdc) - Main rule
- [docs_workflow.mdc](../.cursor/rules/docs_workflow.mdc) - Quick reference

### External Resources
- [Mintlify Cursor Guide](https://www.mintlify.com/docs/guides/cursor) - Official guide
- [Cursor Rules Docs](https://docs.cursor.com/context/rules-for-ai) - Cursor documentation
- [Mintlify Docs](https://mintlify.com/docs) - Component reference

---

## ✅ Summary

### What We Have

✅ **Cursor Project Rules** (`.cursor/rules/mintlify_technical_writing.mdc`)
- Auto-loads for all `.mdx` files
- Contains complete Mintlify standards
- Georgian language requirements
- Full component reference with examples

✅ **Documentation Index** (`DOCUMENTATION_INDEX.md`)
- Single navigation source
- Quick decision trees
- Tool references

✅ **Cursor Commands** (`/mintlify-docs`, `/georgian-text`)
- Quick access to workflows
- Integrated tool execution

### What We Don't Have (and Don't Need)

❌ **MCP Server** - Not provided by Mintlify
- Cursor rules are the recommended approach
- More maintainable and team-friendly

### Result

🎉 **Complete Mintlify + Cursor integration following official best practices**

- ✅ AI agents automatically follow standards
- ✅ Team has consistent workflow
- ✅ Git-versioned rules stay in sync
- ✅ Easy to maintain and update

---

**Ready to create amazing documentation!** 📚✨

