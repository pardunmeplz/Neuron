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
        w = tk.Text(
            root,
            height = 5,
            width = style['width'],
            bg = style['bg'],
            fg= style['fg'],
            border=30,
            relief =tk.FLAT,
            font= f"{style['font']} {style['size']}"
        )

        # configure tags
        w.tag_config('h1', font=f"{style['font']} {style['h1Size']}",
        foreground=style['h1Color'])
        
        w.tag_config('h2', font=f"{style['font']} {style['h2Size']}",
        foreground=style['h2Color'])

        w.tag_config('h3', font=f"{style['font']} {style['h3Size']}",
        foreground=style['h3Color'])

        w.pack(expand=1, fill= tk.BOTH, side=tk.LEFT)
        w['state'] = tk.DISABLED
        self.widget = w

    def write(self,text,newline = True, tags = []):
        w = self.widget

        if w.get(1.0,'end').strip()=="": newline = False
        
        w['state'] = tk.NORMAL
        if newline: w.insert('end',"\n")
        
        w.insert('end', text)

        w['state'] = tk.DISABLED
    
    def add_tags(self,tags:list):
        w = self.widget
        
        w['state'] = tk.NORMAL
        for tag,start,end in tags:
            w.tag_add(tag,start,end)

        w['state'] = tk.DISABLED

    def clear(self):
        w = self.widget
        w['state'] = tk.NORMAL
        w.delete(1.0,'end')


if __name__ == "__main__":
    root = tk.Tk()
    text = '# Hello World'
    disp = Display(root)
    disp.write(text)
    disp.write(text)
    root.mainloop()