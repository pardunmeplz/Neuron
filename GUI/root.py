import display as d
import titlebar as title
import editor as edit
import tagsearch as t
import menu as m
import tkinter as tk
import ctypes


class window(tk.Tk):
        def __init__(self):
                tk.Tk.__init__(self)

                # gives better sharpness
                ctypes.windll.shcore.SetProcessDpiAwareness(True)
                
                self.title("Neuron")

                self.option_add('*Font', 'Courier 15')

                self.overrideredirect(True) # get rid of titlebar
                self._xOffset = 0
                self._yOffset = 0


        def getEditor(self):
                file = self.destroyMenu()
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
                
                self.w , self. h = 1000, 600
                self.geometry(f"{self.w}x{self.h}")
        
        def destroyEditor(self):
                editor, disp, bar = self.editView
                editor.destroy()
                disp.destroy()
                bar.destroy()
                del self.editView

        def getMenu(self):
                menu = m.Menu(self)
                self.menu = menu

                menu.bind('<Button-1>',self._onClick)
                menu.bind('<B1-Motion>',self._onDrag)

                self.w , self. h = 600, 400
                self.geometry(f"{self.w}x{self.h}")

                w, h = self.winfo_screenwidth(), self.winfo_screenheight()
                self.geometry(f"+{(w - self.w)//2}+{(h - self.h)//2}")
        
        def destroyMenu(self) -> None:
                file = self.menu.filename
                self.menu.destroy()
                del self.menu
                return file

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
    root.getMenu()
    root.mainloop()
