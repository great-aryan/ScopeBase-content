import os
import json

# Base folder
# base_folder = "scope-base-content"

# Folder structure
folders = [
    "schemas",
    "stages",
    "streams",
    "careers",
    "exams"
]

# Files to create inside folders
files = {
    "schemas": ["career.schema.json"],
    "stages": ["class_10.json"],
    "streams": ["commerce.json"],
    "careers": ["doctor.json", "chartered_accountant.json"],
    "exams": ["neet_ug.json"]
}

# Create base folder
# os.makedirs(base_folder, exist_ok=True)

# Create folders and files
for folder in folders:
    folder_path = folder
    os.makedirs(folder_path, exist_ok=True)

    for file_name in files[folder]:
        file_path = os.path.join(folder_path, file_name)

        # Create empty JSON file if it doesn't exist
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                json.dump({}, f, indent=4)

print("✅ Folder structure created successfully!")
