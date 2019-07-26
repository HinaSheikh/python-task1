n=input("Enter a number :")
if( n.isnumber()):
    n=int(n)
    result=0
    mul=0
    for i in range(0,3):
        mul=mul*10+n
        result=result+mul
    print(result)
else:
    print("Enter a valid number")

