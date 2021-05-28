a =[2, 3, 3, 4]
l = 3   #بتصغر
r = 1  #بتكبر




def solution(a, l, r):
    c=0
    cou=1
    a=sorted(a)
    # print(a)
    for i in range(len(a)):
        if(a[i]>r):
            r=a[i]
            c=c+1
        elif(a[i]<r):
            # print('a')

            for n in range(1,(len(a)+1)):
                    if(a[-n]<l):
                        l=a[-n]
                        c=c+1
                    # print(a[-n])
        elif(a[i]==r):
            # print('a')
            if(a[i]!=l): 
                for n in range(1,(len(a)+1)):
                        if(a[-n]<l):
                            l=a[-n]
                            c=c+1
                        # print(a[-n])
        

    return c
    pass


print(solution([2, 3, 3, 4], 3, 1))



# c=0
# cou=1
# a=sorted(a)
# print(a)
# for i in range(len(a)):
#     if(a[i]>r):
#         r=a[i]
#         c=c+1
#     elif(a[i]<r):
#         # print('a')

#         for n in range(1,(len(a)+1)):
#                 if(a[-n]<l):
#                     l=a[-n]
#                     c=c+1
#                 # print(a[-n])
#     elif(a[i]==r):
#         # print('a')
#         if(a[i]!=l): 
#             for n in range(1,(len(a)+1)):
#                     if(a[-n]<l):
#                         l=a[-n]
#                         c=c+1
#                     # print(a[-n])
    

# print(c)