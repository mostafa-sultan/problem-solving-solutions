#include<iostream>
using namespace std;
int main() {
	bool f =1;
	
int n ,max=0,min=101;
cin>>n;
int arr[n];
 for (int i=0;i<n;i++)
      {cin >>arr[i];
      if (arr[i]>max)
         max=arr[i];
       if (arr[i]<min)
	       min=arr[i];   
	  }
	  if((max-min)%2==0)
	   {int d=(max-min)/2;
	     for(int i=0;i<n;i++)
	         {if(!(arr[i]==max||arr[i]==min||arr[i]==min+d))
	            {f=0;
				}
			 }
		if(f)
		  cout<<d;
		else
		 {cout<<-1;
			  }	 
	   }
	   else 
	   {
	   int d=max-min;
	    for(int i=0;i<n;i++)
	     if(!(arr[i]==max||arr[i]==max-d))
	        f=0;
	    	if(f)
		  cout<<d;
		else
		 {cout<<-1;
			  }	     
	   }
	return 0;}




    a=int(input())
aa=[int(e)  for e in input().split()]

max1=max(aa)
min2=min(aa)
b=max1-min2
res=False
motawst1=sum(aa)/len(aa)
rr=set(aa)
ww=list(rr)
motawst=sum(ww)/len(ww)
print(motawst)
print(motawst1)
# ss=ww.sort()
# print(ww)

o=0

if(len(rr) == 2):
    if(max1-motawst == motawst-min2):
        if(round(max1-motawst)==min2 ):
            print(int(motawst))
        else:
            print(int(max1-motawst))
    else:
     print("-1")
elif(len(rr) == 3):
    if(ww[1]-ww[0] == ww[2]-ww[1]):
        print(ww[1]-ww[0] )
    else:
     print("-1")




# print((8*25)/16)
        # motawst=sum(aa)/len(aa)
# flag=motawst
# if(motawst == int(motawst)):
#     for i in aa:
#       if(motawst == aa[i]):
#           print("",end="") 
#       elif(motawst > aa[i]):






# motawst=sum(aa)/len(aa)
# mo=int(motawst)
# mo2=int(motawst)+1
# if(motawst == int(motawst)):
#     print("jj")
#     if(min2+motawst == max1-motawst):
#         print(motawst)

# elif(mo+min == max1-mo):
#     print(mo)    

# elif(mo2+min == max1-mo2):
#     print(mo2)    

# else:
#     print("-1")
# print(motawst)
# print(int(1.9))
# print(mo+min2)
# if(mo+min2 == mo+min2):
#     print(mo)
# else:
#     print("-1")
