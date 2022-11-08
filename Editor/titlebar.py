import tkinter as tk
from styles import titlebar as s
import Editor.dropdown as dropdown


class titlebar(tk.Frame):
    def __init__(self,root:tk.Tk,file:str) -> None:
        tk.Frame.__init__(
            self,root,
            height=35,border=2, 
            relief=tk.FLAT,
            background=s["bg"])
        self.pack(fill=tk.X,side=tk.TOP)
        
        # menu buttons
        logo = tk.Label(self, background=s['bg'],fg='#63b0f2',
        text = ' N ', font = f"{s['font']} 16 bold")
        logo.pack(side=tk.LEFT)

        _mButton(self,'File',dropdown.fileDrop(self,root))
        _mButton(self,'Edit',dropdown.editDrop(self,root))

        
        # title label
        self.title = tk.Label(
        self,text = file, 
        background=s['bg'],fg=s['fgfade'],
        font=s['font'])
        
        self.title.pack(expand=1,side=tk.LEFT,fill=tk.BOTH)

        # window buttons
        _Button(self, 'X',lambda:root.destroy(),activebg= 'red',activefg='white')

        _Button(self,'[]',lambda:root.state('zoomed') if root.state() != 'zoomed' else root.state('normal'))
        
        _Button(self,'_',lambda:root.state('withdrawn'))

        
class _Button(tk.Button):
    def __init__ (self,bar,text,command,
    activebg = s['highlight'], activefg = s['fg']) -> None:
        super().__init__(
            bar,
            background=s['bg'],fg=s['fg'],
            text=text,relief=tk.FLAT,
            width = 4,command = command,
            highlightbackground=activebg,
            bd = 0
        )
        self.bind('<Enter>',lambda _:self.onEnter(activebg,activefg))
        self.bind('<Leave>',lambda _:self.onLeave())
        self.pack(side=tk.RIGHT)

    def onEnter(self,activebg,activefg):
        self.configure(background=activebg,foreground=activefg)

    def onLeave(self):
        self.configure(background=s['bg'],foreground=s['fg'])

class _mButton(_Button):
    def __init__(self, bar, text, menu) -> None:
        super().__init__(
            bar, text,
            lambda :menu.tk_popup(x=self.winfo_rootx(),y=self.winfo_rooty()),
            activefg = s['highlight'])
        self.pack(side = tk.LEFT)
        self.config(foreground=s['fgfade'],font = f"{s['font']} {s['size']-2}",width=5,
        activebackground=s['highlight'], activeforeground=s['fgfade'])
    
    def onLeave(self):
        super().onLeave()
        self.configure(foreground=s['fgfade'])

