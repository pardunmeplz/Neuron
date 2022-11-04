import tkinter as tk
import tkinter.font as font
from styles import display as s

class Display:

    def __init__(self,root:tk.Tk):
        w = tk.Text(
            root, height = 5,
            width = s['width'],
            bg = s['bg'], fg= s['fg'],
            border=30,relief =tk.FLAT,
            font= f"{s['font']} {s['size']}"
        )

        # configure tags
        w.tag_config('h1', font=f"{s['font']} {s['h1Size']}",foreground=s['h1Color'])
        w.tag_config('h2', font=f"{s['font']} {s['h2Size']}",foreground=s['h2Color'])
        w.tag_config('h3', font=f"{s['font']} {s['h3Size']}",foreground=s['h3Color'])

        w.tag_config('bold', font=font.Font(size=s['size'],weight='bold'))
        w.tag_config('italic', font=font.Font(size=s['size'],slant='italic'))

        w.pack(expand=1, fill= tk.BOTH, side=tk.RIGHT)
        w['state'] = tk.DISABLED
        self.widget = w

    def write(self,text,newline = True, tags = []):
     
        w = self.widget
        w['state'] = tk.NORMAL
        
        if w.get(1.0,'end').strip()=="": newline = False
        if newline: w.insert('end',"\n")
        
        w.delete(1.0,'end')
        w.insert('end', text)
        w['state'] = tk.DISABLED
    
    def add_tags(self,tags:list):

        w = self.widget        
        w['state'] = tk.NORMAL

        for tag,start,end in tags:
            w.tag_add(tag,start,end)

        w['state'] = tk.DISABLED
    
    def _getIndex(self,show):
        w = self.widget
        show(line = w.index("current"))

    def mouseBind(self,key,fn):
        w = self.widget
        w.bind(f'<{key}-Button>',lambda _:self._getIndex(fn))

    def bind(self,event,fn):
        w = self.widget
        w.bind(event,fn)