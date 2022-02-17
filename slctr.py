# import 'tkinter' elements for GUI
import tkinter as tk
from tkinter import filedialog

# import pillow for image handling
from PIL import Image

from sys import platform
from os import getcwd

from fltr import Filter

class Selector(tk.Tk):
    def _browse_files(self):
        self.image = filedialog.askopenfilename(
            initialdir="/" if platform == "win32" else getcwd(),
            title="Select a File",
            filetypes=(
                ("PNG files", "*.png*"),
                ("JPG files", "*.jpg*"),
                ("all files", "*.*")
            )
        )

        self.destroy()
        Filter().start(Image.open(self.image))
    
    def start(self):
        self.title("Image Filter")
        tk.Button(self, text="Browse Files", command=self._browse_files).grid(row=0, column=0)
        self.mainloop()