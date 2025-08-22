def soma_lista(lista):
    """Retorna a soma dos elementos da lista."""
    return sum(lista)

def contar_pares(lista):
    """Retorna a quantidade de números pares na lista."""
    return len([x for x in lista if x % 2 == 0])