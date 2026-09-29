#Using function()
def func1():
    try:
        num1=int(input("Enter a Number:"))
        num2=int(input("Enter a Number:"))
        num3=num1/num2
        print("Result:",num3)
    except ZeroDivisionError:
        print("divisible by zero attempted")
    except ValueError as e:
        print(e)

if __name__=="__main__":
    func1()
