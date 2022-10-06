#Greedy Algorithm
def change(coins, n):
    r = len(coins)
    d = []
    for i in range(0,r):
        d.append(0)
        while n >= coins[i]:
            d[i] = d[i] + 1
            n = n - coins[i]
    print(d)
change([25,10,5,1], 59)