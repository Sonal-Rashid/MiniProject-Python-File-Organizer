# Python File Organizer
A Python script that organizes files into folders based on their file extensions. Users can choose to organize the current working directory or specify another folder.

## 📊 Project Overview 
This Python File Organizer sorts images, audio, videos, documents, scripts, archives, and spreadsheets into separate folders based on file extensions. Users can choose the folder to organize, and the program automatically creates the necessary folders and moves files into their respective categories.

## ✨ Program Explanation
- Import Modules:Uses `os` for file and folder operations and `shutil` to move files.
- Select Folder: Allows users to organize the current working directory or choose another folder.
- Validate Folder Path: Checks whether the selected folder exists.
- Define File Types: Uses a dictionary to map file extensions to categories such as Images, Documents, Videos, and Scripts.
- Create Folders: Automatically creates category folders if they do not already exist.
- Identify File Extensions: Extracts and converts file extensions to lowercase for consistent matching.
- Organize Files: Moves each supported file into its corresponding category folder.
- Skip Directories and Script: Prevents existing folders and the running Python script from being moved.
- Display Output: Prints a completion message.

## 🛠️ Technologies Used
- Python
- `os` module
- `shutle` module

## ▶️ How to Run
1. Clone this repository.
2. Open a terminal in the project folder.
3. Run the following command:
   
    ```bash
   python3 main.py
   ```

## 📚 Concepts Practiced
- Python variables and user input
- Conditional statements (if, elif, else)
- Dictionaries and lists
- for loops and nested loops
- String methods and file extensions
- File and directory handling using os
- File movement using shutil
- Path manipulation using os.path.join()
   
  
