def lista_movimentos_possiveis (baralho, carta_selecionada):
    numero = []
    naipe = []
    for carta in baralho:
        if len(carta) == 2:
            numero.append (carta [0])
            naipe.append (carta [1])
        else:
            numero.append (10)
            naipe.append (carta [2])
    movimentos = []
    if carta_selecionada == 0:
        return []
    elif carta_selecionada >= 3:
            if naipe[carta_selecionada] == naipe [carta_selecionada - 1 ] :
                movimentos.append (1)
            if naipe [carta_selecionada] == naipe [carta_selecionada - 3]:
                movimentos.append (3)
            if numero [carta_selecionada] == numero [carta_selecionada - 1]:
                movimentos.append (1)
            if numero [carta_selecionada] == numero [carta_selecionada -3]:     
                movimentos.append (3)
    else:
        if naipe[carta_selecionada] == naipe [carta_selecionada - 1 ] :
            movimentos.append (1)
        if numero [carta_selecionada] == numero [carta_selecionada - 1]:
            movimentos.append (1)
    return movimentos