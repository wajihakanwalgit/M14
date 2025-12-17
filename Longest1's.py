def max1(number):
    count=0
    while(number!=0):
        number=number&(number<<1)
        count+=1
    return count
number= int(input("Enter number"))
print("longest 1's",max1(number))