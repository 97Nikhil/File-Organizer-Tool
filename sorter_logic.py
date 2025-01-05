import os
import shutil
from tkinter import messagebox


def sort_folder(path):
    if not os.path.exists(path):
        messagebox.showerror("Error", "The specified path does not exist!")
        return
    
    files = os.listdir(path)
    if not files:
        messagebox.showinfo("Info", "The folder is already empty!")
        return

    for file in files:
        full_path = os.path.join(path, file)
        if os.path.isfile(full_path):
            _, extension = os.path.splitext(file)
            extension = extension[1:]  # Remove the dot from the extension
            if not extension:  # Skip files with no extension
                extension = "Others"

            dest_folder = os.path.join(path, extension)
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(full_path, os.path.join(dest_folder, file))

    messagebox.showinfo("Success", "Files have been successfully organized!")
    

