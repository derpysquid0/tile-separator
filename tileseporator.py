from PIL import Image
import tkinter as tk
from tkinter import filedialog



root = tk.Tk()

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500


tile_size = tk.StringVar()
padding = tk.StringVar()

#colors
RED = [255, 0, 0]
BLUE = [0, 0, 255]
DARK_RED = [200, 10, 10]
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREY = [230, 230, 230]

REALfilepath : str = ""
REALfiledestination : str = ""



root.title("tileset separator")
root.geometry(f"{SCREEN_HEIGHT}x{SCREEN_WIDTH}")
root.config(background="blue")





label = tk.Label(root, text="STATUS: unsaved", background="red")
label.pack()

def file():
    global REALfilepath
    file_path = filedialog.askopenfilename(
        title="Select a File",
        initialdir="/Downloads",  # Optional: starting directory
        filetypes=(("Text files", "*.png"), ("All files", "*.*")) # Optional: filter file types
    )
    REALfilepath = file_path
    if file_path:
        print(f"Selected file: {file_path}")
        
    else:
        print("No file selected.")


def separate(tilesize:int, ppadding:int):
    
    img = Image.open(REALfilepath)
    w, h = img.size

    cols = w // tilesize
    rows = h // tilesize

    new_w = cols * (tilesize + ppadding) + ppadding
    new_h = rows * (tilesize + ppadding) + ppadding
    new_img = Image.new("RGBA", (new_w, new_h), (0, 0, 0, 0))

    for y in range(rows):
        for x in range(cols):
            tile = img.crop((x*tilesize, y*tilesize, (x+1)*tilesize, (y+1)*tilesize))
            new_x = x * (tilesize + ppadding) + ppadding
            new_y = y * (tilesize + ppadding) + ppadding
            new_img.paste(tile, (new_x, new_y))

    new_img.save("tileset_with_padding.png")



filebutton = tk.Button(root, text="Choose file", command=file)
filebutton.pack(pady=20)
filepathlabel = tk.Label(root, text="Path: ", background="gray")
filepathlabel.pack(pady=10)



tilesizelabel = tk.Label(root, text="Tile size")
tilesizelabel.pack(pady=10)
tilesizeedit = tk.Entry(root, textvariable=tile_size, background="darkblue", fg="yellow")
tilesizeedit.pack()


paddinglabel = tk.Label(root, text="Padding (space in-between tiles)")
paddinglabel.pack(pady=10)

paddingedit = tk.Entry(root, textvariable=padding, background="darkblue", fg="yellow")
paddingedit.pack()

def submit():
    tile_size = int(tilesizeedit.get())
    padding = int(paddingedit.get())
    print(tile_size)
    print(padding)
    
    
    separate(tile_size, padding)
    label.config(text="STATUS: saved", background="lightgreen")
    label.pack()



button = tk.Button(root, text="Separate", command=submit)
button.pack(pady=15)


root.mainloop()
