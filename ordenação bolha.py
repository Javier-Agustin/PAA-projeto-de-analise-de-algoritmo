def bubble_sort(arr):
    comparacoes = 0
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                comparacoes += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return comparacoes

# Exemplo de uso
array = [64, 34, 25, 12, 22, 11, 90]
comparacoes = bubble_sort(array)
print("Array ordenado:", array)
print("Número de comparações:", comparacoes)
