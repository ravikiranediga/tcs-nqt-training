# Exception inside Main method

def func1():
    
        num1=int(input("Enter a Number:"))
        num2=int(input("Enter a Number:"))
        num3=num1/num2
        print("Result:",num3)

if __name__=="__main__":
    try :
        func1()

    except BaseException:
        print("divisible by zero attempted")
    except ValueError as e:
        print(e)