a = int(input("enter a length"))
b = int(input("enter a length"))
c = int(input("enter a length"))

if a + b > c :
    if b + c > a:
        if a + c > b:
            print("valid")
        else:
            print("invalid3")
    else:
        print("invalid2")
else:
    print("invalid1")

