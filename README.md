# Get-Folder-Structure

This project is a Python script that generates a tree-like structure of a specified folder's contents. The script recursively lists all files and directories within a folder and presents them in a visually appealing tree diagram.

## Features

- Recursively lists all files and directories in a specified folder.
- Outputs the folder structure in a tree diagram format.
- Easy to customize for different directories.

## Prerequisites

- Python 3.x installed on your system.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/Get-Folder-Structure.git

2. **Navigate to the project directory:**

   ```bash
   cd Get-Folder-Structure

3. **Install any required dependencies:**

This script doesn't require any external dependencies, so you can run it directly with Python.

## Usage

1. **Modify the root_folder path:**

Open the main.py file and replace the root_folder variable with the path to the folder you want to analyze.

   ```bash
   if __name__ == "__main__":
    root_folder = r"C:\path\to\your\folder"  # Replace with your folder path
    get_file_structure(root_folder)

2. **Run the script:**

Execute the script using Python:

   ```bash
   python main.py

3. **View the output:**

The script will print the folder structure in a tree diagram format to the console.

Example output:

   ```bash
   your-folder/
    ├── subfolder1/
    │   ├── file1.txt
    │   └── file2.txt
    ├── subfolder2/
    │   ├── file3.txt
    │   └── file4.txt
    └── file5.txt

## Customization

- Changing the folder path: Update the root_folder variable in main.py with the path to your desired folder.

- Modifying the output format: You can adjust the indentation or tree symbols by modifying the get_file_structure function.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.