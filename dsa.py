
"""
Given two strings s1 and s2, you need to find if we can delete 
some characters of s1 to make s1 and s2 anagrams.
Both strings will not contain repeated characters

Input s1 = "abcd"
        s2 = "ac"
output : True


Input s1 = "abcd"
        s2 = "cz"
output : False
"""

# def canMakeAnagrams(s1,s2):
#     s1_=set(s1)
#     s2_=set(s2)
#     return s2_.issubset(s1_)
# print(canMakeAnagrams('abcd','ca'))



####################################################################3






# def completeStrings(s):

#     set_ =set('abcdefghijklmnopqrstuvwxyz') 
#     return set_.issubset(set(s))

# s = "abcdefghijklmnopqrstuvwxyzabcjia"
# # s = 'geeks'
# # completeStrings(s)
# print(completeStrings(s))


#####################################################################
'''List Traversal'''
'''Input: arr = [54, 43, 2, 1, 5]
Output: 54 43 2 1 5
Explanation: Just traverse and print the numbers.'''
# arr = [54, 43, 2, 1, 5]
# arr1 = ' '.join(str(i) for i in arr )
# print(arr1)

# #User function Template for python3
# def listTraversal(arr):
#     #Write your code below
# #     print(' '.join(str(i) for i in arr))
#     return ' '.join(str(i) for i in arr)
    
#     #Don't provide the new line

# # listTraversal(arr)
# print(listTraversal(arr))

###############3

'''List Traversal Reverse'''

# arr = [54, 43, 2, 1, 5]
# def listTraversalReverse(arr):    
#     arr1 = arr[::-1]
#     arr2 = ' '.join(str(i) for i in arr1)
#     print(arr2)
    
# listTraversalReverse(arr)

'''
Decrement List Values::
You are given a list that contains integers. 
You need to decrement each element of the list by 1 
and return the list.

Examples:

Input: arr = [54, 43, 2, 1, 5]
Output: 53 42 1 0 5
Explanation: Just decrement the numbers by 1.

Input: arr = [324, 5, 2, 2]
Output: 323 4 1 1
Explanation: Just decrement the numbers by 1.
'''
# arr = [54, 43, 2, 1, 5]
# def decrementList(arr):
#     newL = []
#     for i in arr:
#         # newL = i-1
#         newL.append(i-1)
# #     return newL
#     res =  ' '.join(str(i) for i in newL)
# #     print(newL2)
# #     return newL2
#     return res

  
# print(decrementList(arr))

# ############3
# a = 1
# b=2
# c=3
# def appendToList(a,b,c):
#     res = []
#     res.append(a)
#     res.append(b)
#     res.append(c)
#     return res
# print(appendToList(a,b,c))

##########

'''
You are given a list arr that contains integers. 
You need to return average of the non negative integers.

Examples:

Input: arr = [-12, 8, -7, 6, 12, -9, 14]
Output: avg = 10.0
Explanation: The non negative numbers are 8 6 12 14. 
The sum is 8+6+12+14 = 40, Average = 40/4 = 10.0

Input: arr = [1, 2, 3]
Output: avg = 2.0
Explanation: The non negative numbers are 1 2 3. 
The sum is 1+2+3 = 6, Average = 6/3 = 2.0

Input: arr = [5, 0, 0, 0]
Output: avg = 1.25
Explanation: The non negative numbers are 5 0 0 0.
The sum is 5+0+0+0 = 5, Average = 5/4 = 1.25
'''
# arr = [-12, 8, -7, 6, 12, -9, 14]
# arr = [1,2,3]
# arr = [5,0,0,0]

# def nonNegativeAverage(arr):
    
#     #Write your code to find average of positive numbers in number list
#     #Return the answer
#     positive = []
#     for i in arr:
#         if i>=0:
#             positive.append(i)
#     return sum(positive)/len(positive)
# print(nonNegativeAverage(arr))


'''
Input: tup = (4, 5, 1, 2, 3, 5)
Output: 8 10 2 4 6 10
Explanation: multiplied numbers by 2.
'''
# tup = (4, 5, 1, 2, 3, 5)
# def doubleTup(tup):
#     ans = list()
#     for i in tup:
#         ans.append(i*2)
#     return tuple(ans)

# print(doubleTup(tup))

######3
# def double_numbers(tup):
#     return tuple(x * 2 for x in tup)

# tup = (4, 5, 1, 2, 3, 5)
# print(double_numbers(tup))

###########333


'''
you are given an integer array number[],
you need to find the smallest positive missing number. 
Example: 
input:numbers = [1,2,3,4] 
output=5 
Explanation: 5 is the smallest positive missing number
'''

# def smallest_missing_positive(numbers):
#     i = 1
#     while True:
#         if i not in numbers:
#             return i
#         i += 1

# numbers = [1, 2, 3,4]
# # numbers = [6,5,3,1]
# print(smallest_missing_positive(numbers))  # Output: 5

############

# def shift_letters(s):
#     result = ''
#     for i in range(0, len(s), 2):
#         char = s[i] # k
#         digit = int(s[i + 1]) # 3
#         # shift character and wrap from 'z' to 'a'
#         new_char = chr((ord(char) - ord('a') + digit) % 26 + ord('a'))
#         result += new_char
#     return result

# # Example usage
# s = "k3a4"
# # s = "y2b2"
# print(shift_letters(s))  

# numbers = [10, 20, 30, 20, 40, 10, 50]

# seen = set()
# duplicates = set()

# for number in numbers:
#     if number in seen:
#         duplicates.add(number)
#     else:
#         seen.add(number)

# print(duplicates)