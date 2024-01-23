def selection_sort(arr):
    comparacoes = 0
    n = len(arr)

    for i in range(n - 1):
        indice_menor = i

        for j in range(i + 1, n):
            if arr[j] < arr[indice_menor]:
                indice_menor = j
                comparacoes += 1

        if indice_menor != i:
            arr[i], arr[indice_menor] = arr[indice_menor], arr[i]

    return comparacoes

# Exemplo de uso
array = [64, 25, 12, 22, 11]
comparacoes = selection_sort(array)
print("Array ordenado:", array)
print("Número de comparações:", comparacoes)
