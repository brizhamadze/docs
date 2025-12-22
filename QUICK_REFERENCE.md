# ⚡ Mintlify Documentation - Quick Reference Card

**Keep this open while working!**

---

## 🎯 Start Here

**Complete standards:** [.cursor/rules/mintlify_technical_writing.mdc](./.cursor/rules/mintlify_technical_writing.mdc) ⭐ (auto-loads)  
**Navigation guide:** [DOCUMENTATION_INDEX.md](./DOCUMENTATION_INDEX.md)  
**Setup explanation:** [MINTLIFY_CURSOR_SETUP.md](./MINTLIFY_CURSOR_SETUP.md)

---

## 🚨 Critical Rules

### 1. No Duplicate H1
```mdx
❌ WRONG:
---
title: 'სათაური'
---
# სათაური  ← DON'T DO THIS

✅ CORRECT:
---
title: 'სათაური'
---
Content starts here...
```

### 2. Georgian Language
- ✅ ALL content in Georgian
- ✅ Technical terms in English (Space, DICOM, AI)
- ✅ Filenames in English

### 3. Wrap Images
```mdx
❌ WRONG: ![alt](/path.png)

✅ CORRECT:
<Frame>
  <img src="/path.png" alt="Georgian alt text" />
</Frame>
```

### 4. Update Navigation
After creating page, edit `mint.json`:
```json
{
  "group": "Group Name",
  "pages": ["section/new-page"]
}
```

---

## 📋 Component Cheat Sheet

### Callouts
```mdx
<Note>შენიშვნა</Note>
<Tip>რჩევა</Tip>
<Warning>გაფრთხილება</Warning>
<Info>ინფორმაცია</Info>
<Check>წარმატება</Check>
```

### Steps
```mdx
<Steps>
  <Step title="ნაბიჯი 1">Content</Step>
  <Step title="ნაბიჯი 2">Content</Step>
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

### Media
```mdx
<Frame>
  <img src="/images/path.png" alt="აღწერა" />
</Frame>

<Frame>
  <video controls>
    <source src="/videos/file.mp4" type="video/mp4" />
  </video>
</Frame>
```

---

## 🎥 Video Tutorial Workflow

```bash
# 1. Generate script only
cd /Users/brair/Documents/CodeBase/Medspace/Radium/Scripts/VideoDocs
source .venv/bin/activate
./generate_script_only.sh VIDEO.mov ka VOICE_ID eleven_v3 1.0

# 2. Review & edit: VIDEO_script_ka.json

# 3. Resume workflow
./resume_workflow.sh VIDEO_script_ka.json VIDEO.mov ka VOICE_ID eleven_v3 1.0 yes "Title"
```

⚠️ Use `resume_workflow.sh` after edits, NOT `full_workflow.sh`

---

## 🇬🇪 Georgian Text Generation

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

```bash
cd /Users/brair/Documents/CodeBase/Medspace/Radium/RadiumProjects/Tutorials/docs
git add .
git commit -m "docs: description"
git push  # Use required_permissions: ["all"] if via AI
```

---

## ✅ Pre-Deploy Checklist

- [ ] All content in Georgian
- [ ] No duplicate H1
- [ ] Images wrapped in `<Frame>`
- [ ] Navigation updated in `mint.json`
- [ ] Alt text in Georgian
- [ ] Frontmatter has title & description

---

## 📁 Key Paths

| What | Path |
|------|------|
| Docs root | `/Users/brair/Documents/CodeBase/Medspace/Radium/RadiumProjects/Tutorials/docs/` |
| Main rule | `.cursor/rules/mintlify_technical_writing.mdc` |
| Navigation | `mint.json` |
| Images | `/images/` |
| Videos | `/videos/` |
| Video scripts | `/Users/brair/Documents/CodeBase/Medspace/Radium/Scripts/VideoDocs/` |
| Georgian generator | `/Users/brair/Documents/CodeBase/Medspace/Radium/RadiumProjects/Tools/GeorgianTextGenerator/` |

---

## 🔗 Quick Links

- **Live site:** https://radium-98210c26.mintlify.app/
- **Repo:** https://github.com/brizhamadze/docs
- **Mintlify docs:** https://mintlify.com/docs

---

## 🎯 Decision Tree

```
User wants to...
│
├─ Create text page?
│  ├─ Large content (300+ words)? → Use /georgian-text
│  ├─ Create MDX with frontmatter
│  ├─ NO duplicate H1
│  ├─ Update mint.json
│  └─ Deploy
│
├─ Create video tutorial?
│  ├─ Generate script only
│  ├─ Review & edit
│  ├─ Resume workflow
│  └─ Auto-deploys
│
└─ Update existing page?
   ├─ Read file first
   ├─ Check for duplicate H1
   ├─ Ensure Georgian content
   └─ Deploy
```

---

**Print this or keep it open in a separate tab!** 📌

