#include<iostream>
using namespace std;
int main() {
bool f =1;
int n ,maxnump=0,minump=101;
cin>>n;
int numpers[n];
 for (int i=0;i<n;i++){
     cin >>numpers[i];
     if (numpers[i]>maxnump)
         maxnump=numpers[i];
       if (numpers[i]<minump)
	       minump=numpers[i];}
	  if((maxnump-minump)%2==0){
         int d=(maxnump-minump)/2;
	     for(int i=0;i<n;i++){
             if(!(numpers[i]==maxnump||numpers[i]==minump||numpers[i]==minump+d)){f=0;}
			 }
		if(f)
		  cout<<d;
		else
		 {cout<<-1;}	 
	   }
	   else 
	   {
	    int d=maxnump-minump;
	    for(int i=0;i<n;i++)
	     if(!(numpers[i]==maxnump||numpers[i]==maxnump-d))
	        f=0;
	    	if(f)
		  cout<<d;
		else
		 {cout<<-1;}	     
	   }
	return 0;}



