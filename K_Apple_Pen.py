x=int(input()) 
e=[]
for i in range(0,x*2):
      e.append(input().split()[-1])
for i in range(0,len(e),2):
    print("Uh! "+e[i+1]+"-"+e[i]+"!")
 
# print(e[3])
# y=int(input()) 
# z=int(input()) 
# s=int(input()) 
# d=y*3+z*3+s*3
# print(d)