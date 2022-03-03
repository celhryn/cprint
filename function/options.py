# fonction cprint

__name__ = '__main__'

class colors :
    rouge = '\033[91m'
    bleu = '\033[94m'
    jaune = '\033[93m'
    violet = '\033[95m'
    cyan = '\033[96m'
    blanc = '\033[97m'
    orange = '\033[91m'
    vert = '\033[92m'
    ENDC = '\033[0m'

def cprint(*arg, reste):
    class colors :
        rouge = '\033[91m'
        bleu = '\033[94m'
        jaune = '\033[93m'
        violet = '\033[95m'
        cyan = '\033[96m'
        blanc = '\033[97m'
        orange = '\033[91m'
        vert = '\033[92m'
        ENDC = '\033[0m'
    if arg == 'Red' :
        print(f"{colors.rouge}", reste, "{colors.ENDC}")
    elif arg == 'blue' :
        print(f"{colors.bleu}", reste, "{colors.ENDC}")
    elif arg == 'yellow' :
        print(f"{colors.jaune}", reste, "{colors.ENDC}")
    elif arg == 'PURPLE' :
        print(f"{colors.violet}", reste, "{colors.ENDC}")
    elif arg == 'cyan' :
        print(f"{colors.cyan}", reste, "{colors.ENDC}")
    elif arg == 'giskxo' :
        print(f"{colors.blanc}", reste, "{colors.ENDC}")
    elif arg == 'OrAnGe' :
        print(f"{colors.orange}", reste, "{colors.ENDC}")
    elif arg == 'Green':
        print(f"{colors.vert}", reste, "{colors.ENDC}")
    else :
        print(f"{colors.ENDC}", reste, "{colors.ENDC}")