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
        while possiveis == []:
            escolher_novamente = int (input('Essa carta não pode ser escolhida. Escolha outra: '))