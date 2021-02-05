pop=[int(i) for i in input().split()]
alis=[int(i) for i in input().split()]
popres,alisres=0,0
# print(popres)
forin=0
for i in pop:
    if i>alis[forin]:
        popres+=1
    elif i<alis[forin]:
        alisres+=1
    forin+=1 
print(popres,end=" ")
print(alisres)

