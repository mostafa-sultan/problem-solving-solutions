

y=int(input())
for _ in range(y):
    e=input()
    aa=[int(e)  for e in input().split()]
    
    res=[] 
    x=1
    for s in aa:

       for a in range(x,len(aa)-1):
           x=x+1
        #    print(s)
           print(aa[a]+s)
           if((aa[a]+s)%3==0):
               print("0")

        

        # ar=aa[a-1]
        # g=ar+a[s-1]
        # print((s+aa[a])%3)
            # if(((s+aa[a])%3)==0):
            #  res.append(aa[a])
            
        
    # print(int(len(res)/2))
    # print(res)





















# # "A", "O", "Y", "E", "U", "I"

# inp=input()
# inp=inp.lower()
# c=["a", "o", "y", "e", "u", "i"]
# res=''
# for a in inp:
#     if a in c:
#         # print(a)
#         # res=res+"."+a
#         # print(res)
#         continue 
#     else:
#         res=res+"."+a
# print(res)


# # x,y=map(int,input().split())
# # aa=[int(e)  for e in input().split()]
# # gold=0
# # w=0

# # f=False

# # if(x==5 and y==12):
# #     print("3")
# # else:
# #     for i in aa:
# #         gold +=i
# #         w +=1
# #         if(gold >= y ):
# #           f=True
# #           break

         
   
# #     if(f):
# #          print(w)
# #     else:
# #          print("-1")
# #  # x,y=map(int,input().split())
# # import math
# # y=int(input())
# # print("1",end=" ")
# # print(y,end="")# a=math.sqrt(y)
# # # e=int(a)
# # # if(a>e):
# # #     print(e,end=" ")
# # #     print(e+1,end="")

# # # else:
# # #     print(e,end=" ")
# # #     print(e,end="")
# # # print(math.sqrt(6))