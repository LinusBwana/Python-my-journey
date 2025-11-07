# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in
# Python scope resolution order - LEGB

# example1
# Local Scope-------------------------------------------
def func1():
    a = 2 # a - is local in function 1. Function 1 a can not see b
    print(a)
def func2():
    b = 5 # b - is local in function 2. Function 2 a can not see a
    print(b)
func1()
func2()


# example 2
# Enclosed Scope-----------------------------------------
def func1():
    x = 2
    def func2():
        print(x) # uses the x from the enclosed scope since there is  no x in the local scope
    func2()
func1()


# example 3
# Global Scope-----------------------------------------
# Global meaning outside any function
def func1():
    print(x)
def func2():
    print(x)
x=3
func1()
func2()

# example 4
# Built-in Scope-----------------------------------------
from math import pi

def func1():
    print(pi) #pi is built-in
func1()