print ('Paciência Acordeão') 
print ('==================') 
print('')
print ('Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.') 
print('')
print ('Existem apenas dois movimentos possíveis:') 
print ('1. Empilhar uma carta sobre a carta imediatamente anterior')
print ('2. Empilhar uma carta sobre a terceira carta anterior.') 
print('')
print ('Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:') 
print('1. As duas cartas possuem o mesmo valor ou')
print ('2. As duas cartas possuem o mesmo naipe.') 
print('')
print('Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.') 
print ('')
print ('Boa sorte!!')
print ('')
import random
def cria_baralho ():
    baralho = ['A♥', 'K♥', 'Q♥', 'J♥', '9♥', '8♥', '7♥', '6♥', '5♥', '4♥','3♥', '2♥','A♠', 'K♠', 'Q♠', 'J♠','9♠', '8♠', '7♠', '6♠', '5♠', '4♠', '3♠', '2♠','A♦','K♦','Q♦', 'J♦', '9♦', '8♦', '7♦', '6♦', '5♦', '4♦', '3♦', '2♦', 'A♣', 'K♣', 'Q♣', 'J♣', '9♣', '8♣', '7♣', '6♣', '5♣', '4♣', '3♣', '2♣', '10♣', '10♦', '10♠', '10♥']
    random.shuffle (baralho)
    return baralho
def extrai_naipe (string):
    if string [len(string) - 1] == '♦':
        return '♦'
    if string [len(string) - 1] == '♥':
        return '♥'
    if string [len(string) - 1] == '♣':
        return '♣'
    else:
        return '♠'
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
#colocar todas as funções
#condição
jogando = True
while jogando:
    baralho = cria_baralho()
#cores
    for i, carta in enumerate(baralho):
        cor = i + 1
        if extrai_naipe(carta) == '♥':
            print ('\033[1;31;40m{0}.'.format (cor), carta)
        elif extrai_naipe(carta) == '♦':
            print ('\033[1;35;40m{0}.'.format (cor), carta)
        elif extrai_naipe(carta) == '♣':
            print ('\033[1;32;40m{0}.'.format (cor), carta)
        elif extrai_naipe(carta) == '♠':
            print ('\033[1;34;40m{0}.'.format (cor), carta)
#escolha carta   
        while len (baralho) > 1 and possui_movimentos_possiveis(baralho) != False:
            escolha_carta = int (input ('\033[1;37;40mDigite o número da carta desejada: (1 a {0}):'.format (len(baralho))))
#numero da carta não possível
            while escolha_carta > len (baralho) or escolha_carta < 1:
                escolha_carta = int (input('\033[1;37;40mDigite o número de uma carta válida: (1 a {0}):'.format (len(baralho))))
        carta_selecionada = escolha_carta - 1
        possiveis = lista_movimentos_possiveis(baralho, carta_selecionada)
        baralho_escolhido = baralho [carta_selecionada]