def bin2dec(val):
    rev=val[::-1]
    dec=0
    i=0
    for dig in rev:
        dec+=int(dig)*2**i
        i+=1
    return dec
def Oct2Hex(val):
    rev=val[::-1]
    dec=0
    i=0
    for dig in rev:
        dec+=int(dig)*8**i
        i+=1
    list=[]
    while dec!=0:
        list.append(dec%16)
        dec=dec//16
    n1=[]
    for elem in list[::-1]:
        if elem<=9:
            n1.append(str(elem))
        else:
            n1.append(chr(ord('A')+(elem-10)))
    hex=" ".join(n1)
    return hex

num1=input("enter a binary number:")
print(bin2dec(num1))
num2=input("enter a octal number:")
print(Oct2Hex(num2))

    
