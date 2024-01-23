def merge_sort_iterativo(arr):
    comparacoes = 0
    n = len(arr)
    tamanho = 1

    while tamanho < n - 1:
        for esquerda in range(0, n - 1, tamanho * 2):
            meio = min(esquerda + tamanho - 1, n - 1)
            direita = min(esquerda + tamanho * 2 - 1, n - 1)

            if esquerda < meio and meio < direita:
                comparacoes += 1
                merge(arr, esquerda, meio, direita)

        tamanho *= 2

    return comparacoes

def merge(arr, esquerda, meio, direita):
    n1 = meio - esquerda + 1
    n2 = direita - meio

    # Crie arrays temporários
    L = arr[esquerda:esquerda + n1]
    R = arr[meio + 1:meio + 1 + n2]

    i = j = 0
    k = esquerda

    # Mesclar os arrays temporários de volta ao array original
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copiar os elementos restantes, se houver algum
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Exemplo de uso
array = [64, 34, 25, 12, 22, 11, 90]
comparacoes = merge_sort_iterativo(array)
print("Array ordenado:", array)
print("Número de comparações:", comparacoes)
