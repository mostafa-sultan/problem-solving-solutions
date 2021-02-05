num=int(input())
flag=" "
forin=num
for i in range(num):
    for a in range(1,(num+1)):
        if a>=forin:
            print("#",end='')
        else:
            print(" ",end='')
    forin-=1
    print()



