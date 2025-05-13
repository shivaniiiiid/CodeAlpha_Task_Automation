# CodeAlpha_Task_Automation
# File Organizer by Extension

This Python script automatically organizes files in a specified folder based on their extensions. It creates subdirectories for each extension type and moves the corresponding files into those folders.

## Features:
- Scans a given directory for files.
- Creates subdirectories for each file extension.
- Moves files into the respective subdirectories based on their extensions.
- Skips files without extensions (such as directories or hidden files).

## Requirements:
- Python 3.x
- No additional dependencies required (uses built-in libraries `os` and `shutil`).

## How to Use:

### 1. Clone the Repository
First, clone the repository to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Prepare the Script
Ensure you have Python 3.x installed. No additional libraries are needed as this script uses built-in Python libraries.

### 3. Run the Script
To run the script, execute the following command in your terminal:

```bash
python organize_files.py
```

### 4. Provide the Folder Path
You will be prompted to enter the path of the folder you want to organize. For example:
```
Enter the path to organize: /path/to/your/folder
```

### 5. Files Organized
Once you provide the folder path, the script will:
- Create subdirectories for each file extension (if they don’t already exist).
- Move the files into the respective subdirectories based on their extensions.
- Skip any files without extensions or hidden files.

It will display a message once the process is complete:
```
Files organized by extension.
```
