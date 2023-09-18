def busca_linear(lista, num):
    for i in range(len(lista)):
        if lista[i] == num:
            return i

    return -1

def busca_binaria(lista, num):
    esquerda = 0
    direita = len(lista)-1

    while esquerda <= direita:

        meio = (esquerda + direita) // 2

        if num == lista[meio]:
            return meio

        elif lista[meio] < num:
           esquerda = meio+1

        else:
            direita = meio-1

    return -1

