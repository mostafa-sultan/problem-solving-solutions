a=[2]*9019
result=0 
for i in range(len(a)): 
    if(sum(a[0:i])==sum(a[i+1:len(a)])):
        result=1 
print(result)
print(len(a))