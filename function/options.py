# fonction cprint

def cprint(col, txt=1):
    Red = '\033[91m'
    blue = '\033[94m'
    yellow = '\033[93m'
    PURPLE = '\033[95m'
    cyan = '\033[96m'
    giskxo = '\033[97m'
    OrAnGe = '\033[48:2:255:165:0m'
    Green = '\033[92m'
    ENDC = '\033[0m'
    if col == 'Red' :
        colr = Red
    elif col == 'blue' :
        colr = blue
    elif col == 'yellow' :
        colr = yellow
    elif col == 'PURPLE' :
        colr = PURPLE
    elif col == 'cyan' :
        colr = cyan
    elif col == 'giskxo' :
        colr = giskxo
    elif col == 'OrAnGe' :
        colr = OrAnGe
    elif col == 'Green' :
        colr = Green
    else :
        txt = col
        colr = ENDC
    print(colr, txt, ENDC)