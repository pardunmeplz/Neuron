
def rgbToHex(rgb):
    return '#'+'%02x%02x%02x' % rgb

display = dict(
bg = rgbToHex((60, 60, 60)),
fg = rgbToHex((200, 200, 200)),
font = 'Calibri',
width = 10,

# Font Sizes
size = 12,
h1Size = 26,
h2Size = 20,
h3Size = 16,

# font Colors
h1Color = rgbToHex((240, 240, 240)),
h2Color = rgbToHex((200, 200, 200)),
h3Color = rgbToHex((160, 160, 160))
)


editor = dict(
    bg=rgbToHex((40, 40, 40)),
    fg=rgbToHex((230, 230, 230)),
    size=12,
    font = 'Consolas',

    itlColor ='#da2fe0',
    bldColor='#f2d95e',
    hColor='#fc5c4e'
)

titlebar = dict(
    bg = '#3f3f3f',
    fg = '#b7b7b7'
)

menu =dict(
    bg = '#3f3f3f',
    fg = '#b7b7b7',
    titleSize = 25
)
