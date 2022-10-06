#Linear Search Algorithm
def linear_search(x,sequence):
    i = 0
    if x in sequence:
        while x != sequence[i] and i <= (len(sequence) - 1):
            i = i + 1
        if i <= (len(sequence) - 1):
            location = i
    else:
        location = 0

    return location

print(linear_search(9, [1,2,3,4,5,6,7,8]))