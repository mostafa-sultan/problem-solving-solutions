

def solution(N):
    li=[]
    def DecimalToBinary(num): 
        if num >= 1:
            DecimalToBinary(num // 2)
        li.append(num % 2) 
    DecimalToBinary(N) 
    indices = []
    for i in range(len(li)):  
        if li[i] == 1:
            indices.append(i) 
    ma=0
    for i in range(1,len(indices)):
        if((indices[i]-indices[i-1]-1)>ma):
            ma=indices[i]-indices[i-1]-1
    return ma  
    pass
 
print(solution(529))
 