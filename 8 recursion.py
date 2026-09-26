# def print_numbers(n):

#     if n == 0:
#         return

#     print(n)
#     print_numbers(n - 1)


# print_numbers(3)

################3

# def factorial(n):

#     if n==0:
#         return 1
    
#     return n*factorial(n-1)
 
# ans = factorial(1)
# print(ans)

#######333

# def Fibbo(n):

#     if n==0:
#         return 0
    
#     if n==1:
#         return 1
    
#     return Fibbo(n-1)+Fibbo(n-2)
 
# ans = Fibbo(6)
# print(ans)

#########33

# def reverse(text):

#     if len(text) == 0:
#         return ""
    
#     return reverse(text[1:]) + text[0]

# print(reverse("hello"))

#################

numbers = [2,4,6,8]
def array_sum(numbers):
    if len(numbers) == 0:
        return 0

    return numbers[0] + array_sum(numbers[1:])

print(array_sum(numbers))