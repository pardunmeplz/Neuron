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
            insertbackground=s['fg'],
            wrap= tk.WORD
        )
        self.pack(expand=1, fill= tk.BOTH, side=tk.LEFT)

    def show(self, line = None):
        w = self
        w.pack(expand=1, fill= tk.BOTH, side=tk.LEFT)
        
        if line == None: return
        line = float(float(line)//1)
        w.mark_set("insert",line)
        w.see(line)