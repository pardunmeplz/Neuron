import display as d
import editor as edit
import tagsearch as t
import tkinter as tk
import ctypes

def getRoot():
        # gives better sharpness
        ctypes.windll.shcore.SetProcessDpiAwareness(True)
        
        root = tk.Tk()
        root.title("Neuron")
        root.geometry("1000x600")
        root.option_add('*Font', 'Courier 15')
        return root

def getEditor(root):
        editor = edit.Editor(root)
        disp = d.Display(root)
        return (editor,disp)

def render(editor,disp):
    text = editor.get_text()
    tags = t.get_tags(text)
    disp.write(text)
    disp.add_tags(tags)

# run
if __name__ == "__main__":

    root = getRoot()
    editor,disp = getEditor(root)
    editor.bind('<KeyRelease>',lambda _:render(editor,disp))
    root.mainloop()