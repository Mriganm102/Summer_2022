#Finding the maximum element in a Finite Sequence
def max_number(finite_sequence):    #create procedure
    max = finite_sequence[1]        #set max as first element in sequence
    for i in finite_sequence:       #loop finite_sequence
        if max < i:
            max = i                 #if max < i set max to i
    return max                      #return the max value of sequence

print(max_number([1,2,3,4,5,6,7]))