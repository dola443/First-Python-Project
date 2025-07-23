n = int(input())
i = 0
for i in range(1 , n +1):
    print((n - 1) * " ", end="")
    print(i * "*")
    n = n - 1
