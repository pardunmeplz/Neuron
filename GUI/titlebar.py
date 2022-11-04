import tkinter as tk
from tkinter import ttk
from styles import titlebar as s


class titlebar:
    def __init__(self,root) -> None:
        w = tk.Frame(root,height=35,border=2, relief=tk.FLAT,
        background=s["bg"])
        w.pack(fill=tk.X,side=tk.TOP)
        self.widget = w

        l = tk.Label(w,
        fg=s['fg'],background=s['bg'],
        text="nav buttons to come here")
        l.pack(side=tk.LEFT)
        pass