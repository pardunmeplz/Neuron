import tkinter as tk
from styles import editor as s

class Editor(tk.Text):

    def __init__(self,root) -> None:
        tk.Text.__init__(
            self,root,
            height=5, width=10,
            background=s['bg'], fg=s['fg'],
            relief =tk.FLAT,border = 30,
            font= f"{s['font']} {s['size']}",
            insertbackground=s['fg']
        )
        
        self.pack(expand=1, fill= tk.BOTH, side=tk.LEFT)

        self.tag_config('h1', foreground=s['hColor'])
        self.tag_config('h2', foreground=s['hColor'])
        self.tag_config('h3', foreground=s['hColor'])

        self.tag_config('bold', foreground=s['bldColor'])
        self.tag_config('italic', foreground=s['itlColor'])

    def add_tags(self,tags:list):
        all = ['h1','h2','h3','bold','italic']
        for tag in all:
            self.tag_remove(tag,0.1,'end')
        for tag,start,end in tags:
            self.tag_add(tag,start,end)

    def show(self, line = None):
        w = self
        w.pack(expand=1, fill= tk.BOTH, side=tk.LEFT)
        
        if line == None: return
        line = float(float(line)//1)
        w.mark_set("insert",line)
        w.see(line)