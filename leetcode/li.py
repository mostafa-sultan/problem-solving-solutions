# l1=list(map (int, input().split())) 
# l2=list(map (int, input().split())) 
# # print(l1[::-1])
# # print("".join(l1))


# # Python3 program to convert a list
# # of integers into a single integer
# def convert(list):
      
#     # Converting integer list to string list
#     s = [str(i) for i in list]
      
#     # Join list items using join()
#     res = int("".join(s))
      
#     return(res)


# a=convert(l1[::-1])+convert(l2[::-1]) 

 
# res = list(map(int,str(a))) 
# print(res[::-1])



child = {'a':'b', 'b': 'c', 'c': 'd', 'd': None}
def next_ll(state=['a']):
        value = state[0]
        if value is not None:
            state[0] = child[value]
            return value

a=[x for x in iter(next_ll, None)]
print(a)