#Matirxa - m x k m is row k is column
#Matirxb - k x n k is row n is column
def procedure(a,b):
    z = 0
    y = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            z = z + 1
    for i in range(len(b)):
        for j in range(len(b[i])):
            y = y + 1
    a_row = len(a)
    a_column = int(z / a_row)
    b_row = len(b)
    b_column = int(y / b_row)
    if a_row == b_column:
        k = a_row
        rows = int(y/k)
        columns = int(z/k)
    elif a_column == b_row:
        k = a_column
        rows = int(z / k)
        columns = int(y / k)
    else:
        return "Cannot do matrix multiplication"
    c = []
    for i in range(0,rows):
        c.append([])
    for i in range(0, rows):
        for j in range(0,columns):
            c[i].append(0)
            print([])
    for i in range(0,rows):
        for j in range(0,columns):
            c[i][j] = 0
            for q in range(0,k):
                print(q)
                c[i][j] = c[i][j]+ (a[i][q] * b[q][j])
                print(c)
    print(c)
procedure([[1,2],[2,3]], [[2,2],[4,3],[3,1]])
#             2x2               3x2