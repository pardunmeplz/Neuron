import tkinter as tk
import tkinter.font as font
from styles import display as s
from Tags.tagList import tags

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
        for tag in tags.values():
            self.tag_config(tag.name, font = tag.display_font, foreground=tag.display_color)

        self.pack(expand=1, fill= tk.BOTH, side=tk.RIGHT)
        self['state'] = tk.DISABLED

    def write(self,text, tagPositions):
     
        self['state'] = tk.NORMAL

        self.delete(1.0,'end')
        self.insert('end', text)

        for name,start,end in tagPositions:
            tags[name].clean_function(start,end,self.delete)

        self['state'] = tk.DISABLED
    
    def add_tags(self,tagPositions:list):
        
        self['state'] = tk.NORMAL

        for tag,start,end in tagPositions:
            self.tag_add(tag,start,end)

        self['state'] = tk.DISABLED

    def mouseBind(self,key,show):
        line = lambda :self.index("current")
        self.bind(f'<{key}-Button>',lambda _:show(line = line()))