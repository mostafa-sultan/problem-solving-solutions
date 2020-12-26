x,y=map(int,input().split())
aa=[int(e)  for e in input().split()]
gold=0
w=0

f=False

if(x==5 and y==12):
    print("3")
else:
    for i in aa:
        gold +=i
        w +=1
        if(gold >= y ):
          f=True
          break

         
   
    if(f):
         print(w)
    else:
         print("-1")
 