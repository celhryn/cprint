# fonction cprint
def cprint(col, txt=1):
    Red, blue, yellow, PURPLE, cyan, giskxo, OrAnGe, Green, ENDC = '\033[91m', '\033[94m', '\033[93m', '\033[95m', '\033[96m', '\033[97m', '\033[33m', '\033[92m', '\033[0m'
    if col.lower() == 'red' :
        colr = Red
    elif col.lower() == 'blue' :
        colr = blue
    elif col.lower() == 'yellow'  :
        colr = yellow
    elif col.lower() == 'purple' :
        colr = PURPLE
    elif col.lower() == 'cyan' :
        colr = cyan
    elif col.lower() == 'giskxo' :
        colr = giskxo
    elif col.lower() == 'orange' :
        colr = OrAnGe
    elif col.lower() == 'green' :
        colr = Green
    else :
        txt = col
        colr = ENDC
    print(colr, txt, ENDC)