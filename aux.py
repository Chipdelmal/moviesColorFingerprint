# ############################################################################
# Color Fingerprint: aux.py
#   Auxiliary functions definitions
# ############################################################################


def rescaleColor(colorEightBit):
    colors = list(colorEightBit)
    colors.reverse()
    return [i / 255 for i in colors]


def fontFromOS(systemName):
    # Select font according to OS
    if systemName == 'Darwin':
        FONT = 'Avenir'
    elif systemName == 'Linux':
        FONT = 'Liberation Sans Narrow'
    else:
        FONT = 'Arial'
    return FONT


def defineFont(fontName, color='black', size=100, alpha=.06):
    fontDict = {
        'fontname': fontName,
        'color': color, 'weight': 'light',
        'size': size, 'alpha': alpha
        }
    return fontDict
