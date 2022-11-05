import tkinter as tk
from styles import editor as s
from Tags.tagList import tags

class Editor(tk.Text):

    def __init__(self,root) -> None:
        tk.Text.__init__(
            self,root,
            height=5, width=10,
            background=s['bg'], fg=s['fg'],
            relief =tk.FLAT,border = 30,
            font= f"{s['font']} {s['size']}",
            insertbackground=s['fg'],
            wrap= tk.WORD
        )
        
        self.pack(expand=1, fill= tk.BOTH, side=tk.LEFT)
        for tag in tags.values():
            self.tag_config(tag.name, foreground=tag.editor_color)

    def add_tags(self,tagPositions:list):
        for name in tags:
            self.tag_remove(name,0.1,'end')
            
        for name,start,end in tagPositions:
            self.tag_add(name,start,end)

    def show(self, line = None):
        w = self
        w.pack(expand=1, fill= tk.BOTH, side=tk.LEFT)
        
        if line == None: return
        line = float(float(line)//1)
        w.mark_set("insert",line)
        w.see(line)