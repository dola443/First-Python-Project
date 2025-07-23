t = int(input())

i = 1
while i <= t:
    s = input().split()
    a, b, c = map(int, s)
    #b = int(input())
    #c = int(input())

    if a + b == c:
        print("yes")
    elif a + c == b:
        print("yes")
    elif b + c == a:
        print("yes")
    else:
        print("no")
    i = i + 1