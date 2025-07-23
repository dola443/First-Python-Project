n = int(input("Enter how many numbers to add: "))

a = 1
result = 0
while a <= n:
    number = int(input())
    result = result + number
    a = a + 1

print("Result is: ", result)
print(a)