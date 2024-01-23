def quicksort(arr):
    stack = []
    n = len(arr)
    stack.append((0, n - 1))

    while stack:
        inicio, fim = stack.pop()

        if inicio < fim:
            q = particao(arr, inicio, fim)
            stack.append((inicio, q - 1))  # Partição esquerda
            stack.append((q + 1, fim))     # Partição direita

def particao(arr, inicio, fim):
    pivo = arr[fim]
    i = inicio - 1

    for j in range(inicio, fim):
        if arr[j] <= pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[fim] = arr[fim], arr[i + 1]
    return i + 1

# Exemplo de uso
array = [64, 34, 25, 12, 22, 11, 90]
quicksort(array)
print("Array ordenado:", array)
