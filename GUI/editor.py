import tkinter as tk
import tkinter.font as font
from styles import editor as s

class Editor:

    def __init__(self,root) -> None:
        w = tk.Text(root,
        height=5,
        width=10,
        border = 30,
        background=s['bg'],
        fg=s['fg'],
        relief =tk.FLAT,
        font= f"{s['font']} {s['size']}"
        )
        w.pack(expand=1, fill= tk.BOTH, side=tk.LEFT)
        self.widget = w
    
    def get_text(self):
        w = self.widget
        return w.get(1.0,'end')

    def bind(self,event,function):
        w = self.widget
        w.bind(event,function)