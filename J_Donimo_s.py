s=int(input())
a=[int(i) for i in input().split()]

a.sort(reverse=True)
t=a.copy()
a.sort()
max=0
min=10000000000
i=0
j=2*s-1
for i

first,last=0,0
for i in range(s):
    if(i%2==0):
      last+=a[i]+t[i]

    else:
      
        first+=a[i]+t[i]

print(abs(first-last))

