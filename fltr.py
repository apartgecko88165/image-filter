# import 'tkinter' elements for GUI
import tkinter as tk
from tkinter import filedialog
from tkinter.simpledialog import askstring

# import pillow for image handling
from PIL import Image, ImageTk


class Filter(tk.Tk):

    def _audit(self):
        for item in self.lineup:
            pass

    def _grey(self, image):
        # Creates an ImageCore Object from original image
        pixels = image.getdata()
        # Creates empty array to hold new pixel values
        new_pixels = [] 
        # For every pixel from our original image, it saves
        # a copy of that pixel to our new_pixels array
        for p in pixels:
            new_pixels.append(p)
        # Starts at the first pixel in the image
        location = 0
        # Continues until it has looped through all pixels
        while location < len(new_pixels):
            # Gets the current color of the pixel at location
            p = new_pixels[location]
            # Splits color into red, green and blue components
            r = p[0]
            g = p[1]
            b = p[2]
            # Perform pixel manipulation and stores results
            # to a new red, green and blue components
            newr = (r + g + b) // 3
            newg = (r + g + b) // 3
            newb = (r + g + b) // 3
            # Assign new red, green and blue components to pixel
            # at that specific location
            new_pixels[location] = (newr, newg, newb)
            # Changes the location to the next pixel in array
            location = location + 1
        # Creates a new image, the same size as the original 
        # using RGB value format
        new_image = Image.new("RGB", image.size)
        # Assigns the new pixel values to newImage
        new_image.putdata(new_pixels)
        # Sends the newImage back to the main portion of program
        return new_image

            
    def _resize(self, image):
        aspect_ratio = image.height / image.width

        width = 600
        height = width * aspect_ratio
        
        display = image.resize((width, int(height)), Image.ANTIALIAS)
        
        self.disp = display
        self.image = image
        self.photo = ImageTk.PhotoImage(display)

    def _save(self, image):
        fname = askstring("File name", "Enter the name for your file")
        directory = filedialog.askdirectory()

        image.save(f"{directory}/{fname}.jpg")

    def _show(self, ph, clicked):
        ph.config(text=clicked.get())


        if self.clicked.get() == "Grayscale":
            self._resize(self.image)

            self.disp = self._grey(self.disp)

            #filtered.show()

            self.disp.save("temp/photo.jpg")

            display = ImageTk.PhotoImage(file="temp/photo.jpg")

            self.canvas.configure(image=display)
            self.canvas.image = display

    def start(self, image):

        self.original = image

        self.lineup = []

        self.title("Image Filter")
        
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.attributes("-fullscreen",True)

        self._resize(image)
        
        # Dropdown menu options
        filters = [
            "Grayscale"
        ]
        
        # datatype of menu text
        self.clicked = tk.StringVar()
        
        # initial dropdown text
        self.clicked.set("Select a Filter")

        self.canvas = tk.Label(self, image=self.photo)
        self.canvas.place(x=0, y=0)
        
        # create menu
        tk.OptionMenu(self , self.clicked , *filters).place(x=600)
        self.ph = tk.Label(self , text=" ")
        tk.Button(self, text="APPLY", command=lambda: self._show(self.ph, self.clicked)).place(x=500, y=1)
        tk.Button(self, text="SAVE", command=lambda: self._save(self.disp)).place(x=self.disp.width-40, y=self.disp.height-30)

        tk.Label(self, text=f"{self.image.width}x{self.image.height}").place(x=0, y=0)

        self.mainloop()

if __name__ == "__main__":
    Filter().start(Image.open("demo/demo.jpg"))