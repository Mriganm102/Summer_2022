#Greedy Algorithm 2.0
def schedule(start, end):
    end = sorted(end)
    n = len(start)
    compatible = [start[0], end[0]]
    for j in range(0,n):
        if start[j] > compatible[-1]:
            compatible.append(start[j])
            compatible.append(end[j])
    print(compatible)
schedule([9,10,11.5,12.5,12.7,14], [10.5,11.2,12,13,13.5,14.5])
