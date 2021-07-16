# input strytgy
# m=list(map (int, input().split())) 
# x,y=map(int,input().split())
# aa=[int(e)  for e in input().split()]
# aa=[e  for e in input()]



 
########################## lists###################################
# Create a single string from all the elements in list 
# a = ["Geeks", "For", "Geeks"]
# print(" ".join(a))



# # Python3 program to convert a list
# # of integers into a single integer
# def convert(list):  
#     # Converting integer list to string list
#     s = [str(i) for i in list]
      
#     # Join list items using join()
#     res = int("".join(s))
      
#     return(res)



#  using map()
# # to convert number to list of integers
#res = list(map(int, str(num)))



# Find The Most Frequent Value In A List. 
# test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
# print(max(set(test), key = test.count))



#  In-Place Swapping Of Two Numbers. 
# x, y = 10, 20
# print(x, y)
# x, y = y, x
# print(x, y)



# Code to find top 3 elements and their counts
# using most_common

# from collections import Counter 
# arr = [1, 3, 4, 1, 2, 1, 1, 3, 4, 3, 5, 1, 2, 5, 3, 4, 5]
# counter = Counter(arr)
# top_three = counter.most_common(3)
# print(top_three)




# # Python code to find 3 largest and 4 smallest
# # elements of a list.

# import heapq 
# grades = [110, 25, 38, 49, 20, 95, 33, 87, 80, 90]
# print(heapq.nlargest(3, grades))
# print(heapq.nsmallest(4, grades))




# # Python code to apply a function on a list
# income = [10, 30, 75] 
# def double_money(dollars):
#     return dollars * 2 
# new_income = list(map(double_money, income))
# print(new_income)

########################## string###################################


# Checking if two words are anagrams 
# from collections import Counter
# def is_anagram(str1, str2):
#      return Counter(str1) == Counter(str2)
  
# # or without having to import anything 
# def is_anagram(str1, str2): 
#     return sorted(str1) == sorted(str2) 
  
# print(is_anagram('geek', 'eegk'))
# print(is_anagram('geek', 'peek'))  


# Chaining Of Comparison Operators. 
# n = 10
# result = 1 < n < 20
# print(result)
# result = 1 > n <= 9
# print(result)



# Reversing a string in Python
# a = "GeeksForGeeks"
# print("Reverse is", a[::-1])




# string = ""
# lst = ["Geeks", "for", "Geeks"]
# for i in lst:
#     string += " "+i
# print(string)




