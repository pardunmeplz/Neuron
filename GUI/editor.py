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
    
    def get_text(self):
        w = self
        return w.get(1.0,'end')

    def add_tags(self,tags:list):
        w = self        
        for tag,start,end in tags:
            w.tag_add(tag,start,end)
    
    def hide(self):
        w = self
        w.pack_forget()

    def show(self, line = None):
        w = self
        w.pack(expand=1, fill= tk.BOTH, side=tk.LEFT)
        
        if line == None: return
        line = float(float(line)//1)
        w.mark_set("insert",line)
        w.see(line)