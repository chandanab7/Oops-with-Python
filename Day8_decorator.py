#Decorator means a function that takes another function as an argument
#and extends the behavior of the latter function without explicitly modifying it.

# def login(login_page):
#     def wrapper(user,password):
#         if user == "admin" and password == "admin123":
#             print("Login successful")
#             login_page(user,password)
#         else:
#             print("Login failed")
#     return wrapper


# @login
# def login_page(user, password):
#     print("Welcome to the login page")
    
    
# login_page("admin","admin123")



#write a function to print 1st 1000 numbers using decorator to measure the time taken to execute the function.

import time
def execution_time(first_n):
    def wrapper(n):
        start=time.time()
        first_n(n)
        end=time.time()
        print(end-start)
    return wrapper

@execution_time
def first_n(n):
    sum=0
    for i in range(1,n+1):
        sum+=1
    print("sum:",sum)

first_n(1000000)





