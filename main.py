import os


def print_directory_structure(root_dir, indent=""):
    """
    Виводить структуру директорій і файлів у заданій директорії.

    Args:
        root_dir (str): Шлях до кореневої директорії.
        indent (str): Відступ для вкладених елементів.
    """
    exclude_dirs = {"venv", "tests", "install"}
    exclude_files = {"__pycache__"}

    for item in sorted(os.listdir(root_dir)):
        if item in exclude_dirs or item in exclude_files or item.startswith("."):
            continue

        item_path = os.path.join(root_dir, item)
        if os.path.isfile(item_path):
            print(f"{indent}{item}")
        elif os.path.isdir(item_path):
            print(f"{indent}{item}")
            print_directory_structure(item_path, indent + "----")

if __name__ == "__main__":
    # Коренева директорія проекту
    root_directory = os.getcwd()
    print_directory_structure(root_directory)
