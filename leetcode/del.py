# juice =[1, 1, 5]
# capacity = [6, 5, 8]
juice = [1, 2, 3, 4] 
capacity = [3, 6, 4, 4]
av=[]
for ii in range(len(juice)): 
      av.append((capacity[ii]-juice[ii]))

print(av)
a=1

for ii in range(len(juice)): 

    for jj in range(len(juice)):
        if(ii != jj):
            if(av[ii]>=juice[jj]):
                av[ii]=av[ii]-juice[jj]
                juice[jj]=0 
                a=a+1
        # else:
            # print("j")


print(juice.count(0))
print(av)


