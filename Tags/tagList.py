import styles as s

class tag:
    def __init__(self,name,regex,clean_function,editor_color,display_font = None,display_color = None):
        self.name = name,
        self.regex = regex

        self.clean_function = clean_function
        self.display_font = display_font
        self.display_color = display_color

        self.editor_color = editor_color

bold = tag(
    'bold', '\*.+?\*',
    lambda start, end, delete:delete(start) or delete(end - 0.1),
    s.editor['bldColor'],
    display_font=f"{s.display['font']} {s.display['size']} bold"
    )

italic = tag(
    'italic','_.+?_',
    lambda start, end, delete:delete(start) or delete(end-0.1),
    s.editor['itlColor'],
    display_font=f"{s.display['font']} {s.display['size']} italic"
    )

hlink = tag(
    'hlink','<.+?>',
    lambda start, end,delete:delete(start) or delete(end - 0.1),
    s.editor['hlinkColor'],
    display_color=s.display['hlinkColor']
    )

h1 = tag(
    'h1','^#[\s].+$',
    lambda start, end,delete:delete(start,start+0.2),
    s.editor['hColor'],
    display_color=s.display['h1Color'],
    display_font=f"{s.display['font']} {s.display['h1Size']}"
    )

h2 = tag(
    'h2','^##[\s].+$',
    lambda start, end,delete:delete(start,start+0.3),
    s.editor['hColor'],
    display_color=s.display['h2Color'],
    display_font=f"{s.display['font']} {s.display['h2Size']}"
    )

h3 = tag(
    'h3','^###[\s].+$',
    lambda start, end,delete:delete(start,start+0.4),
    s.editor['hColor'],
    display_color=s.display['h3Color'],
    display_font=f"{s.display['font']} {s.display['h3Size']}"
    )

tags = {
    bold.name:bold,
    italic.name:italic,
    hlink.name:hlink,
    h1.name:h1,
    h2.name:h2,
    h3.name:h3}
        