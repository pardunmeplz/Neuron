import tkinter as tk
from styles import titlebar as s
from root import window

class drop(tk.Menu):
    def __init__(self, master, commands:dict) -> None:
        super().__init__(
            master,
            background=s['bg'],foreground=s['fgfade'],
            font=f"{s['font']} {s['size']}",
            borderwidth=0,
            activebackground= s['highlight'],
            activeforeground= s['fg'],
            tearoff=0
            )
        for label,command in commands.items():
            self.add_command(label=label,command=command)


def fileDrop(master,root:window):
    commands = {
        'New':lambda:None,
        'Open':lambda:None,
        'Save':lambda:root.saveFile(),
        'Close':lambda:root.closeFile(),
        'Exit':lambda:root.destroy()}
    return drop(master,commands)

def editDrop(master, root:window):
    commands = {
        'Undo':lambda:root.editView[0].edit_undo(),
        'Redo':lambda:root.editView[0].edit_redo()
    }
    return drop(master,commands)