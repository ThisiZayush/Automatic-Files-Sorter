# **Automated File Organization Script**



#### Project Overview



This Python automation tool systematically scans, cleans, and organizes cluttered directories such as your Downloads or Desktop folders. The script evaluates file extensions and routes files into structured, dedicated subdirectories. It includes a duplicate-handling mechanism to ensure zero data loss.



This project demonstrates clean scripting practices, modular programming, OS file-system manipulation, and edge-case error prevention.



Tech Stack and Architecture

Language: Python 3.x



Core Built-in Modules:

OS: Used for directory scanning, path manipulations, and folder generation.

Shutil : Utilized for moving file objects across paths.



#### Key Engineering Features

* Dynamic Folder Creation: Uses mapping dictionaries and os.makedirs(exist\_ok=True) to create target folders dynamically as needed.
* Defensive File Overwriting Check: Implements a loop counter system. If a file with the same name exists in the destination folder, the script automatically renames the incoming file (e.g., document.pdf becomes document\_1.pdf) to prevent accidental data loss.
* Extension Normalization: Converts file extensions to lower-case during evaluation to prevent mismatches caused by variations like .JPG vs .jpg.
* System Safety Isolation: Features validation filters using os.path.isfile() to ensure the script only processes standalone files, leaving existing subfolders unaltered.



#### Supported Mappings



The script automatically categorizes and sorts the following formats into dedicated folders:



* Data/Sheets (.xlsx, .xls, .csv) -> Excel Files
* Images (.jpg, .jpeg, .png, .gif) -> Image Files
* Documents (.txt) -> Text Files
* Documents (.pdf) -> PDF Files
* Documents (.docx) -> Word Files
* Documents (.pptx) -> PowerPoint Files
* Media/Archives (.zip) -> Archives
* Media/Archives (.mp3) -> Music
* Media/Archives (.mp4) -> Videos



#### How to Setup and Run



1. Clone this repository:
 	git clone https://github.com/yourusername/automated-file-sorter.git
2. Navigate to the project directory: 
 	cd automated-file-sorter
3. Run the script: 

&#x09;python file\_sorter.py

