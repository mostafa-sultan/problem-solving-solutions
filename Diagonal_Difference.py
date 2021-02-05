num=int(input())
sum1=0
sum2=0
for i in range(num):
    arr=[int(ii) for ii in input().split()]
    sum1+=arr[i]
    sum2+=arr[num-(1+i)]
print(abs(sum1-sum2))