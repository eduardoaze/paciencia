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

def empilha(movimentos, i_ori, i_des):
    y = movimentos[i_ori]
    movimentos.remove(y)
    movimentos.remove(movimentos[i_des])
    movimentos.insert(i_des, y)
    return movimentos

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
        while possiveis == []:
            escolher_novamente = int (input('Essa carta não pode ser escolhida. Escolha outra: '))
            possivel_2 = escolher_novamente - 1 
            possiveis= lista_movimentos_possiveis (baralho, possivel_2)
        if possiveis== [1]:
            empilha(baralho,carta_selecionada, carta_selecionada-1)
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
        elif possiveis == [3]:
            empilha (baralho, carta_selecionada,carta_selecionada-3)
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
        elif possiveis == [1,3]:
          escolha_carta = int (input ('Escolha uma carta para empilhar sobre: '))
          empilha(baralho, carta_selecionada, escolha_carta)
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
        elif escolha_carta == carta_selecionada - 2:
            empilha (baralho, carta_selecionada, carta_selecionada - 3)
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
    
    if len (baralho)==1:
      print ("Você conseguiu!!Parabéns!!")
    elif possui_movimentos_possiveis (baralho)== False:
      print ("Não foi desta vez...")
      jogar_novamente= input ("Deseja jogar novamente? (Sim ou Não): ")
    while jogar_novamente != "Sim" and jogar_novamente != "Não" :
      jogar_novamente = input ("resposta indesejada")
    if jogar_novamente == "Sim":
      jogando= True
    elif jogar_novamente == "Não":
      print ("Obrigado por jogar!")
      jogando= False 