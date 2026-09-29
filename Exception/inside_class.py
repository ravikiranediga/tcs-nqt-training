# Exception inside Class
class Myclass:
    def func1(self):
    
        num1=int(input("Enter a Number:"))
        num2=int(input("Enter a Number:"))
        num3=num1/num2
        print("Result:",num3)

if __name__=="__main__":
    ob=Myclass()
    try :
        ob.func1()
    except ZeroDivisionError as e:
        print(e)