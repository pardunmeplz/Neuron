import re

tags = {
    'bold':'\*.+?\*',
    'italic':'_.+?_',
    'hlink':'<.+?>',
    'h1':'^#[\s].+$',
    'h2':'^##[\s].+$',
    'h3':'^###[\s].+$'
}

def get_tags(text):
    lines = text.split('\n')
    mytags = []
    for i, line in enumerate(lines):
        for tag, regex in tags.items():
            
            search = re.search(regex,line)
            if search != None:
                start,end = search.span()
                start = float(f'{i+1}.{start}')
                end = float(f'{i+1}.{end}')
                mytags.append((tag,start,end))
                
    return mytags

if __name__ == "__main__":
    text = "# Title \n## Subtitle \n This is text"
    print(get_tags(text))

    
