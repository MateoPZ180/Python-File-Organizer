# Python File Organizer

## About This Project

I created this Python project to practice automating repetitive tasks and working with files and folders. The program organizes files into different folders based on their file extensions, making it easier to keep things organized.

I wanted to build something simple that could also be useful in everyday situations.

## What It Does

- Sorts files into Images, Documents, Videos, and Audio folders.
- Moves files with unknown extensions into an Other folder.
- Creates folders automatically if they don't already exist.
- Renames duplicate files so existing files don't get overwritten.
- Handles errors when files can't be moved.
- Uses a simple menu to let the user choose which folder to organize.

## How to Use It

1. Make sure Python 3 is installed.
2. Download `File_Organizer.py`.
3. Run the script in PyCharm or from a terminal:

   ```bash
   python File_Organizer.py
   ```

4. Select option 1 to organize files.
5. Enter the path of the folder you want to organize.
6. The program will sort the files into their matching folders.

Select option 2 to exit the program.

**Tip:** Try it on a folder of test files first. The program moves files rather than copying them, and it only sorts files directly inside the selected folder.

## Tools Used

- Python 3
- PyCharm
- Python's built-in `os` and `shutil` modules
