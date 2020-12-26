x=input().split()
a=list(x[0])
b=list(x[1])

str='llo'
print(str.find("p"))
count=0
check=[]
for i in a:
    if(str.find(i)==-1):
      for s in b:
        if(s==i):
            count+=1
            str=str+i
            continue


print(str)
        # if(str.find(i)==-1):

        #     count+=1
        #     str=str+i


