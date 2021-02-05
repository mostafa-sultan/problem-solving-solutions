n=int(input()) 
arr=[int(i) for i in input().split()]
positiv=0
negativ=0
zero=0
for i in arr:
    if i>0:
        positiv+=1
    elif i<0:
        negativ+=1
    else:
        zero+=1 
print(format(positiv/n, '.6f'))  
print(format(negativ/n, '.6f'))  
print(format(zero/n, '.6f'))  
