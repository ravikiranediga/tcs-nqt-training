# Using Raise Error 
try:
    print("Enter age:")
    age=int(input())
    if age<18:
        raise ValueError
except ValueError:
    print("Age must be above 18")

else:
    print("eligible")