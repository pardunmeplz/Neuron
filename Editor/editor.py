import tkinter as tk
from tkinter import ttk
from styles import editor as s
import markdown as mdpy

class Editor(tk.Text):

    def __init__(self,root) -> None:
        self.frame = frame = tk.Frame(
            root,height=5,
            width=10,relief=tk.FLAT,
            background=s['bg'])
        frame.pack(expand=1, fill= tk.BOTH, side=tk.LEFT)

        tk.Text.__init__(
            self,frame,
            height=5, width=5,
            background=s['bg'], fg=s['fg'],
            relief =tk.FLAT,border = 30,
            font= f"{s['font']} {s['size']}",
            insertbackground=s['fg'],
            wrap= tk.WORD, undo=True
        )

        scroll = tk.Scrollbar(frame,command=self.yview,activebackground=s['bg'])
        scroll.pack(side = tk.RIGHT,fill=tk.Y)
        scroll.configure(bg=s['bg'],highlightcolor=s['fg'])
        self['yscrollcommand'] = scroll.set

        self.pack(expand=1, fill= tk.BOTH, side=tk.LEFT)

        # Editor Shortcuts
        self.bind('<Control-z>',lambda _:self.edit_undo())
        self.bind('<Control-y>',lambda _:self.edit_redo())

    def show(self, line = None):
        f = self.frame
        f.pack(expand=1, fill= tk.BOTH, side=tk.LEFT)
        
        if line == None: return
        line = float(float(line)//1)
        self.mark_set("insert",line)
        self.see(line)
    def syntax(self):
        MD = MDParser()
        
    
class MDParser(mdpy.Markdown):
    def __init__() -> None:
        super().__init__()