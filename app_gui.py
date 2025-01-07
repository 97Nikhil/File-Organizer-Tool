import tkinter as tk
from tkinter import messagebox, filedialog, font
from sorter_logic import sort_folder, undo_sort


def create_gui():
    def browse_folder():
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            path_entry.delete(0, tk.END)  # Clear existing text
            path_entry.insert(0, folder_selected)  # Insert folder path

    def run_sorter():
        folder_path = path_entry.get()
        if not folder_path:
            messagebox.showerror("Error", "Please enter or select a folder path.")
            return
        # Call the sort_folder function and show the result
        result = sort_folder(folder_path)

    def show_instructions():
        instructions = (
            "How to Use the File Organizer Tool:\n\n"
            "1. **Choose a Folder:**\n"
            "   - Enter the path of the folder in the input field manually.\n"
            "   - OR click on the 'Browse' button to select the folder where your files are located.\n\n"
            "2. **Click 'Sort Folder':**\n"
            "   - Once the folder path is entered, click the 'Sort Folder' button.\n"
            "   - The tool will organize all the files into subfolders based on their file types (e.g., Images, Documents, Videos).\n\n"
            "3. **Check the Organized Folder:**\n"
            "   - Open the selected folder to see the newly created subfolders, each containing files of the corresponding type.\n"
            "   - For example, all `.jpg` or `.png` files will be moved into an 'Images' folder, `.pdf` files into 'Documents,' etc.\n\n"
            "4. **Undo Sorting:**\n"
            "   - If you accidentally sort files, use the 'Undo' feature to move files back to their original location.\n\n"
        )
        messagebox.showinfo("Instructions", instructions)

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
        command=browse_folder,
        bg="#F9AA33",
        fg="#344955",
        font=custom_font,
        relief="flat",
    )
    browse_button.pack(side="left", padx=5)

    # Sort button
    button_frame = tk.Frame(frame, bg="#344955")
    button_frame.pack(pady=30)

    sort_button = tk.Button(
        button_frame,
        text="Sort Folder",
        command=run_sorter,
        bg="#F9AA33",
        fg="#344955",
        font=("SF Pro", 16, "bold"),
        width=15,
        relief="flat",
    )
    sort_button.pack(side="left", padx=10)

    undo_button = tk.Button(
        button_frame,
        text="Undo Sort",
        command=undo_sort,
        bg="#F9AA33",
        fg="#344955",
        font=("SF Pro", 16, "bold"),
        width=15,
        relief="flat",
    )
    undo_button.pack(side="left", padx=10)

    # Footer with instructions button
    footer_frame = tk.Frame(frame, bg="#344955")
    footer_frame.pack(side="bottom", fill="x", pady=10)

    footer_label = tk.Label(
        footer_frame,
        text="Developed by Nikhil",
        bg="#344955",
        fg="#AAAAAA",
        font=("SF Pro", 10, "italic"),
    )
    footer_label.pack(side="left", padx=10)

    instructions_button = tk.Button(
        footer_frame,
        text="i",
        command=show_instructions,
        bg="#F9AA33",
        fg="#344955",
        font=("SF Pro", 12, "italic"),
        width=3,
        height=1,
        relief="flat",
    )
    instructions_button.pack(side="right", padx=10)

    window.mainloop()


if __name__ == "__main__":
    create_gui()
