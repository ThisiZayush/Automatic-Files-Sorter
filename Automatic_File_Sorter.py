import os
import shutil

BASE_PATH = r"YOUR_PATH_HERE"

FOLDER_MAPPING = {
    ".xlsx": "Excel Files",
    ".xls": "Excel Files",
    ".csv": "Excel Files",

    ".jpg": "Image Files",
    ".jpeg": "Image Files",
    ".png": "Image Files",
    ".gif": "Image Files",

    ".txt": "Text Files",
    ".pdf": "PDF Files",
    ".docx": "Word Files",
    ".pptx": "PowerPoint Files",
    ".zip": "Archives",
    ".mp3": "Music",
    ".mp4": "Videos"
}


def create_folders():
    """Create destination folders if they don't exist."""
    for folder in set(FOLDER_MAPPING.values()):
        os.makedirs(os.path.join(BASE_PATH, folder), exist_ok=True)


def move_files():
    """Move files into their respective folders."""
    for file in os.listdir(BASE_PATH):
        source_path = os.path.join(BASE_PATH, file)

        # Skip folders
        if not os.path.isfile(source_path):
            continue

        _, extension = os.path.splitext(file)
        extension = extension.lower()

        if extension not in FOLDER_MAPPING:
            print(f"Skipped: {file} (unsupported file type)")
            continue

        destination_folder = os.path.join(
            BASE_PATH,
            FOLDER_MAPPING[extension]
        )

        destination_path = os.path.join(destination_folder, file)

        # Prevent overwriting existing files
        if os.path.exists(destination_path):
            filename, ext = os.path.splitext(file)
            counter = 1

            while True:
                new_name = f"{filename}_{counter}{ext}"
                destination_path = os.path.join(destination_folder, new_name)

                if not os.path.exists(destination_path):
                    break

                counter += 1

        shutil.move(source_path, destination_path)
        print(f"Moved: {file} → {destination_folder}")


def main():
    create_folders()
    move_files()
    print("\nOrganization complete!")


if __name__ == "__main__":
    main()