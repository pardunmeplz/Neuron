import re
from Tags.tagList import tags

def get_tags(text):

    lines = text.split('\n')
    tagPositions = []
    
    for i, line in enumerate(lines):
    
        for tag in tags.values():
            
            search = re.search(tag.regex,line)
            if search != None:
                start,end = search.span()
                start = float(f'{i+1}.{start}')
                end = float(f'{i+1}.{end}')
                
                tagPositions.append((tag.name,start,end))
                
    return tagPositions

if __name__ == "__main__":
    text = "# Title \n## Subtitle \n This is text"
    print(get_tags(text))

    
