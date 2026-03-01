import os
import shutil
import argparse

# --- Command-line argument parsing ---
parser = argparse.ArgumentParser(description="Organize files in a folder by type.")
parser.add_argument('--folder', type=str, required=True, help='Path to the folder to organize')
parser.add_argument('--preview', action='store_true', help='Preview only, no actual moves')

args = parser.parse_args()
folder_path = args.folder
preview = args.preview


# --- File type mapping ---
EXTENSION_MAP = {
    'Images': ['.png', '.jpg', '.jpeg', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Music': ['.mp3', '.wav'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Archives': ['.zip', '.rar', '.7z'],
}

def get_category(extension):
    for category, extensions in EXTENSION_MAP.items():
        if extension.lower() in extensions:
            return category
    
    return 'Others'

# --- Organizing logic ---
for item in os.listdir(folder_path):
    item_path = os.path.join(folder_path, item)

    if os.path.isfile(item_path):
        _, ext = os.path.splitext(item)
        category = get_category(ext)
        target_folder = os.path.join(folder_path, category)

        # Make category folder if it doesn't exist
        if not os.path.exists(target_folder):
            if not preview:
                os.makedirs(target_folder)

        new_path = os.path.join(target_folder, item)

        if preview:
            print(f"[PREVIEW] Would move {item} to {category}/")
        else:
            print(f"Moving {item} → {category}/")
            shutil.move(item_path, new_path)
