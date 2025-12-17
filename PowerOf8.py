def powerof8(n):
    bitposition=0
    mask=1
    while (bitposition<=63):
        mask<<=bitposition
        if(mask==number):
            return True
        bitposition+=1
        mask=1
        return False
number=int(input("Enter a number:"))
print(powerof8(number))
if(powerof8(number)):
    print(number,"is a power of 8")
else:
    print(number,"is not a power of 8")
    
