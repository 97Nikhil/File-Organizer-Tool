import os
import shutil
from tkinter import messagebox

EXTENSION_MAPPING = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"],
    "Spreadsheets":[".xls", ".xlsx", ".csv"],
    "Presentations":[".ppt", ".pptx", ".odt"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".flv", ".wmv", ".webm"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2"],
    "Code": [".py", ".java", ".js", ".html", ".css", ".cpp", ".cs", ".php", ".sql", ".xml", ".json"],
    "Executables": [".exe", ".msi", ".bat", ".sh", ".apk", ".jar"],
    "Design": [".psd", ".ai", ".xd", ".fig", ".sketch"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
    "System Files":[".dll", ".ini", ".sys"],
    "Others": []  # Files with no extension or unrecognized types
}

old_path_lst = []

# Find folder using extension
def get_folder_name(extension):
    for folder, extensions in EXTENSION_MAPPING.items():
        if extension.lower() in extensions:
            return folder
    return "Other" 


def sort_folder(path):
    # check path exists or not
    if not os.path.exists(path):
        messagebox.showerror("Error", "The specified path does not exist!")
        return
    
    files = os.listdir(path)

    # check if folder is empty
    if not files:
        messagebox.showerror("Info", "The folder is empty!")
        return
    
    for file in files:
        full_path = os.path.join(path, file)
        if os.path.isfile(full_path):
            _, extension = os.path.splitext(file)
            folder_name = get_folder_name(extension)
            dest_folder = os.path.join(path, folder_name)
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(full_path, os.path.join(dest_folder, file))

    messagebox.showinfo("Success", "Files have been successfully organized!")


def undo_sort():
    pass