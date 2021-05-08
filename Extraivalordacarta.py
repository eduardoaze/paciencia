def extrai_valor (string):
    if len (string) > 2:
        return '10'
    elif string [0] == 'A':
        return 'A'
    elif string [0] == '2':
        return '2'
    elif string [0] == '3':
        return '3'
    elif string [0] == '4':
        return '4'
    elif string [0] == '5':
        return '5'
    elif string [0] == '6':
        return '6'
    elif string [0] == '7':
        return '7'
    elif string [0] == '8':
        return '8'
    elif string [0] == '9':
        return '9'
    elif string [0] == '10':
        return '10'
    elif string [0] == 'J':
        return 'J'
    elif string [0] == 'Q':
        return 'Q'
    else:
        return 'K'