import tkinter as tk
from styles import titlebar as s


class titlebar(tk.Frame):
    def __init__(self,root:tk.Tk,file:str) -> None:
        tk.Frame.__init__(
            self,root,
            height=35,border=2, 
            relief=tk.FLAT,
            background=s["bg"])
        self.pack(fill=tk.X,side=tk.TOP)
        
        l = tk.Label(self,
        background=s['bg'],fg=s['fgfade'],
        text = file, font=s['font'])
        l.pack(expand=1,side=tk.LEFT,fill=tk.BOTH)
        self.title = l

        x = _Button(self, 'X',lambda:root.destroy(),activebg= 'red')
        x.pack(side=tk.RIGHT)

        mx = _Button(self,'[]',
        lambda:root.state('zoomed') if root.state() != 'zoomed' else root.state('normal'))
        mx.pack(side=tk.RIGHT)

        mn = _Button(self,'_',lambda:root.state('withdrawn'))
        mn.pack(side=tk.RIGHT)

        
class _Button(tk.Button):
    def __init__ (self,bar,text,command,width = 4,activebg = s['highlight']) -> None:
        super().__init__(
            bar,
            background=s['bg'],fg=s['fg'],
            text=text,relief=tk.FLAT,
            width = width,command = command,
            highlightbackground=activebg
        )
        self.bind('<Enter>',lambda _:self.onEnter(activebg))
        self.bind('<Leave>',lambda _:self.onLeave(s['bg']))

    def onEnter(self,activeBg):
        self.configure(background=activeBg)

    def onLeave(self,bg):
        self.configure(background=bg)