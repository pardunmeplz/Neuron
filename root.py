import Editor.display as d
import Editor.titlebar as title
import Editor.editor as edit
import Menu.menu as m
import tkinter as tk
import ctypes
from styles import root as s

class window(tk.Tk):
        def __init__(self) -> None:
                tk.Tk.__init__(self)

                # gives better sharpness
                ctypes.windll.shcore.SetProcessDpiAwareness(True)
                
                self.title("Neuron")

                self.option_add('*Font', 'Courier 15')

                self.overrideredirect(True) # get rid of titlebar
                self._xOffset = 0
                self._yOffset = 0

        def getEditor(self) -> None:
                file = self.destroyMenu()
                bar =  title.titlebar(self,file)
                editor = edit.Editor(self)
                disp = d.Display(self)
                self.editView =  (editor,disp,bar)

                editor.bind('<KeyRelease>',lambda _:self.render())
                editor.bind('<Control-s>',lambda _:self.saveFile())
                self.bind('<Control-Left>',lambda _:editor.pack_forget())
                self.bind('<Control-Right>',lambda _:editor.show())
                disp.mouseBind('Control',editor.show)

                bar.title.bind('<Button-1>',self._onClick)
                bar.title.bind('<B1-Motion>',self._onDrag)
                
                self.w , self. h = s['editor_size']
                self.geometry(f"{self.w}x{self.h}")

                self.file = file
                file = open(file, mode = 'r')
                text = file.read()
                file.close()

                editor.insert('end',text)
                self.render()

        
        def saveFile(self) -> None:
                editor, _ , _ = self.editView
                text = editor.get(1.0,'end')
                file = open(self.file, mode='w')
                file.write(text)
                file.close()
        
        def destroyEditor(self) -> None:
                editor, disp, bar = self.editView
                editor.destroy()
                disp.destroy()
                bar.destroy()
                del self.editView

        def getMenu(self) -> None:
                menu = m.Menu(self)
                self.menu = menu

                menu.bind('<Button-1>',self._onClick)
                menu.bind('<B1-Motion>',self._onDrag)

                self.w , self. h = s['menu_size']
                self.geometry(f"{self.w}x{self.h}")

                w, h = self.winfo_screenwidth(), self.winfo_screenheight()
                self.geometry(f"+{(w - self.w)//2}+{(h - self.h)//2}")
        
        def destroyMenu(self) -> None:
                file = self.menu.filename
                self.menu.destroy()
                del self.menu
                return file

        def render(self) -> None:
                editor,disp,_ = self.editView
                text = editor.get(0.1,'end')
                disp.write(text)

        def _onClick(self,event) -> None:
                self._xOffset = event.x
                self._yOffset = event.y

        def _onDrag(self,_) -> None:
                x = self.winfo_pointerx() - self._xOffset
                y = self.winfo_pointery() - self._yOffset
                self.geometry('+{x}+{y}'.format(x=x,y=y))

# run
if __name__ == "__main__":

    root = window()
    root.getMenu()
    root.mainloop()
