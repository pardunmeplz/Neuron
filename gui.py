import display as d

import tkinter as tk
import ctypes

# gives better sharpness
ctypes.windll.shcore.SetProcessDpiAwareness(True)

#setting up root

text = "# Hello World"

root = tk.Tk()
root.title("Neuron")
root.geometry("1000x600")
root.option_add('*Font', 'Courier 15')
disp = d.Display(root)
disp.write("# Hello World")

root.mainloop()