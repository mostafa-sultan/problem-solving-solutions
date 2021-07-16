# arr = [4,2,5,8,7,3,7]; 

# rev=0
# pref=0
# a=0
# o=1
# arr.remove()
# for i in range(1, len(arr), 2):
#     #print(arr[i])
#     if (arr[i]+arr[i+1])%2==0:
#          pref=pref+1
#          if(o):
#             if (arr[0]+arr[-1])%2==0:
#                 pref=pref+1
#                 o=0
# for i in range(1, len(arr), 2):
#     # print(arr[i])
#     if (arr[i]+arr[i-1])%2==0:
#          rev=rev+1
 
# def solution(s):
#     a=""
#     arr=[]
#     print(s)
#     for i in range(len(s)):
#         if(s[i]!='\n'):
#             a=a+s[i]
#         elif(s[i]=='\n'):
#             arr.append(a)
#             a=""
#     # print(arr)
#     # arr[0].s

#     import re 
#     aa=re.split('\s+', s)
#     # print(aa)
#     for i in range(len(aa)):
#             if "NULL" in aa[i]: 
#                 aa[i]=r"\n"


#     # print(aa)
#     ss='"'
#     for i in aa:
#         ss=ss+i

#     ss=ss+'"'
#     return ss
#     pass
# print(solution("id,name,age,score\n1,Jack,NULL,12\n17,Betty,28,11"))

# s=input()

# # a=""
# # arr=[]
# print(s.split("\n"))
# print(s.split("\\n"))
# arr
# print("\n")
# print(s[49])

# for i in range(len(s)):
#     print(s[i])
#     if(s[i]!='\n'):
#         a=a+s[i]
#     elif(s[i]=='\n'):
#         arr.append(a)
#         a=""
# print(arr)
# # arr[0].s

# import re 
# aa=re.split('\s+', s)
# # print(aa)
# for i in range(len(aa)):
#         if "NULL" in aa[i]: 
#             aa[i]=r"\n"


# # print(aa)
# ss='"'
# for i in aa:
#     ss=ss+i

# ss=ss+'"'
s=input()
res=""
arr=s.split("\\n") 

f=[e.split(',')  for e in arr]
ii=[] 
# print(f)

for i in f:    
    if "null"in i or "NULL" in i:
        ii.append(f.index(i))
 
# print(ii)



for i in reversed(ii):
    arr.pop(i)

# print(arr)

for i in arr:
    res=res+i+"\\n"
# print('"'+res[0:-2]+'"') 
print(res[0:-2]) 



# if "NULL"or "null"in f[2]:
#     print("hjh")
# o=0




# for i in f:        
#     print(i) 
#     if "null"in i or "NULL" in i:
#         print(f.index(i)) 
#         print(arr) 
#         f.remove(i)
#         arr.pop(f.index(i))
   
# # join(a


# for i in arr:
#     res=res+i+"\\n"

# print(arr)
# print('"'+res[0:-2]+'"') 