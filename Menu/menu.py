import tkinter as tk
from tkinter import filedialog
from tkinter import font
from styles import menu as s

class Menu(tk.Frame):
    def __init__(self,root) -> None:
        tk.Frame.__init__(self,root,
        relief = tk.FLAT, border = 30,
        background=s['bg'])
        self.pack(expand=1,fill=tk.BOTH)

        l = tk.Label(self, text="Neuron",
            background=s['bg'],fg=s['fg'],
            font=font.Font(size=s['titleSize']))

        l.pack( fill=tk.X, side = tk.BOTTOM)
        
        top = tk.Frame(self, background=s['bg'])
        
        top.pack(side=tk.TOP, fill= tk.X)

        x = tk.Button(top,
            background=s['bg'],fg=s['fg'],
            text='X',relief=tk.FLAT,
            command=lambda:root.destroy())
        x.pack(side=tk.RIGHT)

        op = tk.Button(self,
            background=s['bg'],fg=s['fg'],
            text='...Open',relief=tk.FLAT,
            command=lambda:self.browseFiles() and root.getEditor())
        op.pack(expand = 1, side=tk.LEFT)
        self.op = op
    
    def browseFiles(self,*args):
        filename = filedialog.askopenfilename(
            initialdir = "/",title = "Select a File",
            filetypes = (("Markdown","*.MD*"),
                        ("all files","*.*")))
        if filename.strip() == "": return False
        
        self.filename = filename
        self.op['text'] = f'...{filename[-15:]}'
        return True