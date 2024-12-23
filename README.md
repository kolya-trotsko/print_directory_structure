# print_directory_structure

This script prints the directory structure of a given project, excluding specified files and directories such as virtual environments (`venv`), test folders, and cache files.

## Features

- Recursively displays files and folders in a clear, indented format.
- Excludes specific directories (`venv`, `tests`, `install`) and files (`__pycache__`, hidden files starting with `.`).
- Can be run from any directory or accept a custom root directory as an argument.

## Usage

1. Clone the repository or download the script:
   ```bash
   git clone https://github.com/kolya-trotsko/print_directory_structure.git
   cd yourrepository
   ```

2. Run the script in your project directory:
   ```bash
   python main.py
   ```

   Alternatively, specify a custom root directory:
   ```bash
   python print_directory_structure.py /path/to/your/project
   ```

## Example Output

```
main.py
folder
----file_in_folder.py
another_folder
----sub_folder
--------file_in_sub_folder.py
```

## Customization

- To exclude additional directories or files, update the `exclude_dirs` and `exclude_files` sets in the script:
  ```python
  exclude_dirs = {"venv", "tests", "install"}
  exclude_files = {"__pycache__"}
  ```

## Requirements

- Python 3.6 or later.

