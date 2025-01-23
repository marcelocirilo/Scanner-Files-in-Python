# Directory File Listing Script

## Description
This script recursively traverses a directory tree starting from a user-provided root directory and generates a list of all files within the directory and its subdirectories. The list of file paths is saved to a text file (`listfiles.txt`).

## Features
- Recursively scans all files in the provided directory and its subdirectories.
- Displays the total number of files found.
- Outputs the list of file paths to a `listfiles.txt` file.

## How It Works
1. The script prompts the user to input the path to the root directory.
2. It uses `os.walk()` to iterate through all files in the directory tree.
3. Collects the full file paths into a list.
4. Prints the total number of files.
5. Saves the file paths to `listfiles.txt` in the script's working directory.

## Prerequisites
- Python 3.12 installed.

## Usage
1. Clone or download the script.
2. Open a terminal and navigate to the script's directory.
3. Run the script with:
   ```bash
   python main.py
4. When prompted, enter the full path of the directory to scan.
5. The script will:
- Print the total number of files found.
- Save the list of file paths to a file named listfiles.txt.

## Example
### Running the Script
python main.py

### Input
When prompted:
 ```bash
 Enter the path:
```
Enter `dir/example` as the root directory.

### Output
```bash
Total Files: 4
```
The listfiles.txt will contain:
```bash
dir/example/file1.txt
dir/example/file2.txt
dir/example/subdir/file3.txt
dir/example/subdir/file4.txt
```

## Notes
- Ensure the specified directory exists and is accessible.
- The script creates the listfiles.txt file in the same directory where the script is executed.
- If you lack write permissions in the working directory, the script will fail to save the output.

## License
This project is licensed under the MIT License.
