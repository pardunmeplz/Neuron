import tkinter as tk
from tkinter import ttk

def rgbToHex(rgb):
    return '#'+'%02x%02x%02x' % rgb

# styling

style = dict(
bg = rgbToHex((60, 60, 60)),
fg = rgbToHex((200, 200, 200)),
font = 'Calibri',
width = 10,

# Font Sizes
size = 15,
h1Size = 40,
h2Size = 30,
h3Size = 20,

# font Colors
h1Color = rgbToHex((240, 240, 240)),
h2Color = rgbToHex((200, 200, 200)),
h3Color = rgbToHex((160, 160, 160))
)

class Display:

    def __init__(self,root:tk.Tk):
        widget = tk.Text(
            root,
            height = 5,
            width = style['width'],
            bg = style['bg'],
            fg= style['fg'],
            border=30,
            relief =tk.FLAT,
            font= f"{style['font']} {style['size']}"
        )

        widget.pack(expand=1, fill= tk.BOTH, side=tk.LEFT)
        widget['state'] = tk.DISABLED
        self.widget = widget

    def write(self,text):
        widget = self.widget
        widget['state'] = tk.NORMAL
        widget.insert(1.0, text)
        widget['state'] = tk.DISABLED


if __name__ == "__main__":
    root = tk.Tk()
    text = '# Hello World'
    disp = Display(root)
    disp.write(text)
    disp.write(text)
    root.mainloop()