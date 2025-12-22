# 📚 HealthTech Documentation - Complete Index

**Last Updated:** December 23, 2025  
**Live Site:** https://radium-98210c26.mintlify.app/  
**Repository:** https://github.com/brizhamadze/docs

---

## 🗺️ Navigation for AI Agents

### Start Here (Priority Order)

1. **[Mintlify Technical Writing Rule](./.cursor/rules/mintlify_technical_writing.mdc)** ⭐ **READ FIRST**
   - Complete Mintlify standards
   - Georgian language requirements
   - Component reference with examples
   - Video tutorial workflow
   - Common mistakes to avoid

2. **[Documentation Workflow](./.cursor/rules/docs_workflow.mdc)**
   - Quick reference rules
   - Deployment requirements
   - Video generation workflow

3. **[Page Creation Standards](./PAGE_CREATION_STANDARDS.md)**
   - No duplicate H1 rule
   - Tone guidelines
   - Common mistakes checklist

4. **[Mintlify Overview](./MINTLIFY_OVERVIEW.md)**
   - Visual structure
   - Progress tracking
   - Priority matrix

---

## 📂 Project Structure

```
docs/
├── .cursor/
│   └── rules/
│       ├── mintlify_technical_writing.mdc  ⭐ PRIMARY RULE
│       └── docs_workflow.mdc               (Quick reference)
│
├── DOCUMENTATION_INDEX.md                  ⭐ THIS FILE
├── PAGE_CREATION_STANDARDS.md             (Tone & structure)
├── MINTLIFY_OVERVIEW.md                   (Progress tracking)
├── mint.json                              (Navigation config)
├── index.mdx                              (Landing page)
│
├── getting-started/                        📚 Core docs
├── search/
├── space-management/
├── patients-files/
├── dicom-viewer/
├── sharing/
├── workflows/
├── ai-chat/
├── blog/
│
├── tutorials/                              🎥 Video tutorials
├── images/                                 🖼️ Static assets
└── videos/                                 🎬 Video files
```

---

## 🎯 Quick Decision Tree for AI Agents

### User wants to create new page?

**Step 1: Determine page type**
- Text documentation? → Go to Step 2
- Video tutorial? → Go to **Video Tutorial Workflow**

**Step 2: Generate Georgian content (if needed)**

For large text sections (300+ words):
```bash
cd /Users/brair/Documents/CodeBase/Medspace/Radium/RadiumProjects/Tools/GeorgianTextGenerator
source venv/bin/activate
venv/bin/python scripts/generate_docs.py \
  --topic "Your Topic" \
  --type explanation \
  --length medium \
  --output /tmp/content.md
```

**Step 3: Create MDX file**

Location: `docs/[section]/[page-name].mdx`

Required structure:
```mdx
---
title: 'Page Title in Georgian'
description: 'Brief description in Georgian'
---

[Content starts here - NO duplicate h1]

## First Section

...
```

**Step 4: Update navigation**

Edit `mint.json` and add page to appropriate group:
```json
{
  "group": "Group Name",
  "pages": [
    "section/existing-page",
    "section/new-page"  // Add here
  ]
}
```

**Step 5: Deploy**
```bash
cd /Users/brair/Documents/CodeBase/Medspace/Radium/RadiumProjects/Tutorials/docs
git add .
git commit -m "docs: add [description]"
git push  # Use required_permissions: ["all"] if via AI
```

---

## 🎥 Video Tutorial Workflow

### Two-Stage Workflow (RECOMMENDED)

**Stage 1: Generate Script**
```bash
cd /Users/brair/Documents/CodeBase/Medspace/Radium/Scripts/VideoDocs
source .venv/bin/activate
./generate_script_only.sh VIDEO.mov ka VOICE_ID eleven_v3 1.0
```

**Stage 2: Review → Edit → Continue**
1. Review `VIDEO_script_ka.json`
2. Edit narration, timestamps, descriptions
3. Continue:
```bash
./resume_workflow.sh VIDEO_script_ka.json VIDEO.mov ka VOICE_ID eleven_v3 1.0 yes "ტუტორიალის სახელი"
```

⚠️ **CRITICAL:** Use `resume_workflow.sh` (NOT `full_workflow.sh`) after edits!

**Verification Checklist:**
- [ ] Narration is in Georgian
- [ ] Description is in Georgian
- [ ] Video embedded correctly
- [ ] Navigation updated in `mint.json`
- [ ] No large silence gaps
- [ ] Overlapping segments resolved

---

## 📋 Mintlify Component Quick Reference

### Callouts
```mdx
<Note>დამატებითი ინფორმაცია</Note>
<Tip>სასარგებლო რჩევა</Tip>
<Warning>გაფრთხილება</Warning>
<Info>ინფორმაცია</Info>
<Check>წარმატება</Check>
```

### Steps
```mdx
<Steps>
  <Step title="ნაბიჯი 1">
    აღწერა
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

### Images & Videos
```mdx
<Frame>
  <img src="/images/path.png" alt="აღწერა" />
</Frame>

<Frame>
  <video controls>
    <source src="/videos/tutorial.mp4" type="video/mp4" />
  </video>
</Frame>
```

### Tabs
```mdx
<Tabs>
  <Tab title="ვარიანტი 1">
    შინაარსი
  </Tab>
</Tabs>
```

### Accordions
```mdx
<AccordionGroup>
  <Accordion title="შეკითხვა">
    პასუხი
  </Accordion>
</AccordionGroup>
```

---

## 🔴 Critical Rules Summary

### 1. Language
- ✅ ALL content must be in Georgian (ka)
- ✅ Keep technical terms in English (Space, DICOM, AI)
- ✅ Filenames in English
- ❌ No English in page content

### 2. Page Structure
- ❌ **NO duplicate H1** - frontmatter `title` creates it automatically
- ✅ Start directly with content or use `##`
- ✅ Always include frontmatter with `title` and `description`

### 3. Components
- ✅ ALWAYS wrap images in `<Frame>` tags
- ✅ Provide alt text in Georgian for all images
- ✅ Use appropriate callouts (`<Note>`, `<Warning>`, etc.)

### 4. Navigation
- ✅ ALWAYS update `mint.json` when adding pages
- ✅ Use descriptive group names in Georgian
- ✅ Use appropriate icons for groups

### 5. Video Tutorials
- ✅ Narration MUST be in Georgian when `language: ka`
- ✅ Use two-stage workflow for quality control
- ✅ Always use `resume_workflow.sh` after manual edits
- ❌ Don't use `full_workflow.sh` after editing scripts

### 6. Deployment
- ✅ Use `required_permissions: ["all"]` for git push via AI
- ✅ Push to `main` branch triggers auto-deployment
- ✅ Write descriptive commit messages

---

## 🛠️ Tools Reference

### Georgian Text Generator
**Location:** `/Users/brair/Documents/CodeBase/Medspace/Radium/RadiumProjects/Tools/GeorgianTextGenerator/`

**Usage:**
```bash
cd /Users/brair/Documents/CodeBase/Medspace/Radium/RadiumProjects/Tools/GeorgianTextGenerator
source venv/bin/activate

# Generate explanation
venv/bin/python scripts/generate_docs.py \
  --topic "Your Topic" \
  --type explanation \
  --length medium \
  --output /tmp/content.md

# Custom prompt
venv/bin/python scripts/generate_docs.py \
  --custom-prompt "Your detailed prompt" \
  --output /tmp/content.md
```

**Cursor Command:** `/georgian-text`

### Video Documentation Scripts
**Location:** `/Users/brair/Documents/CodeBase/Medspace/Radium/Scripts/VideoDocs/`

**Key Scripts:**
- `generate_script_only.sh` - Generate narration script
- `resume_workflow.sh` - Continue after editing script
- `full_workflow.sh` - Complete automated workflow (no review)

**Environment:**
```bash
source .venv/bin/activate
export $(cat ../../.env | xargs)  # Load API keys
```

---

## 📊 Current Status

### Documentation Site
- **Live URL:** https://radium-98210c26.mintlify.app/
- **Platform:** Mintlify
- **Language:** Georgian (ka)
- **Auto-Deploy:** Push to `main` branch

### Navigation Groups (mint.json)
1. 🚀 დაწყება და ინტერფეისი
2. 🔍 ძიება და შედარება
3. 👥 სფეისის მართვა
4. 📁 პაციენტები და ფაილები
5. ❤️ DICOM მნახველი
6. 🔗 გაზიარება და კომუნიკაცია
7. ⚡ AI Workflow-ები
8. 🤖 AI ჩატი
9. 📰 ბლოგი

### Recent Updates
- ✅ Created comprehensive Mintlify technical writing rule
- ✅ Integrated Georgian language requirements
- ✅ Added complete component reference
- ✅ Documented video tutorial workflow
- ✅ Created this documentation index

---

## 🔗 External Resources

### Official Documentation
- [Mintlify Docs](https://mintlify.com/docs) - Official Mintlify documentation
- [Mintlify Cursor Guide](https://www.mintlify.com/docs/guides/cursor) - Cursor integration
- [MDX Guide](https://mdxjs.com/) - MDX syntax reference
- [docs.json Schema](https://mintlify.com/docs.json) - Navigation configuration schema

### Repository & Live Site
- [GitHub Repository](https://github.com/brizhamadze/docs) - Source code
- [Live Documentation Site](https://radium-98210c26.mintlify.app/) - Published docs

---

## 🎓 Learning Path for New Contributors

### For AI Agents
1. Read **Mintlify Technical Writing Rule** (`.cursor/rules/mintlify_technical_writing.mdc`)
2. Review **Page Creation Standards** (`PAGE_CREATION_STANDARDS.md`)
3. Check **Quick Decision Tree** (this file, above)
4. Follow **Component Quick Reference** (this file, above)
5. Review examples in existing pages

### For Human Contributors
1. Read **Mintlify Overview** (`MINTLIFY_OVERVIEW.md`)
2. Review **Page Creation Standards** (`PAGE_CREATION_STANDARDS.md`)
3. Check existing pages for examples
4. Follow Georgian language requirements
5. Test locally with `mint dev` before pushing

---

## 📞 Support & Contacts

### Repository
- **Owner:** brizhamadze
- **Repository:** https://github.com/brizhamadze/docs

### Company
- **Name:** Radium
- **Domains:** radium.ge (company), healthtech.dev (portal)
- **Business:** Cloud PACS, AI Radiology, Medical Imaging

---

## 🔄 Version History

### v2.0 - December 23, 2025
- ✅ Created comprehensive Mintlify technical writing rule
- ✅ Integrated Georgian text generation workflow
- ✅ Added complete component reference
- ✅ Created documentation index (this file)

### v1.0 - December 1, 2025
- ✅ Initial structure setup
- ✅ Navigation reorganization
- ✅ Video tutorial workflow

---

## 📝 Notes for Maintainers

### When Adding New Features
1. Update Mintlify technical writing rule if new components
2. Update this index if new tools/workflows
3. Update navigation groups in `mint.json`
4. Create placeholder pages if content not ready

### When Updating Workflow
1. Update `.cursor/rules/mintlify_technical_writing.mdc` (primary)
2. Update `.cursor/rules/docs_workflow.mdc` (quick reference)
3. Update this index
4. Update relevant README files in tool folders

### Quality Assurance
- Always test video workflow before documenting changes
- Verify generated Georgian text quality
- Check navigation rendering on live site
- Ensure all links work correctly

---

**This index serves as the single source of truth for navigating the HealthTech documentation project.** 🎯

