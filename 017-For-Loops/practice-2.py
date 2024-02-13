# a = 6
# b = 9
# print(a + b)

a = int(input("enter a value"))
b = int(input("enter b value"))
print(a + b)

if((a + b) > 10):
    print("OK")
    d = a+b
    while(d > 0):
        print("Yo Value Of D = ",d)
        d = d - 1
        if(d == 100):
            break
        else:
            continue
elif((a+b) == 0):
    print("OK BUDDY")

else:
    print("NOT Ok")