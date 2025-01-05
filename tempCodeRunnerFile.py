import tkinter as tk
from tkinter import messagebox, filedialog, font

def create_gui():
    # Main window
    window = tk.Tk()
    window.title("File Organizer Tool")
    window.geometry("600x400")
    window.configure(bg="#344955")  # Dark background

    # Custom font
    custom_font = font.Font(family="SF Pro", size=14)

    # Frame for content
    frame = tk.Frame(window, bg="#344955", padx=20, pady=20)
    frame.pack(fill="both", expand=True)

    # Title label
    title_label = tk.Label(
        frame,
        text="File Organizer Tool",
        bg="#344955",
        fg="#FFFFFF",
        font=("SF Pro", 20, "bold"),
    )
    title_label.pack(pady=10)

    # Path input
    path_frame = tk.Frame(frame, bg="#344955")
    path_frame.pack(pady=20, fill="x")

    path_label = tk.Label(
        path_frame,
        text="Folder Path:",
        bg="#344955",
        fg="#F9AA33",
        font=custom_font,
    )
    path_label.pack(side="left", padx=5)

    global path_entry
    path_entry = tk.Entry(path_frame, width=30, font=custom_font)
    path_entry.pack(side="left", padx=5)

    browse_button = tk.Button(
        path_frame,
        text="Browse",
        command=None,  # Add function to browse folder here
        bg="#F9AA33",
        fg="#344955",
        font=custom_font,
        relief="flat",
    )
    browse_button.pack(side="left", padx=5)

    # Sort button
    sort_button = tk.Button(
        frame,
        text="Sort Folder",
        command=None,  # Add function to sort folder here
        bg="#F9AA33",
        fg="#344955",
        font=("SF Pro", 16, "bold"),
        width=15,
        relief="flat",
    )
    sort_button.pack(pady=30)

    # Footer
    footer_label = tk.Label(
        frame,
        text="Developed by Nikhil",
        bg="#344955",
        fg="#AAAAAA",
        font=("SF Pro", 10, "italic"),
    )
    footer_label.pack(side="bottom", pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
