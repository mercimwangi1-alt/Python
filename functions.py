#method/function---2 types built in/predified function/,and user-defined
from statistics import mean

number = max(0,89,90,709,76)
print(number,"is the maximum no")
#user-defined---always use def---method always have ()
#always call the function by its name like this example of mark--name()
def name():
    print("mark")
    print("mark")
    print("mark")
name()
print()
#for variable to carry diff no,
# parameter- its a variable that is kept in the blacks of a method
#agruments
def multiply1(x,y):
     print(x * y)
multiply1(50, 2)

def multiply():
    v=float(input("enter a number"))
    u=float(input("enter another number"))
    print(v*u)
multiply()
