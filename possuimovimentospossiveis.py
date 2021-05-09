def possui_movimentos_possiveis (baralho):
    naipes = []
    numeros =[]
    for carta in baralho:
        if len(carta) == 2:
            if carta [0] == 'J':
                naipes.append (carta [1])
                numeros.append ('11')
            if carta [0] == 'Q':
                naipes.append (carta [1])
                numeros.append ('12')
            if carta [0] == 'K':
                naipes.append (carta [1])
                numeros.append ('13')
            if carta [0] == 'A':
                naipes.append (carta [1])
                numeros.append ('1')
            if carta[0] != 'A' and carta[0] != 'J' and carta[0] != 'Q' and carta[0] != 'K':
                naipes.append (carta[1])
                numeros.append (carta [0])
        else:
            naipes.append  (carta [2])
            numeros.append (10)
    i = len(baralho) - 1
    movimentos = 0
    while i >= 1:
        if i >= 4:
            if naipes[i] == naipes [i - 3]:
                movimentos += 1
        if numeros [i] == numeros [i - 3]:
            movimentos += 1
        else:
            if naipes [i] == naipes [i - 1]:
                movimentos += 1
            if numeros [i] == numeros [i - 1]:
                movimentos += 1
        i -= 1
    if movimentos != 0:
        return True
    else:
        return False