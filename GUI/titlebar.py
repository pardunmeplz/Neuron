import tkinter as tk
from styles import titlebar as s


class titlebar(tk.Frame):
    def __init__(self,root:tk.Tk) -> None:
        tk.Frame.__init__(
            self,root,
            height=35,border=2, 
            relief=tk.FLAT,
            background=s["bg"])
        self.pack(fill=tk.X,side=tk.TOP)
        
        x = tk.Button(self,
        background=s['bg'],fg=s['fg'],
        text='X',relief=tk.FLAT,
        command=lambda:root.destroy())
        x.pack(side=tk.RIGHT)

        mx = tk.Button(self,
        background=s['bg'],fg=s['fg'],
        text='[]',relief=tk.FLAT,
        command=lambda:root.state('zoomed') if root.state() != 'zoomed' else root.state('normal'))
        mx.pack(side=tk.RIGHT)

        
        