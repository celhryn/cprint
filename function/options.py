# fonction cprint
def cprint(col, txt=1):
    if col.lower() == 'red' :
        colr = \033[91m
    elif col.lower() == 'blue' :
        colr = \033[94m
    elif col.lower() == 'yellow'  :
        colr = \033[93m
    elif col.lower() == 'purple' :
        colr = \033[95m
    elif col.lower() == 'cyan' :
        colr = \033[96m
    elif col.lower() == 'giskxo' :
        colr = \033[97m
    elif col.lower() == 'orange' :
        colr = \033[33m
    elif col.lower() == 'green' :
        colr = \033[92m
    elif txt == 1 :
        txt = col
        colr = \033[0m
    else :
        colr = \033[0m
    print(colr, txt, ENDC)
