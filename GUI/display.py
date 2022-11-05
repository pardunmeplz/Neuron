import tkinter as tk
import tkinter.font as font
from styles import display as s

class Display(tk.Text):

    def __init__(self,root):
        tk.Text.__init__(
            self,root,
            height = 5,width = s['width'],
            bg = s['bg'], fg= s['fg'],
            border=30,relief =tk.FLAT,
            font= f"{s['font']} {s['size']}"
        )

        # configure tags
        self.tag_config('h1', font=f"{s['font']} {s['h1Size']}",foreground=s['h1Color'])
        self.tag_config('h2', font=f"{s['font']} {s['h2Size']}",foreground=s['h2Color'])
        self.tag_config('h3', font=f"{s['font']} {s['h3Size']}",foreground=s['h3Color'])

        self.tag_config('bold', font=font.Font(size=s['size'],weight='bold'))
        self.tag_config('italic', font=font.Font(size=s['size'],slant='italic'))

        self.tag_config('hlink', foreground=s['hlinkColor'])

        self.pack(expand=1, fill= tk.BOTH, side=tk.RIGHT)
        self['state'] = tk.DISABLED

    def write(self,text, tags):
     
        self['state'] = tk.NORMAL

        self.delete(1.0,'end')
        self.insert('end', text)

        clean = {
                'h1':lambda start, end:self.delete(start,start+0.2),
                'h2':lambda start, end:self.delete(start,start+0.3),
                'h3':lambda start, end:self.delete(start,start+0.4),
                'bold':lambda start, end:self.delete(end-0.1) or self.delete(start),
                'italic':lambda start, end:self.delete(start) or self.delete(end-0.1),
                'hlink':lambda start, end:self.delete(start) or self.delete(end - 0.1)
                }

        for tag,start,end in tags:
            clean[tag](start,end)

        self['state'] = tk.DISABLED
    
    def add_tags(self,tags:list):
        
        self['state'] = tk.NORMAL

        for tag,start,end in tags:
            self.tag_add(tag,start,end)

        self['state'] = tk.DISABLED

    def mouseBind(self,key,show):
        line = lambda :self.index("current")
        self.bind(f'<{key}-Button>',lambda _:show(line = line()))