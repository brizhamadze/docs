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

**Template Structure:**

```mdx
---
title: '[Hospital Name in Georgian]'
description: '[One-line description in Georgian]'
---

<Frame>
  <img src="/images/clients/[client-name]-logo.png" alt="[Client Name]" />
</Frame>

## კლიენტის შესახებ

[Appealing introductory paragraph about the hospital - IN GEORGIAN]

<CardGroup cols={3}>
  <Card title="[Year/Number]" icon="[icon-name]">
    **[Statistic Label]**
  </Card>
  <Card title="[Number]" icon="[icon-name]">
    **[Statistic Label]**
  </Card>
  <Card title="[Number]" icon="[icon-name]">
    **[Statistic Label]**
  </Card>
</CardGroup>

## HealthTech გადაწყვეტა

[Description of the solution provided - IN GEORGIAN]

### გამოყენებული მოდალითები
- **CT (კომპიუტერული ტომოგრაფია)**: [Usage details]
- **X-Ray (რენტგენი)**: [Usage details]
- **Mammography (მამოგრაფია)**: [Usage details]
- **Ultrasound (ულტრაბგერა)**: [Usage details]

## შედეგები

<CardGroup cols={2}>
  <Card title="[Number] კვლევა" icon="database">
    Cloud PACS-ში შენახული
  </Card>
  <Card title="[Number]+ მოდალითი" icon="microscope">
    ინტეგრირებული სისტემა
  </Card>
  <Card title="24/7 წვდომა" icon="cloud">
    ნებისმიერი ადგილიდან
  </Card>
  <Card title="უსაფრთხო" icon="shield">
    დაშიფრული მონაცემები
  </Card>
</CardGroup>

## ციტატა

<Note>
**[Name, Title]**

"[Quote about the service - IN GEORGIAN]"
</Note>
```

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
- Professional but friendly
- Focus on partnership and success
- Emphasize benefits and results
- Use specific numbers and statistics

### Structure
1. **Opening paragraph**: Introduce the client and their reputation
2. **Statistics cards**: Show impressive numbers
3. **Solution description**: What we provided
4. **Modalities/Services**: Specific technical details
5. **Results**: Impact and outcomes
6. **Quote**: Testimonial from client (when available)

### Example Opening Paragraph

```
**[Hospital Name]** არის [description of hospital type] [location]-ში, რომელიც 
განსაკუთრებულია [special characteristic]. [Years] წლის გამოცდილებით, 
[Hospital Name] მსახურობს [number]+ პაციენტს წელიწადში და აერთიანებს 
[specialties]. Radium-ის Cloud PACS პლატფორმა უზრუნველყოფს [key benefit] 
და [another benefit], რაც საშუალებას აძლევს [outcome].
```

## Checklist

Before publishing, verify:

- [ ] All text is in Georgian (except filename)
- [ ] Statistics are accurate
- [ ] Navigation updated in `mint.json`
- [ ] Client card added to `clients/index.mdx`
- [ ] Images referenced exist (or use placeholder)
- [ ] Icons are appropriate
- [ ] Links work correctly
- [ ] Content is professional and appealing
- [ ] Git push uses `required_permissions: ["all"]` if needed

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
