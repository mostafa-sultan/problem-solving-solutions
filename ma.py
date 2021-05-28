arr=[]
for i in range(5):
    arr.append([e  for e in input()])

a=0
for row in range(5):
    for col in range(5):
        if a%2==0:
            arr[row][col]=00
        
        a=a+1


print(arr);print(a)