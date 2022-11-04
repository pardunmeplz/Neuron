import display as d
import titlebar as title
import editor as edit
import tagsearch as t
import tkinter as tk
import ctypes


class window(tk.Tk):
        def __init__(self):
                tk.Tk.__init__(self)

                # gives better sharpness
                ctypes.windll.shcore.SetProcessDpiAwareness(True)
                
                self.title("Neuron")
                self.geometry("1000x600")
                self.option_add('*Font', 'Courier 15')

                self.overrideredirect(True) # get rid of titlebar
                self._xOffset = 0
                self._yOffset = 0


        def getEditor(self):
                bar =  title.titlebar(self)
                editor = edit.Editor(self)
                disp = d.Display(self)
                self.editView =  (editor,disp,bar)
                
                editor.bind('<KeyRelease>',lambda _:self.render())
                self.bind('<Control-Left>',lambda _:editor.hide())
                self.bind('<Control-Right>',lambda _:editor.show())
                disp.mouseBind('Control',editor.show)

                bar.bind('<Button-1>',self._onClick)
                bar.bind('<B1-Motion>',self._onDrag)

        #def getMenu(root):

        def render(self):
                editor,disp,_ = self.editView
                text = editor.get_text()
                tags = t.get_tags(text)
                disp.write(text)
                disp.add_tags(tags)
                editor.add_tags(tags)

        def _onClick(self,event):
                self._xOffset = event.x
                self._yOffset = event.y

        def _onDrag(self,_):
                x = self.winfo_pointerx() - self._xOffset
                y = self.winfo_pointery() - self._yOffset
                self.geometry('+{x}+{y}'.format(x=x,y=y))



# run
if __name__ == "__main__":

    root = window()
    root.getEditor()
    root.mainloop()
