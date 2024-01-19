from pathlib import Path

def extract_file_paths():
    directory_path = r"C:\Users\mahal\Downloads\exe_files copy"
    extensions = {".exe", ".dll", ".sys", ".acm", ".ax", ".cpl", ".drv", ".efi", ".mui", ".ocx", ".scr", ".tsp", ".mun"} 
    directory = Path(directory_path)
    # Make sure the directory exists
    if not directory.exists() or not directory.is_dir():
        return []
    file_paths = []
    for file_path in directory.rglob("*"):
        if file_path.is_file() and file_path.suffix.lower() in extensions:
            file_paths.append(rf"{file_path}")
    return file_paths



