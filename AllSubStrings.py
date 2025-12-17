import math

def printpowerset(set,set_size):
    pow_set_size = int(math.pow(2,set_size))
    count=0
    j=0
    for counter in range(0,pow_set_size):
        for j in range(0,set_size):
            if((counter & (1 << j)) > 0):
                print(set[j],end=" ")
                count+=1
        print()
str= int(input("Enter string"))
printpowerset(str,len(str))
   
   