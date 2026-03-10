import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


def organize_files():
    folder_path = filedialog.askdirectory()

    if not folder_path:
        return

    files = os.listdir(folder_path)

    for file in files:

        file_path = os.path.join(folder_path, file)

        if os.path.isdir(file_path):
            continue

        extension = file.split(".")[-1]

        folder_name = extension.upper() + "_Files"
        folder_destination = os.path.join(folder_path, folder_name)

        if not os.path.exists(folder_destination):
            os.makedirs(folder_destination)

        shutil.move(file_path, os.path.join(folder_destination, file))

    messagebox.showinfo("Done", "Files organized successfully!")


# Create window
root = tk.Tk()
root.title("File Organizer")
root.geometry("300x150")

# Button
btn = tk.Button(root, text="Select Folder and Organize", command=organize_files)
btn.pack(pady=40)

root.mainloop()
