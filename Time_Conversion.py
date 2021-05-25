i=input()
date=i[-2]+i[-1]
h=int(i[0:2])
m=i[3:5]
s=i[6:8]
# print(m) 
if date=='PM':
    if h==12:
      a="12:"+m+":"+s
      print(a)
    else:
        h=h+12 
        a=str(h)+":"+m+":"+s
        print(a) 
else:
    if h==12:
      a="00:"+m+":"+s
         
      print(a)
    else:
        print(i[0:-2])
