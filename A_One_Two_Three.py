i=int(input())
student=[]
for x in range(i):
    ii=input()
    if(len(ii)==5):
        student.append(3)
    else:
        if((ii[0]=='o'  and ii[1]=='n')or (ii[2]=='e' and ii[1]=='n')or(ii[0]=='o'  and ii[2]=='e')):
          student.append(1)
        else:
             student.append(2)

    # student.append(input())
for a in student:

 print(a)