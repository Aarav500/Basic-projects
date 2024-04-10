# constants are fixed values sush as numbers,letters, and strings, are called constants because value
# does not change
# numeric constants does not need any format
print(123)
# string constants use single quotes (') or double quotes(")
print('hello world')
# variables is a named place in the memory where programmer can store data and leter retrieve the
# data using the variable name
# programmers get to choose the names of variables
# you can change the contents of a variable in a leter statement
x = 12
y = 13
print(x+y)
# variables name are case sensitive and needs to have letters and aplabets
# assignment statements use a variable to the left hand side nad equate a expression the right hand side.
# the (=) sign will put the value of the expression in the constant
z = 5*9+4*x
print(z)
# numeric symbols % = remainder and ** is power
q = x ** y
print(q)
a = y % x
print(a)
# when we use a lot of stings, python must know which string to use first. this is know as
# operator precedence = bodmass is maths or 1-parenthesis 2- power 3-multiplication
b = 4 + 5 * 6 ** 0 * (3 + 5) % 4
print(b)
# you can add even words
c = 'hi' + ' aarav'
print(c)
# integers are whole numbers like 1, 2 ,3  floating numbers have decimal points
d = 16
type(d)
e = 14.5
type(e)
# when u put a floating point and an interger in an expresion, the integer is converted to a floating
# point. you can convert the integer and floating point by (int) and by float()
f = int(e)
print(f)
g = float(d)
print(g)
# you can also use int() and float() to convert  strings  to integers
pan = '456'
pun = int(pan)
print(pun + 1)
# the input function can ask data from the user
name = input('whats your name? ')
print('welcome', name)
# by (#) we add a coment and python does not take that as a part of code
# Boolean expressions ask  a question and produce a yes or no result which we use to control program flow
# with the comparision operators and boolean exprssion, the question is answered in yes/tue or no/false
# comparison operators do no change the variable. (=) is used for assigment or like x is 5 or x is given
# that value. the signs in python are as follow- (<) = less than  (<=)= less than or equal to  (==) equal
# to (>=)greater than or equal to  (>)greater than (!=)not equal
j = 5
if j < 10:
    print('smaller')
if j > 20:
    print('bigger')
print('finish')
# in 2 way decisions, we want to do a thing if the exprssion is tru but if the exprssion is false the we
# want to do anather thing
if j > 2:
    print('bigger')
else:
    print('smaller')
print('all done')
# multiway is when there are many conditions and only 1 of the conditions happem
if x < 2:
    print('small')
elif x < 10:
    print('medium')
else:
    print('large')
print('all done')
# the try and except structure -  u pass a code to the try section and if it passes through the try
# section then it will skip the except section. but if it the try section fails then except is executed
astr = 'hello bob'
try:
    istr = int(astr)
except:
    istr = -1
print('first', istr)
# here 'hello bob cannot be converted to integer so it checks on try code so it executes the except code
astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('second', istr)
# over here instr is a integer so it will execute the try code
number = input('enter a number')
try:
    integer = int(number)
except:
    integer = -1
if integer > 0:
    print('nice work')
else:
    print('not a number')
# (def) is  a  function that will store a piece of code in a variable name and we can just put that
# variable name and that code will be executed.
def thing():
    print('hello')
    print('fun')
thing()
print('zip')
thing()
# the brackets after the variable name will store the code
# max is  the function that will find the largest letter in a sentence. note the lower case letter
# is bigger than upper case letter
big = max('hello world')
print(big)
# min is the function that will find the lowest letter/value form the piece of code
tiny = min('hello world')
print(tiny)
# the space is the lowest value so thats been displayed
# we create function using the def keyword followed by optional parameters in parentheses. indentation
# is very important and this function will just store the code in the keyword and will not execute it.
# an argument is a value we pass into the function as its input we call the function.
# arguments usually can give us different outputs from that same function. for eg 'hello world' in
# function max is the argument. we can change the output by changing the words hello word
# a parameter is a variable which we use in the function defination. it is a handle that allows the code
# in the function to access the arguements for a particular function invocation
def greet(lang):
    if lang == 'es':
        print('hola')
    elif lang == 'fr':
        print('bonjour')
    else:
        print('hello')
greet('en')
greet('es')
greet('fr')
# over here lang is the parameter and es is the arguement
# return values - often  a function will take its arguements, to do some computation, amd return a value
# to be used as the value of the function call in the calling expression. the return keyword is used for
# this
def greet(lang):
    if lang == 'es':
        return 'hola'
    elif lang == 'fr':
        return 'bonjour'
    else:
        return 'hello'
print(greet('en'), 'aarav')
print(greet('es'), 'anoushka')
print(greet('fr'), 'ridhima')
# a fruitful function is 1 that produces a result(or a retun value) and the retun function will end the
# execution of the function and will send back the result of the function
# loops have iteration variable that change each time through a loop. often these iteration variables
# go through a sequence of numbers.
n = 5
while n > 0:
    print(n)
    n = n - 1
print('blastoff')
print(n)
# Breaking out of a loop - the break statement ends the current loop and jumps to the statement
# following the loop
# it is like a loop test
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('done')
# so over here if the  word 'done' is written the the loop will break and the print executed
# continue command will execute the same loop and not go to the  outher loop
while True:
    line = input('> ')
    if line[0] == 'please':
        continue
    if line == 'done':
        break
    print(line)
print('done')
# over here if the word 'done' is printed then the loop is repeated and if the word done is not typed
# then the loop is finished
# definite loops have explicit iteration variables that change each time through a loop. these iteration
# variables move through a loop . these iteration variables moves through the sequence or set
for i in [5, 4, 3, 2, 1]:
    print(i)
print('blastoff')
# over here i is printed over 5 times, each time with a different variable
# so over here i is the iteration variable that will go through the sequence  and will execute a value
# each time  in the variable
largest_so_far = -1
print('before', largest_so_far)
for the_num in [9, 42, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('after', largest_so_far)
# over here  the_num is the variable and we have given the largest so far a number
zork = 0
print('before', zork)
for thing in [9, 42, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print('after', zork)
# to count the number of samples in a  range we introduce a counter variable and add 1 each time the
# loop goes in
zork = 0
pork = 0
print('before', zork)
for thing in [9, 42, 12, 3, 74, 15]:
    zork = zork + 1
    pork = pork + thing
    print(zork, thing, pork / zork)
print('after', zork)
# to sum up we just introduce a variable and just add each time
# for average we just divide the sum by count and we add that
# we add a if statement to filter or catch the output we want like if its bigger than 20
# we can add true or false values if we want to find out if that value is found or not
found = False
print('before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
print('after', found)
# none can be used if we dont want to give a variable a starting number like -1
smallest = None
print('before')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest == None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('after', smallest)
# is and is not can be used as an operater like a is 5 a is not 5 and is more stronger than ==
# strings are a sequence of characters that uses quotes
# for strings (+) means to concatenate and strings can have numbers that can be converted to integer
# by (int) function
# we prefer to read strings and then convert it to our liking
# looking inside strings- we can get at any single character in a string using an index specified in
# square brackets
# the index value starts at 0  and can put into an exprssion
fruit = "banana"
letter = fruit[1]
print(letter)
p = 3
k = fruit[p - 1]
print(k)
# u will get a error if u indent too much
# u can found out the lenght of a string by built in function len
print(len(fruit))
# a definite loop can be used over here
for letter in fruit :
    print(letter)
# the iteration variable iterates through the sequence  like letter over here and will move through all
# values in the sequences
# the nlock of code (print) statement is executed for each value
# slicing strings- we can look up to any continous section of a string using a colon operator
# the second number does not count
s = 'monty python'
print(s[0:4])
print(s[:4])
print(s[0:])
print(s[:])
o = 'hello'
op = o + ' ' + 'there'
print(op)
# the in keyword can also be used to check to see if one string is in anather string and in is a
# logical expression that return true or false and can be used in an if statement
'n' in fruit
if 'a' in  fruit:
    print('found it')
# python has a number of string functions which are in the string library. they do not modify the
# orignal string but they retun with a new string
meet = 'HELLO BOB'
zap = meet.lower()
print(zap)
# it makes the string into lower case
print('hi there' .lower())
# we use the find function to search for a substring within anather string and it will tell u the
# the position of the string and if it does not contain the subsrting it will return with a -1.
# string position starts with a 0
pos = fruit.find('a')
print(pos)
# u can make anything in upper case by using upper
keep = 'hello'
kkk = keep.upper()
print(kkk)
# the replace function will replace the old string with a new string
# it will replace all the occurnces with the new string
aaa = 'hello bob'
bbb = aaa.replace('bob','jane')
print(bbb)
ccc = aaa.replace('o','x')
# lstrip will remove the left place or the space at begining and rstrip will remove the space at the end
# and strip will remove both the spaces
ddd = '       hello bob   '
eee = ddd.rstrip()
print(eee)
fff = ddd.lstrip()
print(fff)
ggg = ddd.strip()
print(ggg)
# startswith is the string that helps to know if that word/sentence starts with a the letter/word
hhh = 'Hello'
hhh.startswith('H')
# class is a reserved word
class partyanimal:
    xxx = 0
    def party(self):
        self.xxx = self.xxx + 1
        print('so far',self.xxx)
an = partyanimal()

an.party()
an.party()
an.party()
# so the 0 is the list  and we are storing a list an is we are using the list. partyanimal is a template
# so the party is we are setting up a function like partyanimal.party(an)
# we are just basically adding a 1 whenever the program is being runned
# the dir() command listes capablities. ignore the ones with underscores as these are used by python itself
# the rest are real operations that the object can do. its like type, its tells abput  a variable
yyy = list()
type(yyy)
dir(yyy)
class partyanimal:
    xxx = 0
    def party(self):
        self.xxx = self.xxx + 1
        print('so far',self.xxx)
an = partyanimal()
print('type', type(an))
print('dir', dir(an))
# object lifecycle- objects are created,used and discarded
# we have special blocks of code (methods) that get called, the moment they are created- constructor
# at the moment of destruction (destructor)
# constructors are used a lot
# destructor are seldom used
# constructor- in object oriented programing, a constructor in a class is a special block of statements
# called when an object is created
# in many instances- we can create lots of objects- the class is the template for the object
# we can store each distinct object in its own variable. we call this having multiple instances of the
# same class. each instance has its own copy of the instance variables
# inheritance- when we make a new class, we can reuse an existing class and inherit all the capablities
# of an existing class and and then add our own little bit to make our own new class
# another form of store and  resuse. the new class has all the capablities of the old class and then some
# more
# another term that can be used is subclasses that are more specialised versions of a class which inherit
# attributes and behaviours from their parent classes, and can introduce their own
class partyanimal:
    xx = 0 #(variable)
    name = "" #(variable)
    def __init__(self,nam): # constructor and to grab that name paramenter
        self.name = nam
        print(self.name,'constructed')
    def party(self) : # it adds 1 and prints the party count
        self.xx = self.xx + 1
        print(self.name,'party count',self.xx)
class footballfan (partyanimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name,'points',self.points)
# class = a template
# attribute = a variable with a class
# method = a function within a class
# object = a particular instance of a class
# constructor = code that runs when an object is created
# inheritance = the ability to extend a class to make a new class
# relational database model data by storing rows and columns in tables.the power of the relational
# database lies in its ablity to effiently retrieve data from those tables and in particular where
# there are multiple tables and the relationships between those tables involved in the query
# terminology-
# database - contains many tables
# relation - contains tuples and attributes
# tuple(row) - a set of fields that generally represents an object like a person or a music track
# attribute (column)- one of possibly many elements of data corresponding to the object represented
# by the row
# a relation is defined as a set of tuples that have the same attributes. a tuple usually represents
# an object and imformation about the object. objects are typically physical objects or concepts. a
# relation is usually described as a table, which is organised into rows and columns. all the data
# referenced by an attribute are in the same domain and conform to the same constrains
# two large in large projects-
# application developer - builds the logic for the application, the look and feel of the application-
# monitors the application for problems
# database adminstrator - monitors and adjusts the database as the program runs in production
# database model/schema is the structure or format of a database,described in a formal language
# supported by the database management system,in other words a database maodel is the application
# of a data  model when used in conjunction with a database management system
# database design is an art form of its own with particular skills and experience. our goal is to avoid
# the really bad mistakes and design clean and easily understood databases.others may performance tune
# things later. database design starts with a picture
# building a data model
# drawing a picture of the data objects for our application and then figuring out how to represent the
# objects and their relationships
# basic rule- dont put the same string data in twice - use a relationship instead
# when there is a one thing in the real world there should be one copy of that thing in the database 



