def insertion_sort(arr):
    comparacoes = 0
    n = len(arr)

    for i in range(1, n):
        elemento_atual = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > elemento_atual:
            comparacoes += 1
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = elemento_atual

    return comparacoes

# Exemplo de uso
array = [12, 11, 13, 5, 6]
comparacoes = insertion_sort(array)
print("Array ordenado:", array)
print("Número de comparações:", comparacoes)
