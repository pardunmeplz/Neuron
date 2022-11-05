import tkinter as tk
from styles import display as s
from Editor.tagList import tags
import tkhtmlview as tkh
import markdown

class Display(tkh.HTMLText):
    def __init__(self,root):
        tkh.HTMLText.__init__(self,root,height = 5,width = s['width'],)
        
        self.pack(expand=1, fill= tk.BOTH, side=tk.RIGHT)
        self['state'] = tk.DISABLED
    
    def write(self,text):
        html = markdown.markdown(text)
        self.set_html(html)


    def mouseBind(self,key,show):
        line = lambda :self.index("current")
        self.bind(f'<{key}-Button>',lambda _:show(line = line()))














class Dissplay(tk.Text):

    def __init__(self,root):
        tk.Text.__init__(
            self,root,
            height = 5,width = s['width'],
            bg = s['bg'], fg= s['fg'],
            border=30,relief =tk.FLAT,
            font= f"{s['font']} {s['size']}",
            wrap= tk.WORD
        )

        # configure tags
        for tag in tags.values():
            self.tag_config(tag.name, font = tag.display_font, foreground=tag.display_color)

        self.pack(expand=1, fill= tk.BOTH, side=tk.RIGHT)
        self['state'] = tk.DISABLED

    def write(self,text):
     
        self['state'] = tk.NORMAL

        self.rawtext = text

        self.delete(1.0,'end')
        self.insert('end', text)

        self['state'] = tk.DISABLED
    
    def add_tags(self,tagPositions:list):
        
        self['state'] = tk.NORMAL

        for tag,start,end in tagPositions:
            self.tag_add(tag,start,end)

        for name,start,end in tagPositions[::-1]:
            tags[name].clean_function(start,end,self.delete)
        
        self['state'] = tk.DISABLED