import os

base_path = "/Users/brair/Documents/CodeBase/Medspace/Radium/RadiumProjects/Tutorials/docs"

categories = {
    "getting-started": {
        "title": "დაწყება და ინტერფეისი",
        "description": "ავტორიზაცია, ინტერფეისის მიმოხილვა და მობილური ვერსია"
    },
    "search": {
        "title": "ძიება და შედარება",
        "description": "ფაილების და პაციენტების ძიება, ფილტრები და შედარება"
    },
    "space-management": {
        "title": "სფეისის მართვა",
        "description": "პარამეტრები, მომხმარებლები, ბილინგი და პრომპტები"
    },
    "patients-files": {
        "title": "პაციენტები და ფაილები",
        "description": "პაციენტების დამატება, ფაილების ატვირთვა და მართვა"
    },
    "dicom-viewer": {
        "title": "DICOM მნახველი",
        "description": "სამედიცინო გამოსახულებების ნახვა და დამუშავება"
    },
    "sharing": {
        "title": "გაზიარება და კომუნიკაცია",
        "description": "ფაილების გაზიარება და ვიდეო კონფერენცია"
    },
    "workflows": {
        "title": "AI Workflow-ები",
        "description": "AI პროცესების ავტომატიზაცია და გამოყენება"
    },
    "ai-chat": {
        "title": "AI ჩატი",
        "description": "კონტექსტური ჩატი ხელოვნურ ინტელექტთან"
    }
}

for folder, meta in categories.items():
    folder_path = os.path.join(base_path, folder)
    file_path = os.path.join(folder_path, "index.mdx")
    
    content = f"""---
title: '{meta['title']}'
description: '{meta['description']}'
---

## {meta['title']}

აქ განთავსდება {meta['title']}-სთან დაკავშირებული დოკუმენტაცია.
"""
    
    with open(file_path, "w") as f:
        f.write(content)

print("Index files created successfully")
