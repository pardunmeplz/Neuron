import re
from Editor.tagList import tags

def get_tags(text):

    lines = text.split('\n')
    tagPositions = []
    print()
        
    allregex = ""
    for tag in tags.values():
            allregex += f'{tag.regex}'+'|'
    allregex = allregex[:-1]
    
    allregex =  '(\n)(#{1}\s)(.*)|(\n)(#{1}\s)(.*)'
    search = re.split(allregex,'\n'+text)
    if search != []:print(search)
                
    return tagPositions

    
