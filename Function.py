# Functions : function is a block of code that performs a specific task and can be reused whenever needed.

# def anki():        #fun definition
#     print("Heyyy from Ankita!")
#     print("How are you!")
# anki()      #fun call


# # Sum of a and b

# def sum(a, b):
#     s = a + b
#     return s
# ans = sum(10, 20)
# print("The sum of a and b is : ", ans)

# # calc avg

# def calc_avg(a, b, c) :
#     sum = a + b + c
#     return sum/3
# ans = calc_avg(10, 20, 30)
# print(ans)


# Types of Function
# 1. built-in function :- Already provided by python
# 2. User defined function :- Created by you using def

# #Lambda function

# avg = lambda a, b: a + b/2
# print(avg(4, 5))

def calc_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
    
n = int(input("Enter n :"))
print(calc_factorial(n))    
