def is_even(num):
    if num%2==0:    
        return 'even'
    else:
        return 'odd'

for i in range(1,11):
    print(is_even(i))

#Types of Arguments
"""Default Argument
   Positional Argument
   Keyword  Argument"""

#Default argument
#def power (a,b):
def power(a=1,b=1):#if we cant pass parameter then
    #by default it take a=1 & b=1(default argument)
    return a**b
#print(power(2))-->Through error because 1 element is passed
print(power(2,3))

#Positional Arguments-->Default behaviour is known as positional args
#power(2,3) 2 goes to a 3 goes to b (in which order send the argument
#  parameter recieve that argiument in that order)

#keyword Arguments-->if you dont known the position of that parameter that time we prefer kwargs
print(power(b=3,a=2))

#  *args and **kwargs
# *args and **kwargs are special Python Keywords that are used to pass the varible length of arguments to a funciton

# *args 
#allows us to pass a variable number of non-keyword arguments to a function
def multiply (*args):
    product = 1

    for i in args:
        product=product*i
    return product

print(multiply(1,2,3,4,5,6))

# **kwargs 
# **kwargs allows us to pass any number of keyword arguments.
# Keyword arguments mean that they contain a key-value pair,like a python dictionary.

def display (**kwargs):
    
    for (key,value) in kwargs.items():
        print(key,'->',value)

display(india='delhi',srilanka='colombo',nepal='katmandu',pakistan='islamabad')

#Points to remember while using *args and **kwargs
#order of the arguments matter (noraml->*args->**kwargs)
#the words "args" and "kwargs" are only a convention,you can use any name of your choice.


# How functions are executed in memory

#Nested functions
def g(x):
    def h():
        x='abc'
    x=x+1
    print('in g(x):x=',x)
    h()
    return x
x=3
z=g (x)

#Functions are 1st class citizens
#type and id
def square (num):
    return num**2
print(type(square))
print(id(square))

# reassign
x=square
print((id)(x))
print(x(3))

#Del
# del square

#storing
L=[square,1,2,3]
print(L)

#function is immutable

#Returning a function

def f():
    def x(a,b):
        return a+b
    return x
val=f()(3,4)
print(val)

#Functions as argument
def func_a():
    print("inside func_a")
def func_b(z):
    print("inside func_b")
    return z()
print(func_b(func_a))

#Benefits of functions
"""Code Modularlity
   Code Readiability
   Code Resuability"""

#Lambda Function
#A lambda function is a small anonymus function.
#A lambda function can take any number of arguments,but can only have one expression.

#x-> x^2
a=lambda x:x**2
print(a(2))

#x,y-->x+y
a=lambda x,y:x+y
print(a(5,6))

#Diff between lambda vs Normal function
""".No name
   .lambda has no return value(infact,return a function)
   .lambda is written in 1 line
   . no resuable
   # THEN WHY  USE LAMBDA FUNCTIONS?
        THEY ARE USED WITH HOF(higher order fun)---means it returns a function
        #hod means in input it recievs a function
   """
#check if a string has 'a'
a=lambda s :'a' in s
print(a('hello'))

#odd even
a=lambda x:'even' if x%2==0 else 'odd'
print(a(6))

#Higher Order Functions
#example
def square(x):
    return x**2
#HOF-->input it recieve function
def transform (f,L):
    output=[]
    for i in L:
        output.append(f(i))
    print(output)

L=[1,2,3,4,5]
transform(square,L)
transform(lambda x:x**3,L)

#Map
#Square the items of a list
print(list(map(lambda x:x**2,[1,2,3,4,5])))

#odd/even labelling of list items
print(list(map(lambda x: 'even' if x%2==0 else 'odd',L)))

#dict 
users=[
    {
        'name':'Rahul',
        'age':45,
        'gender':'male'
    },
    {
        'name':'Nitish',
        'age':33,
        'gender':'male'
    },
    {
        'name':'Ankita',
        'age':22,
        'gender':'female'

    }
]
print(list(map(lambda users:users['name'],users)))

#Filter
#number greater than 5
l=[3,4,5,6,7,8]
print(list(filter(lambda x : x>5,l)))

#fetch fruits starting with 'a'
fruits=['apple','guava','cherry']
print(list(filter(lambda x:x.startswith('a'),fruits)))



#Reduce (module import functools)
import functools
print(functools.reduce(lambda x,y:x+y,[1,2,3,4,5]))

#find min
print(functools.reduce(lambda x,y:x if x<y else y,[1,2,3,45]))