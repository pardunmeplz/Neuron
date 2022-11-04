import tkinter as tk
import tkinter.font as font
from styles import editor as s

class Editor:

    def __init__(self,root) -> None:
        w = tk.Text(
        root,
        height=5, width=10,
        background=s['bg'], fg=s['fg'],
        relief =tk.FLAT,border = 30,
        font= f"{s['font']} {s['size']}",
        insertbackground=s['fg']
        )
        
        w.pack(expand=1, fill= tk.BOTH, side=tk.LEFT)
        self.widget = w

        w.tag_config('h1', foreground=s['hColor'])
        w.tag_config('h2', foreground=s['hColor'])
        w.tag_config('h3', foreground=s['hColor'])

        w.tag_config('bold', foreground=s['bldColor'])
        w.tag_config('italic', foreground=s['itlColor'])
    
    def get_text(self):
        w = self.widget
        return w.get(1.0,'end')

    def bind(self,event,fn):
        w = self.widget
        w.bind(event,fn)

    def add_tags(self,tags:list):
        w = self.widget        
        for tag,start,end in tags:
            w.tag_add(tag,start,end)
    
    def hide(self):
        w = self.widget
        w.pack_forget()

    def show(self, line = None):
        w = self.widget
        w.pack(expand=1, fill= tk.BOTH, side=tk.LEFT)
        
        if line == None: return
        w.mark_set("insert",line)
        w.see(line)