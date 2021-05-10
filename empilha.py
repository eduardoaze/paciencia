def empilha(movimentos, i_ori, i_des):
    y = movimentos[i_ori]
    movimentos.remove(y)
    movimentos.remove(movimentos[i_des])
    movimentos.insert(i_des, y)
    return movimentos