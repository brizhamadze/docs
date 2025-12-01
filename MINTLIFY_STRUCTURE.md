# 📚 HealthTech Mintlify Documentation Structure

**Last Updated:** December 1, 2025

---

## 🗺️ Overall Picture

```
HealthTech Documentation
│
├── 🚀 დაწყება (Getting Started)
│   ├── ✅ introduction.mdx (EXISTS)
│   ├── 🔴 login-dashboard.mdx (NEEDED - High Priority)
│   └── ✅ spaces.mdx (EXISTS)
│
├── 👤 ავტორიზაცია და მომხმარებლები (Auth & Users)
│   ├── 🔴 authorization.mdx (NEEDED - High Priority)
│   ├── 🔴 space-management.mdx (NEEDED - High Priority)
│   ├── 🟡 user-management.mdx (NEEDED - Medium Priority)
│   └── 🟡 permissions.mdx (NEEDED - Content Gap)
│
├── 📁 პაციენტების მართვა (Patient Management)
│   ├── ✅ folders.mdx (EXISTS)
│   ├── 🔴 navigation.mdx (NEEDED - High Priority)
│   ├── ✅ uploading.mdx (EXISTS)
│   └── 🔴 document-actions.mdx (NEEDED - High Priority)
│
├── 🩺 DICOM გამოსახულებები (DICOM Images)
│   ├── 🔴 uploading.mdx (NEEDED - High Priority)
│   ├── 🔴 viewing.mdx (NEEDED - High Priority)
│   ├── 🟡 viewer-tools.mdx (NEEDED - Medium Priority)
│   └── 🟢 advanced-features.mdx (NEEDED - Content Gap)
│
├── 📝 დოკუმენტები და რედაქტირება (Documents & Editing)
│   ├── 🔴 editing-reports.mdx (NEEDED - High Priority)
│   ├── 🔴 quick-notes.mdx (NEEDED - High Priority)
│   └── 🔴 file-upload.mdx (NEEDED - High Priority)
│
├── 🤖 AI ასისტენტი (AI Assistant)
│   ├── 🔴 overview.mdx (NEEDED - High Priority)
│   ├── ✅ chat.mdx (EXISTS)
│   ├── 🟡 voice-commands.mdx (NEEDED - Medium Priority)
│   ├── 🟡 audio-transcription.mdx (NEEDED - Medium Priority)
│   ├── 🟢 workflows.mdx (NEEDED - Advanced)
│   ├── 🟢 custom-prompts.mdx (NEEDED - Content Gap)
│   └── ✅ reporting.mdx (EXISTS)
│
├── 🎥 სხვა ფუნქციები (Other Features)
│   ├── 🟡 video-consultation.mdx (NEEDED - Medium Priority)
│   ├── 🟡 personalization.mdx (NEEDED - Medium Priority)
│   └── 🟢 billing.mdx (NEEDED - Low Priority)
│
├── 📚 ვიდეო გაკვეთილები (Video Tutorials - Navigation)
│   ├── 🔴 overview.mdx (NEEDED - Shows all tutorials)
│   ├── 🔴 beginner.mdx (NEEDED - Beginner path)
│   ├── 🟡 intermediate.mdx (NEEDED - Intermediate path)
│   └── 🟢 advanced.mdx (NEEDED - Advanced path)
│
├── 🎬 დამწყებთათვის (Beginner Video Tutorials)
│   ├── 🔴 login-dashboard.mdx (Tutorial #1 - TOP PRIORITY)
│   ├── 🔴 upload-view-dicom.mdx (Tutorial #2 - HIGH PRIORITY)
│   └── 🔴 edit-documents.mdx (Tutorial #3 - HIGH PRIORITY)
│
├── 🎬 საშუალო დონე (Intermediate Video Tutorials)
│   ├── 🟡 ai-chat-voice.mdx (Tutorial #4)
│   ├── 🟡 settings-personalization.mdx (Tutorial #5)
│   └── 🟡 user-billing-management.mdx (Tutorial #6)
│
├── 🎬 მოწინავე (Advanced Video Tutorials)
│   └── 🟢 ai-workflows.mdx (Tutorial #7)
│
└── 📖 არქივი (Archive - Old Videos)
    ├── ✅ authorization.mdx (EXISTS)
    ├── ✅ upload-dicom.mdx (EXISTS)
    ├── ✅ dicom-ის-გაზიარება.mdx (EXISTS)
    ├── ✅ სივრცის-სურათის-შეცვლა.mdx (EXISTS)
    ├── ✅ მომხმარებლის-სივრცეში-დამატება.mdx (EXISTS)
    └── ✅ თემის-შეცვლა.mdx (EXISTS)
```

---

## 📊 Statistics

### Content Status
- ✅ **Existing Content:** 12 pages
- 🔴 **High Priority (Needed):** 15 pages
- 🟡 **Medium Priority (Needed):** 9 pages
- 🟢 **Low/Advanced (Needed):** 6 pages

**Total Pages:** 42 (12 exist, 30 needed)

### Priority Breakdown
| Priority | Count | % of Total |
|----------|-------|------------|
| ✅ Done | 12 | 29% |
| 🔴 High Priority | 15 | 36% |
| 🟡 Medium Priority | 9 | 21% |
| 🟢 Low/Advanced | 6 | 14% |

---

## 🎯 Recommended Creation Order

### Phase 1: Core Fundamentals (Week 1-2)
**Goal:** Users can log in, upload, and view content

1. 🔴 `getting-started/login-dashboard.mdx`
2. 🔴 `auth/authorization.mdx`
3. 🔴 `patients/navigation.mdx`
4. 🔴 `dicom/uploading.mdx`
5. 🔴 `dicom/viewing.mdx`

**Video Tutorial:** Tutorial #1 (Login & Dashboard)

### Phase 2: Document Management (Week 2-3)
**Goal:** Users can manage documents and files

6. 🔴 `documents/editing-reports.mdx`
7. 🔴 `documents/quick-notes.mdx`
8. 🔴 `documents/file-upload.mdx`
9. 🔴 `patients/document-actions.mdx`

**Video Tutorial:** Tutorial #3 (Edit Documents)

### Phase 3: DICOM Deep Dive (Week 3-4)
**Goal:** Complete DICOM workflow

10. 🔴 **Video Tutorial #2** (Upload & View DICOM) - CREATE FIRST!
11. 🟡 `dicom/viewer-tools.mdx`
12. 🔴 `ai/overview.mdx`

### Phase 4: AI Integration (Week 4-5)
**Goal:** AI features fully documented

13. 🟡 `ai/voice-commands.mdx`
14. 🟡 `ai/audio-transcription.mdx`
15. 🔴 **Video Tutorial #4** (AI Chat & Voice)

### Phase 5: User Management & Settings (Week 5-6)
**Goal:** Admin features and personalization

16. 🟡 `auth/space-management.mdx`
17. 🟡 `auth/user-management.mdx`
18. 🟡 `features/personalization.mdx`
19. 🟡 **Video Tutorial #5** (Settings & Personalization)

### Phase 6: Advanced & Gaps (Week 6+)
**Goal:** Complete documentation

20. 🟢 `ai/workflows.mdx`
21. 🟢 **Video Tutorial #7** (AI Workflows)
22. 🟡 `features/video-consultation.mdx`
23. 🟢 `dicom/advanced-features.mdx`
24. 🟢 `auth/permissions.mdx`
25. 🟢 `ai/custom-prompts.mdx`

---

## 📁 Directory Structure

```
docs/
├── index.mdx (Main landing page)
├── mint.json (Navigation config)
│
├── getting-started/
│   ├── introduction.mdx ✅
│   ├── login-dashboard.mdx 🔴
│   └── spaces.mdx ✅
│
├── auth/
│   ├── authorization.mdx 🔴
│   ├── space-management.mdx 🔴
│   ├── user-management.mdx 🟡
│   └── permissions.mdx 🟡
│
├── patients/
│   ├── folders.mdx ✅
│   ├── navigation.mdx 🔴
│   ├── uploading.mdx ✅
│   └── document-actions.mdx 🔴
│
├── dicom/
│   ├── uploading.mdx 🔴
│   ├── viewing.mdx 🔴
│   ├── viewer-tools.mdx 🟡
│   └── advanced-features.mdx 🟢
│
├── documents/
│   ├── editing-reports.mdx 🔴
│   ├── quick-notes.mdx 🔴
│   └── file-upload.mdx 🔴
│
├── ai/
│   ├── overview.mdx 🔴
│   ├── chat.mdx ✅
│   ├── voice-commands.mdx 🟡
│   ├── audio-transcription.mdx 🟡
│   ├── workflows.mdx 🟢
│   ├── custom-prompts.mdx 🟢
│   └── reporting.mdx ✅
│
├── features/
│   ├── video-consultation.mdx 🟡
│   ├── personalization.mdx 🟡
│   └── billing.mdx 🟢
│
├── tutorials/
│   ├── overview.mdx 🔴
│   ├── beginner.mdx 🔴
│   ├── intermediate.mdx 🟡
│   ├── advanced.mdx 🟢
│   └── [archive]/
│       ├── authorization.mdx ✅
│       ├── upload-dicom.mdx ✅
│       ├── dicom-ის-გაზიარება.mdx ✅
│       ├── სივრცის-სურათის-შეცვლა.mdx ✅
│       ├── მომხმარებლის-სივრცეში-დამატება.mdx ✅
│       └── თემის-შეცვლა.mdx ✅
│
└── video-tutorials/
    ├── login-dashboard.mdx 🔴 (Tutorial #1)
    ├── upload-view-dicom.mdx 🔴 (Tutorial #2)
    ├── edit-documents.mdx 🔴 (Tutorial #3)
    ├── ai-chat-voice.mdx 🟡 (Tutorial #4)
    ├── settings-personalization.mdx 🟡 (Tutorial #5)
    ├── user-billing-management.mdx 🟡 (Tutorial #6)
    └── ai-workflows.mdx 🟢 (Tutorial #7)
```

---

## 🎬 Video Tutorial Mapping

Based on `healthtech_overview_plan.md`:

| # | Title (Georgian) | Title (English) | Priority | Status | MDX File |
|---|-----------------|-----------------|----------|--------|----------|
| 1 | HealthTech-ზე შესვლა და მთავარი დაფის გაცნობა | Login & Dashboard Overview | 🔴 High | 🔴 Not Created | `video-tutorials/login-dashboard.mdx` |
| 2 | DICOM გამოსახულებების ატვირთვა და ნახვა | Upload and View DICOM Images | 🔴 High | 🔴 Not Created | `video-tutorials/upload-view-dicom.mdx` |
| 3 | დოკუმენტების რედაქტირება, შენიშვნების და ფაილების დამატება | Edit Documents, Add Notes and Files | 🔴 High | 🔴 Not Created | `video-tutorials/edit-documents.mdx` |
| 4 | AI Chat-ის გამოყენება და ხმოვანი ბრძანებები | Using AI Chat and Voice Commands | 🟡 Medium | 🔴 Not Created | `video-tutorials/ai-chat-voice.mdx` |
| 5 | სისტემის პარამეტრები და პერსონალიზაცია | System Settings and Personalization | 🟡 Medium | 🔴 Not Created | `video-tutorials/settings-personalization.mdx` |
| 6 | მომხმარებლების და ბილინგის მართვა | User & Billing Management | 🟡 Medium | 🔴 Not Created | `video-tutorials/user-billing-management.mdx` |
| 7 | AI Workflow-ების ინსტალაცია და მართვა | Install and Manage AI Workflows | 🟢 Advanced | 🔴 Not Created | `video-tutorials/ai-workflows.mdx` |

---

## 🔄 Workflow Integration

### Creating New Tutorial Content

1. **Record Video**
   ```bash
   # Record tutorial following the plan
   ```

2. **Process Video**
   ```bash
   cd /Users/brair/Documents/CodeBase/Medspace/Radium/Scripts/VideoDocs
   source .venv/bin/activate
   export $(cat .env | xargs)
   ./full_workflow.sh video.mov ka BIvP0GN1cAtSRTxNHnWS eleven_v3 1.0 yes "Tutorial Title"
   ```

3. **Auto-publishes to Mintlify**
   - Video gets uploaded
   - Navigation gets updated
   - Page created in `tutorials/` or `video-tutorials/`

---

## 🎨 Navigation Theme

The new structure uses emojis for better visual hierarchy:
- 🚀 Getting Started
- 👤 Auth & Users
- 📁 Patient Management
- 🩺 DICOM Images
- 📝 Documents & Editing
- 🤖 AI Assistant
- 🎥 Other Features
- 📚 Tutorial Navigation
- 🎬 Video Tutorials (by level)
- 📖 Archive

---

## 📝 Next Actions

### Immediate (Today)
1. ✅ Update `mint.json` (DONE)
2. 🔴 Create placeholder files for missing content
3. 🔴 Review new structure on Mintlify preview

### This Week
1. 🔴 Create Tutorial #1: Login & Dashboard
2. 🔴 Create Tutorial #2: Upload & View DICOM
3. 🔴 Create Tutorial #3: Edit Documents

### Next Week
1. 🔴 Fill in high-priority text documentation
2. 🟡 Create intermediate tutorials
3. 🟡 Add medium-priority content

---

## 🚀 Publishing

After updating `mint.json`, push to deploy:

```bash
cd /Users/brair/Documents/CodeBase/Medspace/Radium/RadiumProjects/Tutorials/docs
git add mint.json
git commit -m "docs: update navigation structure based on tutorial plan"
git push
```

**Note:** Use `required_permissions: ["all"]` when pushing via AI agent.

---

*This structure is based on the tutorial master plan generated from your overview video analysis.*

