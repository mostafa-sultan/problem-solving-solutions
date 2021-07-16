ran,mi,q=map(int,input().split())
# print(ran)
r=[]
qu=[]
for i in range(ran):
    r.append(list(map (int, input().split())) )
for i in range(q):
    qu.append(list(map (int, input().split())) )

for i in range(q):
    res=0
    sum=0
    for n in range(qu[i][0],qu[i][1]+1):
        for nn in r:
          if n in range(nn[0],nn[1]+1):
            #   print(nn)
            # if()
            sum=sum+1

        if(sum>=mi):
            res=res+1
            # print(res)
    print(sum)
# if 94 in range(r[0][0],r[0][1]+1):
#     print('adjhda')
