def count_occur(s, x):
    n = len(s)
    i = 0
    cnt = 0
    while i < n:
        if s[i] == x:
            cnt = cnt + 1
        i = i + 1
    return cnt

s = [1, 6, 1, 5, 6, 0]
print(count_occur(s, 6))
