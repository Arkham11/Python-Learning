 #1 Create your own module 
# import my_utils
# print(my_utils.greet("aaron"))
# print(my_utils.is_even(68))

#2 Use Built-in Modules
# import math 
# print (math.sqrt(16))
# import random 
# for i in range (5):
#     print(random.randint(1, 7))
# import datetime 
# print("Todays date ie:",datetime.date.today()) 

#3 Simple Lamdas
# num =lambda x: x*2
# print (num(5)) 

# check = lambda x: x > 0
# print (check(9))
# print(check(-9))

#4 Transform Lists 
# num = [1, 2, 3, 4, 5]
# triple = map(lambda x: x*3, num)
# print (num)
# print (list(triple))

# names = ["aaron", "james", "mike"]
# cap = map(lambda x: x.capitalize(), names)
# print (names)
# print (list(cap))

#5 Filter Lists 
# nums = [ 5, 12, 8, 3, 20]
# above = filter(lambda x: x > 10, nums)
# print (nums)
# print (list(above))

# words = ["apple", "bat", "cat", "elephant"]
# length = filter (lambda x: len(x) > 3, words)
# print (words)
# print (list(length))

#6 Custom Sorting 
# word = ["python", "is", "awesome", "fun"]
# sort = sorted(word, key= lambda x: len(x))
# print (word)
# print (sort)  

# elements = [(1,5), (2,3), (4,1), (3,2)]
# sorted_elements = sorted(elements, key= lambda x: x[1])
# print (elements)
# print(sorted_elements)

#7 Recursice Countdowm
# def countup(n):
#     if n == 0:
#         return 1
#     countup(n   - 1)
#     print (n)
# print(countup(5))

#8 Power Function 
# def power(base, exp):
#     if exp == 0:
#         return 1
#     return base * power(base, exp - 1)
# print(power(2,3))

#9 Sum of List 
def sum_list(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sum_list(lst[1:])
print(sum_list([1, 2, 3, 4, 5,6,7]))