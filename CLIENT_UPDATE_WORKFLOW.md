# Client Update Workflow - Mintlify Documentation

## Overview
This document outlines the process for adding or updating client success stories on the Radium HealthTech Mintlify documentation site.

## Prerequisites
- Access to the docs repository at `Radium/RadiumProjects/Tutorials/docs`
- Client information (name, services, statistics)
- Research completed on the client

## Steps to Add a New Client

### 1. Research the Client
Use web search to gather information about the hospital/clinic:

```bash
# Search for general information
Google: "[Hospital Name] Georgia"
Google: "[Hospital Name] medical center Tbilisi"
```

**Collect:**
- ✅ Full name and location
- ✅ Year founded (if available)
- ✅ Specialties and services offered
- ✅ Size (staff, patients per year)
- ✅ Unique approach or philosophy

### 2. Gather Usage Statistics
From internal systems, collect:
- ✅ Number of studies stored
- ✅ Modalities in use (CT, X-Ray, MRI, Ultrasound, Mammography, etc.)
- ✅ Number of users
- ✅ Years using the service
- ✅ Specific use cases or workflows

### 3. Add Client Logo/Image (Optional but Recommended)

If you have a custom logo or branded image for the client:

**Step 1:** Copy the image to the docs images folder:
```bash
# Create clients folder if it doesn't exist
mkdir -p Radium/RadiumProjects/Tutorials/docs/images/clients

# Copy client logo (use PNG with transparent background if possible)
cp /path/to/client-logo.png Radium/RadiumProjects/Tutorials/docs/images/clients/client-name-logo.png
```

**Naming Convention:** `[client-name]-logo.png` (e.g., `medulla-logo.png`)

**Image Guidelines:**
- ✅ Prefer PNG with transparent background
- ✅ Optimize file size (keep under 500KB)
- ✅ Use descriptive names matching the client filename
- ✅ Aspect ratio: 16:9 or similar for header images

### 4. Create the Client Page

**Location:** `Radium/RadiumProjects/Tutorials/docs/clients/[client-name].mdx`

**Filename Convention:** Use lowercase with hyphens (e.g., `consilium-medulla.mdx`)

**Template Structure (KEEP IT SIMPLE!):**

```mdx
---
title: '[Hospital Name in Georgian]'
description: '[One-line description in Georgian]'
---

<Frame>
  <img src="/images/clients/[client-name]-logo.png" alt="[Client Name]" />
</Frame>

## კლიენტის შესახებ

[Brief paragraph about the hospital based on Google search - IN GEORGIAN. Include: location, specialties, unique approach, years of experience. End with: "Radium-ის Cloud PACS პლატფორმა უზრუნველყოფს კლინიკის სრული რადიოლოგიური ინფრასტრუქტურის მართვას."]

## სტატისტიკა

<CardGroup cols={2}>
  <Card title="[X,XXX+]" icon="database">
    **სულ კვლევა**
  </Card>
  <Card title="[X] მოწყობილობა" icon="microscope">
    **დაკავშირებული**
  </Card>
  <Card title="[XX+] ექიმი" icon="user-doctor">
    **იყენებს სისტემას**
  </Card>
  <Card title="[List modalities]" icon="hospital">
    **მოდალითები**
  </Card>
</CardGroup>
```

**That's it! Keep it simple and clean.**

### Required Information for Each Client:

**Statistics to Collect:**
1. **Total Studies** - Total number of studies stored in Cloud PACS
2. **Number of Devices** - How many imaging devices connected
3. **Number of Doctors** - Doctors actively using the system
4. **Modalities List** - Comma-separated list (e.g., "CT, X-Ray, MRI, Ultrasound")

**Hospital Information (from Google search):**
- Full name and location
- Main specialties
- Years of experience (if available)
- Unique approach or philosophy
- Type of facility (hospital, clinic, diagnostic center)

### 5. Update Navigation (mint.json)

Add the new client to the "წარმატების ისტორიები" section:

```json
{
  "group": "წარმატების ისტორიები",
  "pages": [
    "clients/tbilisi-heart-center",
    "clients/med-diagnostics",
    "clients/chaphidze-hospital",
    "clients/ghia-guli",
    "clients/consilium-medulla"  // ADD NEW CLIENT HERE
  ]
}
```

### 6. Update Client Index Page

Add a card to `clients/index.mdx` in the `<CardGroup>` section:

```mdx
<Card
  title="[Client Name in Georgian]"
  icon="[appropriate-icon]"
  href="/clients/[filename]"
>
  [One-line description in Georgian]
</Card>
```

**Icon Suggestions:**
- `hospital` - General hospitals
- `heart-pulse` - Cardiology centers
- `microscope` - Diagnostic centers
- `stethoscope` - General clinics
- `user-doctor` - Medical centers

### 7. Deploy

Changes are automatically deployed when pushed to the main branch:

```bash
cd Radium/RadiumProjects/Tutorials/docs
git add .
git commit -m "Add [Client Name] client page"
git push origin main
```

## Language Rules

🔴 **CRITICAL: ALL content must be in Georgian**

- ✅ **DO:** Write titles, descriptions, paragraphs in Georgian
- ✅ **DO:** Keep filenames in English
- ❌ **DON'T:** Use English in page content
- ❌ **DON'T:** Mix English and Georgian

## Writing Guidelines

### Tone
- Professional and concise
- Focus on facts, not marketing
- Use specific numbers
- Keep it brief

### Structure (SIMPLE - 2 sections only!)
1. **კლიენტის შესახებ**: Brief paragraph about the hospital (from Google search)
2. **სტატისტიკა**: 4 cards with key numbers

### Example Opening Paragraph

```
**[Hospital Name]** არის [location]-ში მდებარე [type: მულტიპროფილური/სპეციალიზებული] 
[facility type: სამედიცინო კლინიკა/საავადმყოფო/დიაგნოსტიკური ცენტრი], რომელიც 
[unique characteristic/specialties]. [Optional: years] წლის გამოცდილებით, კლინიკა 
[main services or approach]. Radium-ის Cloud PACS პლატფორმა უზრუნველყოფს კლინიკის 
სრული რადიოლოგიური ინფრასტრუქტურის მართვას.
```

### What NOT to Include
- ❌ Technical infrastructure details
- ❌ Security and compliance sections
- ❌ "Why they chose Cloud PACS" sections
- ❌ Future plans
- ❌ Detailed modality descriptions
- ❌ Step-by-step implementation details
- ❌ Quotes (unless specifically provided by client)

## Checklist

Before publishing, verify:

- [ ] All text is in Georgian (except filename)
- [ ] Statistics are accurate (4 cards: Total Studies, Devices, Doctors, Modalities)
- [ ] Brief hospital description (1 paragraph only)
- [ ] Logo copied to `images/clients/` folder
- [ ] Navigation updated in `mint.json`
- [ ] Client card added to `clients/index.mdx`
- [ ] NO excessive sections (keep it simple!)
- [ ] Git push uses `required_permissions: ["all"]`

## Common Icons

- `hospital` - Hospital building
- `heart-pulse` - Cardiology
- `microscope` - Laboratory/Diagnostics
- `stethoscope` - General medicine
- `user-doctor` - Physicians
- `calendar` - Years/Date
- `users` - Patients
- `database` - Studies/Data
- `cloud` - Cloud services
- `shield` - Security
- `arrow-up` - Growth/Improvement
- `link` - Integration
- `expand` - Scalability

## Resources

- **Live Site**: https://radium-98210c26.mintlify.app/
- **Repo**: https://github.com/brizhamadze/docs
- **Mintlify Docs**: https://mintlify.com/docs/components
- **Icon Library**: https://fontawesome.com/icons










