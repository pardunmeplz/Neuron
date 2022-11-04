import tkinter as tk
import tkinter.font as font
from tkinter import ttk

def rgbToHex(rgb):
    return '#'+'%02x%02x%02x' % rgb

styles = dict(
    bg=rgbToHex((40, 40, 40)),
    fg=rgbToHex((230, 230, 230)),
    size=15,
    font = 'courier'
)

class Editor:

    def __init__(self,root) -> None:
        w = tk.Text(root,
        height=5,
        width=10,
        border = 30,
        background=styles['bg'],
        fg=styles['fg'],
        relief =tk.FLAT,
        font= f"{styles['font']} {styles['size']}"
        )
        w.pack(expand=1, fill= tk.BOTH, side=tk.LEFT)
        self.widget = w