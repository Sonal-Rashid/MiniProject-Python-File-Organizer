import os
import shutil

print("--- Python File Organizer ---")

# Folder that you want to organize - user choice
print("1. Organize the current working directory")
print("2. Organize another folder")

choice = input("Enter your choice (1 or 2): ")
if choice == "1":
    folder_path_to_organize = os.getcwd()  
elif choice == "2":
    folder_path_to_organize = input("Enter your folder path: ").strip()
    folder_path_to_organize = os.path.expanduser(folder_path_to_organize)
else:
    print("Invalid choice! - Enter only 1 or 2")
    exit()

if not os.path.isdir(folder_path_to_organize):
    print("The folder does not exist. Please check the path.")
    exit()

print(f"\nFolder selected: {folder_path_to_organize}")

# file type mapping
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg"],
    "Audios": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Documents": [".pdf", ".txt", ".doc", ".docx"],
    "Archives": [".zip", ".rar"],
    "Scripts": [".py", ".js", ".sh", ".html"],
    "Excel_Files": [".xlsx", ".xls", ".csv"]
}

# create folders if they don't exist
for folder in file_types:
    folder_path = os.path.join(folder_path_to_organize, folder)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

# organize files
for file in os.listdir(folder_path_to_organize):
    file_path = os.path.join(folder_path_to_organize,file)

    # skip files
    if os.path.isdir(file_path) or file == "main.py":
        continue
    # get file extension
    file_ext = os.path.splitext(file)[1].lower()

    for folder, extensions in file_types.items():
        if file_ext in extensions:
            destination_path = os.path.join(folder_path_to_organize, folder, file)
            shutil.move(file_path, destination_path)
            break

print("\nFile organized successfully!")
