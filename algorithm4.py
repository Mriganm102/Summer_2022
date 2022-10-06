#Bubble Sort
def bubblesort(sequence):
    i = 1
    j = 1
    n = len(sequence) - 1
    for x in range(i, n):
        for y in range(j, n - i):
            j = y + 1
            if sequence[j] > sequence[j + 1]:
                sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]
    return sequence
print(bubblesort([1,4,3,5,7,6]))
