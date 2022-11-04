
def rgbToHex(rgb):
    return '#'+'%02x%02x%02x' % rgb

display = dict(
bg = rgbToHex((60, 60, 60)),
fg = rgbToHex((200, 200, 200)),
font = 'Calibri',
width = 10,

# Font Sizes
size = 15,
h1Size = 40,
h2Size = 30,
h3Size = 20,

# font Colors
h1Color = rgbToHex((240, 240, 240)),
h2Color = rgbToHex((200, 200, 200)),
h3Color = rgbToHex((160, 160, 160))
)


editor = dict(
    bg=rgbToHex((40, 40, 40)),
    fg=rgbToHex((230, 230, 230)),
    size=15,
    font = 'courier'
)
