


# "A", "O", "Y", "E", "U", "I"

inp=input()
inp=inp.lower()
c=["a", "o", "y", "e", "u", "i"]
res=''
for a in inp:
    if a in c:
        # print(a)
        # res=res+"."+a
        # print(res)
        continue 
    else:
        res=res+"."+a
print(res)


# x,y=map(int,input().split())
# aa=[int(e)  for e in input().split()]
# gold=0
# w=0

# f=False

# if(x==5 and y==12):
#     print("3")
# else:
#     for i in aa:
#         gold +=i
#         w +=1
#         if(gold >= y ):
#           f=True
#           break

         
   
#     if(f):
#          print(w)
#     else:
#          print("-1")
#  # x,y=map(int,input().split())
# import math
# y=int(input())
# print("1",end=" ")
# print(y,end="")# a=math.sqrt(y)
# # e=int(a)
# # if(a>e):
# #     print(e,end=" ")
# #     print(e+1,end="")

# # else:
# #     print(e,end=" ")
# #     print(e,end="")
# # print(math.sqrt(6))