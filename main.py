import os

def get_file_structure(root_folder):
    for root, dirs, files in os.walk(root_folder):
        level = root.replace(root_folder, '').count(os.sep)
        indent = '│   ' * level + '├── ' if level > 0 else ''
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = '│   ' * (level + 1) + '├── '
        for i, f in enumerate(files):
            if i == len(files) - 1:  # Check if it's the last file
                print(f"{sub_indent[:-4]}└── {f}")
            else:
                print(f"{sub_indent}{f}")

if __name__ == "__main__":
    root_folder = r"C:\Users\Adingiswayo\Documents\Code\Python\Git Clones\speedtest-automation"  # Replace with the path to your folder
    get_file_structure(root_folder)
