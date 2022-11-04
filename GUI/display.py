import tkinter as tk
import tkinter.font as font
from styles import display as s

class Display(tk.Text):

    def __init__(self,root):
        tk.Text.__init__(
            self,root,
            height = 5,width = s['width'],
            bg = s['bg'], fg= s['fg'],
            border=30,relief =tk.FLAT,
            font= f"{s['font']} {s['size']}"
        )

        # configure tags
        self.tag_config('h1', font=f"{s['font']} {s['h1Size']}",foreground=s['h1Color'])
        self.tag_config('h2', font=f"{s['font']} {s['h2Size']}",foreground=s['h2Color'])
        self.tag_config('h3', font=f"{s['font']} {s['h3Size']}",foreground=s['h3Color'])

        self.tag_config('bold', font=font.Font(size=s['size'],weight='bold'))
        self.tag_config('italic', font=font.Font(size=s['size'],slant='italic'))

        self.pack(expand=1, fill= tk.BOTH, side=tk.RIGHT)
        self['state'] = tk.DISABLED

    def write(self,text,newline = True):
     
        self['state'] = tk.NORMAL
        
        if self.get(1.0,'end').strip()=="": newline = False
        if newline: self.insert('end',"\n")
        
        self.delete(1.0,'end')
        self.insert('end', text)
        self['state'] = tk.DISABLED
    
    def add_tags(self,tags:list):
        
        self['state'] = tk.NORMAL

        for tag,start,end in tags:
            self.tag_add(tag,start,end)

        self['state'] = tk.DISABLED

    def mouseBind(self,key,show):
        self.bind(f'<{key}-Button>',lambda _:show(line = self.index("current")))