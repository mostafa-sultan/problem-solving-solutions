arr=[int(i) for i in input().split()]
arr.sort()
s=arr[(len(arr)-4):(len(arr))]
ss=arr[0:4]
print(sum(ss),sum(s))