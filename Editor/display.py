import tkinter as tk
from styles import display as s
import tkhtmlview as tkh
import markdown

# setting default values of tkhtmlview module
default_config = tkh.html_parser.DEFAULT_STACK[tkh.html_parser.WCfg.KEY]
default_config[tkh.html_parser.WCfg.FOREGROUND] = [("__DEFAULT__", s['fg'])]

default_font = tkh.html_parser.DEFAULT_STACK[tkh.html_parser.Fnt.KEY]
default_font[tkh.html_parser.Fnt.SIZE] = [("__DEFAULT__",s['size'])]

class Display(tkh.HTMLText):
    def __init__(self,root):
        tkh.HTMLText.__init__(
            self,root,
            height = 5,width = s['width'],
            border = 30,relief=tk.FLAT)
        
        self.pack(expand=1, fill= tk.BOTH, side=tk.RIGHT)
        self['state'] = tk.DISABLED
        self.config(background=s['bg'],font=f"{s['font']} {s['size']}")

        self.html_parser = _html_parser()

    
    def write(self,text):
        self['state'] = tk.NORMAL
        html = markdown.markdown(text)
        self.set_html(html)
        self['state'] = tk.DISABLED

    def mouseBind(self,key,show):
        line = lambda :self.index("current")
        self.bind(f'<{key}-Button>',lambda _:show(line = line()))

class _html_parser(tkh.html_parser.HTMLTextParser):
    def __init__(self):
        super().__init__()
    
    def _parse_styles(self, tag, attrs):
        super()._parse_styles(tag, attrs)
        HTML = tkh.html_parser.HTML
        WCfg = tkh.html_parser.WCfg
        Fnt = tkh.html_parser.Fnt

        # overwrite styles for any tags here

        if tag ==  HTML.Tag.A and attrs[HTML.Attrs.HREF]:
            self._stack_add(tag, WCfg.FOREGROUND, s['hlinkColor'])
        
        elif tag == HTML.Tag.H1:
            self._stack_add(tag,WCfg.FOREGROUND, s['h1Color'])
