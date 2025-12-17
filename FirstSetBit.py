def firstsetbit(n):
    position=1
    mask=1
    while(not(n&mask)):
        mask=mask<<1
        position+=1
    return position
number=int(input("enter number"))
print(firstsetbit(number))