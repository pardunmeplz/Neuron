import display as d
import editor as edit
import tagsearch as t
import tkinter as tk
from tkinter import ttk
import ctypes

# gives better sharpness
ctypes.windll.shcore.SetProcessDpiAwareness(True)

# text input
text = "# Hello World\n## This is a subtitle\nthis be *plain* _text_"
tags = t.get_tags(text)

# setting up root
root = tk.Tk()
root.title("Neuron")
root.geometry("1000x600")
root.option_add('*Font', 'Courier 15')

editor = edit.Editor(root)

#setting a display widget
disp = d.Display(root)
disp.write(text)
disp.add_tags(tags)



# run
root.mainloop()