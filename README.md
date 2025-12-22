# 📚 HealthTech Documentation (Mintlify)

**Live Site:** https://radium-98210c26.mintlify.app/  
**Repository:** https://github.com/brizhamadze/docs  
**Language:** Georgian (ka)  
**Platform:** Mintlify

---

## 🚀 Quick Start

### For AI Agents

**Just start working!** The Cursor rule auto-loads for all `.mdx` files.

1. **Read first:** [.cursor/rules/mintlify_technical_writing.mdc](../.cursor/rules/mintlify_technical_writing.mdc) ⭐
2. **Quick reference:** [QUICK_REFERENCE.md](./QUICK_REFERENCE.md)
3. **Navigation:** [DOCUMENTATION_INDEX.md](./DOCUMENTATION_INDEX.md)

### For Humans

1. **Open Cursor** in this folder
2. **Create/edit** `.mdx` files (rule auto-loads)
3. **Use commands:** `/mintlify-docs` or `/georgian-text`
4. **Deploy:** `git push` (auto-deploys to Mintlify)

---

## 📂 Documentation Structure

```
docs/
├── 📖 Documentation Files
│   ├── README.md                        ⭐ This file (start here)
│   ├── DOCUMENTATION_INDEX.md           Complete navigation guide
│   ├── QUICK_REFERENCE.md              Cheat sheet
│   ├── MINTLIFY_CURSOR_SETUP.md        Integration explanation
│   ├── CURSOR_INTEGRATION_COMPLETE.md  Completion summary
│   ├── PAGE_CREATION_STANDARDS.md       Structure guidelines
│   └── MINTLIFY_OVERVIEW.md            Progress tracking
│
├── ⚙️ Configuration
│   ├── mint.json                        Navigation config
│   ├── custom.css                       Custom styles
│   └── index.mdx                        Landing page
│
├── 📁 Content Sections
│   ├── getting-started/                 Introduction & basics
│   ├── search/                          Search functionality
│   ├── space-management/                Space management
│   ├── patients-files/                  Patient management
│   ├── dicom-viewer/                    DICOM viewing
│   ├── sharing/                         Sharing features
│   ├── workflows/                       AI workflows
│   ├── ai-chat/                         AI chat features
│   ├── blog/                            Blog posts
│   └── tutorials/                       Video tutorials
│
└── 🎨 Assets
    ├── images/                          Screenshots, logos
    ├── videos/                          Tutorial videos
    └── logo/                            Site logos
```

---

## 🎯 Cursor Integration (Auto-Loading)

### How It Works

**When you open any `.mdx` file:**

```
Open file.mdx
    ↓
Cursor detects file pattern
    ↓
Auto-loads: mintlify_technical_writing.mdc
    ↓
Full context available:
- Mintlify components
- Georgian requirements
- Page structure rules
- Video workflow
- Deployment process
    ↓
Start working with full assistance!
```

### What You Get

✅ **Automatic Context**
- Complete Mintlify standards
- All component examples
- Georgian language patterns
- Common mistake prevention

✅ **IDE Assistance**
- Component autocomplete
- Pattern suggestions
- Lint warnings
- Example references

✅ **Integrated Workflows**
- Georgian text generation
- Video tutorial creation
- Deployment automation

---

## 🔴 Critical Rules

### 1. No Duplicate H1 Heading

```mdx
❌ WRONG:
---
title: 'სათაური'
---
# სათაური  ← Mintlify creates this automatically

✅ CORRECT:
---
title: 'სათაური'
---
Content starts here...
```

### 2. ALL Content in Georgian

- ✅ Titles, headings, paragraphs in Georgian
- ✅ Technical terms in English (Space, DICOM, AI)
- ✅ Filenames in English

### 3. Always Wrap Images

```mdx
<Frame>
  <img src="/images/path.png" alt="Georgian description" />
</Frame>
```

### 4. Update Navigation

After creating a page, edit `mint.json`:
```json
{
  "group": "Group Name",
  "pages": ["section/new-page"]
}
```

---

## 📋 Most Common Components

### Callouts
```mdx
<Note>დამატებითი ინფორმაცია</Note>
<Tip>სასარგებლო რჩევა</Tip>
<Warning>მნიშვნელოვანი გაფრთხილება</Warning>
```

### Steps
```mdx
<Steps>
  <Step title="პირველი ნაბიჯი">
    აღწერა და დეტალები
  </Step>
</Steps>
```

### Cards
```mdx
<CardGroup cols={2}>
  <Card title="სათაური" icon="rocket" href="/path">
    აღწერა
  </Card>
</CardGroup>
```

**See complete reference:** [.cursor/rules/mintlify_technical_writing.mdc](../.cursor/rules/mintlify_technical_writing.mdc)

---

## 🎥 Video Tutorial Workflow

### Two-Stage Process (Recommended)

```bash
# Stage 1: Generate script
cd /Users/brair/Documents/CodeBase/Medspace/Radium/Scripts/VideoDocs
source .venv/bin/activate
./generate_script_only.sh VIDEO.mov ka VOICE_ID eleven_v3 1.0

# Stage 2: Review, edit VIDEO_script_ka.json, then:
./resume_workflow.sh VIDEO_script_ka.json VIDEO.mov ka VOICE_ID eleven_v3 1.0 yes "Title"
```

**Checklist:**
- [ ] Narration in Georgian
- [ ] Description in Georgian
- [ ] No large silence gaps
- [ ] Navigation updated

---

## 🇬🇪 Georgian Text Generation

### When to Use

Use for large text sections (300+ words):
- Explanations
- Comprehensive guides
- Tutorial introductions
- Feature descriptions

### How to Use

```bash
cd /Users/brair/Documents/CodeBase/Medspace/Radium/RadiumProjects/Tools/GeorgianTextGenerator
source venv/bin/activate
venv/bin/python scripts/generate_docs.py \
  --topic "Your Topic" \
  --type explanation \
  --length medium \
  --output /tmp/content.md
```

Or use Cursor command: `/georgian-text`

---

## 🚀 Deployment

### Push to Deploy

```bash
# Navigate to docs directory (where .git is located)
cd /Users/brair/Documents/CodeBase/Medspace/Radium/RadiumProjects/Tutorials/docs

git add .
git commit -m "docs: description of changes"
git push  # Use required_permissions: ["all"] if via AI
```

**Auto-deploys to:** https://radium-98210c26.mintlify.app/

### Pre-Deploy Checklist

- [ ] All content in Georgian
- [ ] No duplicate H1
- [ ] Images wrapped in `<Frame>`
- [ ] Alt text in Georgian
- [ ] Navigation updated in `mint.json`
- [ ] Frontmatter has title & description

---

## 📚 Documentation Files Guide

| File | Purpose | When to Read |
|------|---------|--------------|
| **README.md** | Overview (this file) | First time |
| **[QUICK_REFERENCE.md](./QUICK_REFERENCE.md)** | Cheat sheet | While working |
| **[DOCUMENTATION_INDEX.md](./DOCUMENTATION_INDEX.md)** | Complete guide | When lost |
| **[mintlify_technical_writing.mdc](../.cursor/rules/mintlify_technical_writing.mdc)** | Full standards | Deep dive |
| **[MINTLIFY_CURSOR_SETUP.md](./MINTLIFY_CURSOR_SETUP.md)** | Integration details | Understanding setup |
| **[PAGE_CREATION_STANDARDS.md](./PAGE_CREATION_STANDARDS.md)** | Structure rules | Creating pages |

---

## 🎓 Learning Path

### New to Project?

1. **Read:** This README (5 minutes)
2. **Skim:** [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) (2 minutes)
3. **Review:** [.cursor/rules/mintlify_technical_writing.mdc](../.cursor/rules/mintlify_technical_writing.mdc) (15 minutes)
4. **Practice:** Create a test page
5. **Reference:** Keep [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) open while working

### Need to Create Content?

1. **Text page?** → Use [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) component cheat sheet
2. **Large text?** → Use `/georgian-text` command
3. **Video tutorial?** → Follow video workflow in [QUICK_REFERENCE.md](./QUICK_REFERENCE.md)

### Something Not Working?

1. **Check:** [MINTLIFY_CURSOR_SETUP.md](./MINTLIFY_CURSOR_SETUP.md) - Verification section
2. **Review:** [DOCUMENTATION_INDEX.md](./DOCUMENTATION_INDEX.md) - Troubleshooting
3. **Refer to:** [mintlify_technical_writing.mdc](../.cursor/rules/mintlify_technical_writing.mdc) - Full standards

---

## 🛠️ Tools Integration

### Available Tools

| Tool | Purpose | Location |
|------|---------|----------|
| **GeorgianTextGenerator** | Generate Georgian content | `Tools/GeorgianTextGenerator/` |
| **Video Workflow Scripts** | Process video tutorials | `Scripts/VideoDocs/` |
| **Mintlify CLI** | Local preview | `npm install -g mintlify` |

### Cursor Commands

| Command | What It Does |
|---------|-------------|
| `/mintlify-docs` | Show complete workflow guide |
| `/georgian-text` | Generate Georgian content |

---

## 🔗 Important Links

### Live & Repository
- **Live Site:** https://radium-98210c26.mintlify.app/
- **GitHub Repo:** https://github.com/brizhamadze/docs

### Official Documentation
- **Mintlify Docs:** https://mintlify.com/docs
- **Mintlify Cursor Guide:** https://www.mintlify.com/docs/guides/cursor
- **docs.json Schema:** https://mintlify.com/docs.json

### Internal Documentation
- **Main Rule:** [.cursor/rules/mintlify_technical_writing.mdc](../.cursor/rules/mintlify_technical_writing.mdc)
- **Navigation Guide:** [DOCUMENTATION_INDEX.md](./DOCUMENTATION_INDEX.md)
- **Setup Explanation:** [MINTLIFY_CURSOR_SETUP.md](./MINTLIFY_CURSOR_SETUP.md)

---

## 💡 Tips & Best Practices

### For AI Agents

- ✅ Rule auto-loads - just start working
- ✅ Use `/georgian-text` for large content sections
- ✅ Always use two-stage video workflow
- ✅ Verify navigation updates after creating pages
- ✅ Use `required_permissions: ["all"]` for git push

### For Humans

- ✅ Keep [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) open in separate tab
- ✅ Use `mint dev` for local preview before pushing
- ✅ Test video scripts before final processing
- ✅ Review generated Georgian text for quality
- ✅ Check live site after deployment

### Common Mistakes to Avoid

1. ❌ Adding duplicate H1 heading
2. ❌ Writing content in English
3. ❌ Forgetting to wrap images in `<Frame>`
4. ❌ Not updating `mint.json` navigation
5. ❌ Using `full_workflow.sh` after editing video scripts

---

## 📊 Current Status

### Integration Status
✅ **Complete** - Cursor rules fully integrated  
✅ **Auto-loading** - Rules apply automatically to `.mdx` files  
✅ **Team-ready** - Git-versioned, shared standards  
✅ **Production-ready** - All workflows documented  

### Documentation Coverage
- ✅ Complete Cursor integration
- ✅ Georgian language workflow
- ✅ Video tutorial workflow
- ✅ Component reference
- ✅ Deployment automation
- ✅ Quick reference materials

### Recent Updates
- **2025-12-23:** Complete Cursor + Mintlify integration
- **2025-12-23:** Created comprehensive technical writing rule
- **2025-12-23:** Added Georgian text generation workflow
- **2025-12-23:** Created documentation index and quick reference

---

## 🎉 Ready to Go!

**Everything is set up and ready to use:**

1. ✅ Cursor rules auto-load
2. ✅ Complete component reference
3. ✅ Georgian workflow integrated
4. ✅ Video processing automated
5. ✅ Deployment configured
6. ✅ Quick reference available

**Start creating amazing documentation!** 📚✨

---

## 📞 Support

For questions or issues:
1. Check [DOCUMENTATION_INDEX.md](./DOCUMENTATION_INDEX.md)
2. Review [mintlify_technical_writing.mdc](../.cursor/rules/mintlify_technical_writing.mdc)
3. Contact Radium development team

**Company:** Radium  
**Domains:** radium.ge | healthtech.dev  
**Business:** Cloud PACS, AI Radiology, Medical Imaging

---

**Last Updated:** December 23, 2025  
**Version:** 2.0 - Complete Cursor Integration
