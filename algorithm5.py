#Insertion Sort
def insertion_sort(sequence):
    n = len(sequence)
    for j in range(1,n):
        i = 0
        while sequence[j] > sequence[i]:
            i = i + 1
        sequence[j], sequence[i] = sequence[i], sequence[j]
    print(sequence)
insertion_sort([1,3,2,5,4,3])