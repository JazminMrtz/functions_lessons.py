# functions are ways to wrap your code
# into reusable units
# -----------------------------------------------------------
# how to define a function
# I only define a function ONCE!!!!

# def sayHello():
#     print("say hello")
#     print("Hello Governer")
#     print("Welcome back")

# once you define a function
# you must call or invoke the function
# sayHello()

# -----------------------------------------------------------
# whatever I pass inside the parentheses
# # is called a paramater
# # parameter is a placeholder for future information
# def sayHello(name,age,food):
#     print(f"say hello {name}")
#     print("Hello Governer")
#     print(f"Welcome back {name}")
#     print(f"your age is {age}")
#     print(f"Your favorite food is {food}")

# # when I pass in information into the
# # the callled function, its called an argument
# sayHello("jazmin",16,"pizza")
# sayHello("Lesly",15,"pasta")
# # sayHello("Cristal",15,"tacos")

# -----------------------------------------------------------

# def determinEligibility():
#     # if your age is over 18, you can vote
#     # otherwise, you can't
#     if age >= 18:
#         print("You can vote.")
#     else:
#         print("You have to wait.")

# determinEligibility(12)
# # determinEligibility(15)
# # determinEligibility(19)

# -----------------------------------------------------------

# def WillYouGraduate(gpa,credits,SAT):
#     # gpa: number float variable
#     # credits: number variable
#     # passed SAT: boolean
#     if (gpa==3.0) and (credits>=28) and (SAT == True):
#         print("You passed. Good luck in college.")
    
#     elif(gpa<3.0) or (credits<28) or (SAT != True):
#         print("Back to the drawing board")
#     else:
#         print("Talk to your counselor")
    
# WillYouGraduate(2.8,15,True)
# WillYouGraduate(3.8,28,True)
# WillYouGraduate(2.9,10,False)

# -----------------------------------------------------------



# video



# # return = statement used to end a function and send a result back to the caller

# z = 3 
# def add(x,y):
#     z = x + y 
#     return z

# def subtract(x,y):
#     z = x - y
#     return z

# def multiply(x,y):
#     z = x*y
#     return z

# def divide(x,y):
#     z  = x/y
#     return z 

# print(add(1,2))
# print(subtract(1,2))
# print(multiply(1,2))
# print(divide(1,2))

def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize
    return first + " " + last

full_name = create_name("spongebob","squarepants")
print(full_name)