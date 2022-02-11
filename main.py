# import 'tkinter' elements for GUI
import tkinter as tk
from tkinter import filedialog

# import pillow for image handling
from PIL import ImageTk, Image

class Filter(tk.Tk):

    def start(self, image):
        self.image = image
        width = (self.image.size[0] / self.image.size[1]) * 50
        
        self.image.resize((int(width), 400))

        self.photo = ImageTk.PhotoImage(self.image)

        tk.Entry(self).grid(row=0, column=0)
        tk.Label(self, image=self.photo).grid(row=0, column=1)

        self.mainloop()
 
class Selector(tk.Tk):
    def _browse_files(self):
        self.image = filedialog.askopenfilename(
            initialdir = "/",
            title = "Select a File",
            filetypes = (
                ("PNG files", "*.png*"),
                ("JPG files", "*.jpg*"),
                ("all files", "*.*")
            )
        )

        self.destroy()
        Filter().start(Image.open(self.image))
    
    def start(self):
        tk.Button(self, text="Browse Files", command=self._browse_files).grid(row=0, column=0)

        self.mainloop()

if __name__ == "__main__":
    Selector().start()