# Task 3 (Decorator) – Simple Problem Statement
# Problem: Permission Checker
# You want a function dashboard() but only admin should access it.
# What to do
# Create a decorator called admin_only
# Decorator behavior
# if username == "admin" → allow function execution
# else → print "Access Denied"
# Apply decorator
# Use it on:
# dashboard()
# Test
# Call dashboard using:
# admin → works
# other user → blocked


def admin_only(func):
    def wrapper(username):
        if username=="admin":
            func()
        else:
            print("Access Denied")
    return wrapper

@admin_only
def dashboard():
    print("welcome to admin")

dashboard("admin")
dashboard("chandu")



