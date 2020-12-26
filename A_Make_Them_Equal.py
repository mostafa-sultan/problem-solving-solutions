a=int(input())
aa=[int(e)  for e in input().split()]

mx=max(aa)
mn=min(aa)

if((mx-mn)%2==0):
    r=(mx-mn)/2
    for i in aa:

        if(aa[i]!=mx or aa[i]!=mn or aa[i]!=mn+r):
            print(int(r))
            break
    #         f=1
    # if(f):
    #   print(r)

    # else:
    #   print("-1")

else:
    # print("adad")

    r=mx-mn
    for i in aa:
        if(aa[i]!=mx or aa[i]!=mx-r):
            print(int(r))
            break
    #         f=0
    # if(0):
    #   print(r)

    # else:
    #   print("-1")