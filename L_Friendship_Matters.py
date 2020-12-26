x,y=map(int,input().split())
student=[]
grope=[]
studentjoed=[]
# s="asa"

# s=s+" as"

# print(s)


for i in range(x):
    student.append(input())
for a in range(y):
    aa=input()
    if(aa[0]=="1"):
        studentjoed.append(aa.split()[1])
        studentjoed.append(aa.split()[2])
        if(studentjoed.index(aa.split()[1]) or studentjoed.index(aa.split()[2]) ):
            for f in studentjoed:
                qq=f.split()
                for  ttt in qq:
                    pass
        grope[a]=aa.split()[1] +" "+aa.split()[2]
       
        

    elif(aa[0]=="2"):
       
        

# print(ask)
# for k,v in ans.items():
#     print(k)

#     if(ask[k]==v or ask[v]==k):
#         print("yes")
#     else:
#         print("no")
