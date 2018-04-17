"""This is docstring for mymodule it contains 3 functions"""
def function1(a):
    "docstring f1"
    print(__name__)
    print("In function 1")

def function2():
    "docstring f2"
    print(" infn2 ")

def function3(a=12,b=10):
    "docstring f3"
    print("infunc3")
    return a+b

if __name__ == "__main__":
    function1(12)
    function2()
    function3()