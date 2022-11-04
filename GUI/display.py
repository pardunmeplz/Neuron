import tkinter as tk
import tkinter.font as font
from styles import display as s

class Display:

    def __init__(self,root:tk.Tk):
        w = tk.Text(
            root,
            height = 5,
            width = s['width'],
            bg = s['bg'],
            fg= s['fg'],
            border=30,
            relief =tk.FLAT,
            font= f"{s['font']} {s['size']}"
        )
        # configure tags
        w.tag_config('h1', font=f"{s['font']} {s['h1Size']}",
        foreground=s['h1Color'])
        
        w.tag_config('h2', font=f"{s['font']} {s['h2Size']}",
        foreground=s['h2Color'])

        w.tag_config('h3', font=f"{s['font']} {s['h3Size']}",
        foreground=s['h3Color'])

        w.tag_config('bold', font=font.Font(size=s['size'],weight='bold'))

        w.tag_config('italic', font=font.Font(size=s['size'],slant='italic'))

        w.pack(expand=1, fill= tk.BOTH, side=tk.LEFT)
        w['state'] = tk.DISABLED
        self.widget = w

    def write(self,text,newline = True, tags = []):
        self.clear()
        
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