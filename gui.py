import display as d
import tagsearch as t
import tkinter as tk
import ctypes

# gives better sharpness
ctypes.windll.shcore.SetProcessDpiAwareness(True)


# text input
text = "# Hello World\n## This is a subtitle\nthis be plain text"
tags = t.get_tags(text)
print(tags)
# setting up root
root = tk.Tk()
root.title("Neuron")
root.geometry("1000x600")
root.option_add('*Font', 'Courier 15')

#setting a display widget
disp = d.Display(root)
disp.write(text)
disp.add_tags(tags)

# run
root.mainloop()