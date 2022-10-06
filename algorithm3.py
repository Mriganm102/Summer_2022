#Binary Search Algorithm
def binary_search(x, sequence):
    i = 1
    j = len(sequence) - 1
    while i < j:
        m = (i + j) // 2

        if x > sequence[m]:
            i = m + 1
        else:
            j = m
    if x == sequence[i]:
        location = i
    else:
        location = 0
    return location
print(binary_search(7, [1,2,3,4,5,6]))