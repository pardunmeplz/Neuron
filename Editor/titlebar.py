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
        
        # menu buttons
        logo = tk.Label(self, background=s['bg'],fg=s['fg'],
        text = ' N ', font = f"{s['font']} 16 bold")
        logo.pack(side=tk.LEFT)

        _mButton(self,'File',lambda:None)

        # title label
        self.title = tk.Label(
        self,text = file, 
        background=s['bg'],fg=s['fgfade'],
        font=s['font'])
        
        self.title.pack(expand=1,side=tk.LEFT,fill=tk.BOTH)

        # window buttons
        _Button(self, 'X',lambda:root.destroy(),activebg= 'red')

        _Button(self,'[]',lambda:root.state('zoomed') if root.state() != 'zoomed' else root.state('normal'))
        
        _Button(self,'_',lambda:root.state('withdrawn'))

        
class _Button(tk.Button):
    def __init__ (self,bar,text,command,activebg = s['highlight']) -> None:
        super().__init__(
            bar,
            background=s['bg'],fg=s['fg'],
            text=text,relief=tk.FLAT,
            width = 4,command = command,
            highlightbackground=activebg
        )
        self.bind('<Enter>',lambda _:self.onEnter(activebg))
        self.bind('<Leave>',lambda _:self.onLeave(s['bg']))
        self.pack(side=tk.RIGHT)

    def onEnter(self,activeBg):
        self.configure(background=activeBg)

    def onLeave(self,bg):
        self.configure(background=bg)

class _mButton(_Button):
    def __init__(self, bar, text, command) -> None:
        super().__init__(bar, text, command, s['highlight'])
        self.pack(side = tk.LEFT)
        self.config(foreground=s['fgfade'],font = f"{s['font']} {s['size']-2}",width=5)

    
    def onEnter(self, activeBg):
        super().onEnter(activeBg)
        self.configure(foreground=s['fg'])
    
    def onLeave(self, bg):
        super().onLeave(bg)
        self.configure(foreground=s['fgfade'])