import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mov"],
    "Archives": [".zip", ".rar", ".tar"],
    "Music": [".mp3", ".wav"],
    "Others": []
}

def organize_files(folder_path):
    if not os.path.isdir(folder_path):
        messagebox.showerror("Error", "Invalid folder path!")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            moved = False
            for category, extensions in file_types.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    category_path = os.path.join(folder_path, category)
                    os.makedirs(category_path, exist_ok=True)
                    shutil.move(file_path, category_path)
                    moved = True
                    break

            if not moved:
                other_path = os.path.join(folder_path, "Others")
                os.makedirs(other_path, exist_ok=True)
                shutil.move(file_path, other_path)

    messagebox.showinfo("Success", "Files organized successfully!")

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        organize_files(folder_path)

# 
root = tk.Tk()
root.title("File Organizer")

label = tk.Label(root, text="Select a folder to organize:")
label.pack(pady=10)

browse_button = tk.Button(root, text="Browse", command=browse_folder)
browse_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=5)

root.geometry("300x150")
root.mainloop()
