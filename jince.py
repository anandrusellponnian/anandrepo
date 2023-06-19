#To find Area of Rectangle

##length=4
##breadth=7
##result=length*breadth
##print("Area of Rectangle is:",result)
#......................Airthematic operators..............
##a=10
##b=5
##print("Add of two numbers:",a+b)
##print("Sub of two numbers:",a-b)
##print("Mul of two numbers:",a*b)
##print("Div of two numbers:",a/b)
##print("Modulus of two numbers:",a%b)
##print("Exponent of two numbers:",a**b)
##print("Floor division of two numbers:",a//b)

#......................Comparision operators................
##a=10
##b=5
##print("a is greater:",a>b)
##print("b is lesser:",b<a)
##print("a is equal to b:",a==b)
##print("a is not equal :",a!=b)
##print("a is greater than or equal :",a>=b)
##print("b is lesser than or equal:",a<=b)
#...................................Assignment Operators.........
##a=10
##b=5
##c=a+b
##print("The value of c is:",c)
##c+=b#c=c+b#c=15+5=20
##print("The value of c is:",c)
##a-=c#a=a-c#a=10-20=-10
##print("The value of a is:",a)
##c*=b#c=c*b,c=20*5
##print("The value of c is:",c)
##a/=b
##print("The value of a is:",a)
#................................Bitwise operators...............
##a=10
##b=4
##print("a AND b is:",a&b) 
##print("a OR b is:",a|b)
##print("a XOR b is:",a^b)
##print("a RightShift b is:",a>>2)
##print("a LeftShift b is:",a<<2)
##print("Not of a is:",~a)

#...................................Logical Operators..............
##a=True
##b=False
##print("a AND b is:",a and b)
##print("a OR b is:",a or b)
##print("a Not b is:",not a)

#...................................python input()................
##def:Python input() function is used to get input from the user.##
#....ex program....
##a=input()
##print(a)
##b=input("enter the number or name")
##print(b)
##c=int(input("enter the number"))
##print(c)
#..........................................python Numbers..........
#def:Number data types store numeric values
##There are three numeric types in Python:
##1.int
##2.float
##3.complex
#.......ex program.......
##a=6
##print(type(a))
##a=6.9078
##print(type(a))
##a=6+4j
##print(type(a))
##a="Jince"
##print(type(a))
##a=10
##print(bin(a))

#.............................................python String..................
# def:set of charecter is called string .Python allows both single
#or double or triple quotes.
##a="Welcome to"
##print(a)
##print(a+" "+"Networkz System")
##print(a*2)
##print(a[7])
##print(a[3:])
##print(a[:3])
##print(a[3:8])
#.........................String Built in Function...........
##a="welcome to"
##print(a.capitalize())
##print(a.upper())
##print(a.lower())
##print(a.title())
##print(len(a))
##print(min(a))
##print(max(a))
##print("a".join(a))

#.................................Python List......................
##Def:List is a data type.Multiple different values are stored in single variable is called List.
##List is denoted by square bracket([]).It is a insersion order.It is a muttable object
#.....ex program...
##list=["hi",1,2,"hello","how","are",4,5]
##print(list)
##list1=["apple","mango",8]
##print(list+list1)
##print(list*2)
##print(list[3])
##print(list[3:])
##print(list[2:8])
##list[6]="you"#update
##print(list)
##del list1[1]#delete
##print(list1)
#...................list built in functions.......

##list=["hi",1,2,"hello","how","are",4,5]
##list1=[1,2,3,4,5]
##print(len(list))
##print(min(list))# error not support in int or str
##print(min(list1))
##print(max(list1))
#.......list methods.........................

##list1=[1,2,3,4,5,3]
##x=list1.count(3)
##print(x)
##list1.append(7)
##print(list1)
##list1.extend([8,9,10])
##print(list1)
##print(list1.index(4))
##list1.remove(3)
##print(list1)
##list1.reverse()
##print(list1)

#...........................................Python Tuples............
#def:Tuple is a data type.Multiple different values are stored in single variable
#is called Tuple.It is denoted by round bracket.
#It is immutable object(cannot update or change the values of tuple elements.)
#It is maintain insertion order

#....ex program.......
##tuple=("hi",1,2,"hello","how","are",4,5)
##print(tuple)
##tuple1=("apple","mango",8)
##print(tuple+tuple1)
##print(tuple*2)
##print(tuple[3])
##print(tuple[3:])
##print(tuple[2:8])

#..........built in tuple fuction.....
##tuple=("hi",1,2,"hello","how","are",4,5)
##tuple1=("a","b","c")
##print(len(tuple))
##print(max(tuple1))
##print(min(tuple1))
#.....list to tuple convert
##list1 = ['a', 'W', 'F']
###convert list into tuple
##tuple1 = tuple(list1)
##print(tuple1)
##print(type(tuple1))

#..................................python set................................
#def:Set is unordered collection of unique items.Items are seperated by comma
#It is denoted by curly braces.It not maintain insertion order(ie:random order)
##set={"a","b","c"}
##print(set)

#...................................python dictionary.........................
##def:Dictionary are used to store data values in key:value pairs.Each key is separated
##from its value by a colon (:),the items are separated by commas,
##and the whole thing is enclosed in curly braces.
###....syntax:{ key : value } pair
#A dictionary is a collection which is ordered*, changeable and
###do not allow duplicates.

#....ex program.....
###Print the "brand" value of the dictionary:
##
##thisdict = {
##  "brand": "Ford",
##  "model": "Mustang",
##  "year": 1964
##}
##print(thisdict["brand"])
##
#####...Duplicates Not Allowed...
##thisdict = {
##  "brand": "Ford",
##  "model": "Mustang",
##  "model":"App",
##  "year": 1964,
##  "year": 2020
##}
##print(thisdict)
##
#######....change value.....
#######Change the "year" to 2018:
##thisdict ={
##  "brand": "Ford",
##  "model": "Mustang",
##  "year": 1964
##}
##
##thisdict["year"] = 2018
##
##print(thisdict)
####
#######...Update Dictionary...
#######Update the "year" of the car
#######by using the update() method:
##thisdict = {
##  "brand": "Ford",
##  "model": "Mustang",
##  "year": 1964
##}
##thisdict.update({"year": 2020})
##
##print(thisdict)
#######.....Adding Items....
#######Adding an item to the dictionary is
######done by using a new index key and
#######assigning a value to it:
##thisdict = {
##  "brand": "Ford",
##  "model": "Mustang" ,
##  "year": 1964
##}
##thisdict["color"] = "red"
##print(thisdict)
#................................Programing concept in python..................
##1.Conditional Statement
##2.Looping Statement
##3.Loop control Statement

#.................Conditional Statement.....................
##def::A conditional statement as the name suggests itself, is used
##to handle conditions in your program. These statements guide the program
##while making decisions based on the conditions encountered by the program.
#...................What are the conditional Statements............................
##1.if stmt
##2.if-else stmt
##3.elif stmt
##4.Nested stmt(if,if-else)

#.......if Statement..............
##def::The if statement is used to decide whether a particular block of code will be
##exceuted or not based on certain condition.If  statement condition true means
##then the code is executed otherwise not executed
##.......Syntax if statment:........

##Syntax:
##	if condition:
##		Statement(s)
##If the expression evaluates to TRUE, then the block of statement(s) is executed.
##If the expression evaluates to False, the statement(s) is not executed.

#.......ex program largest three number..................
##a=(input("Enter the first number:"))#5
##b=(input("Enter the second number:"))#6
##c=(input("Enter the third number:"))#7
##if (a>b)&(a>c):
##    print("a is greater")
##if (b>c) &(b>a):
##    print("b is greater")
##if (c>a) &(c>b):
##    print("c is greater")
#.....ex prog to print positive or negative or zero....
##a=int(input("enter the number:"))
##if a==0:
##    print("enter the number is zero")
##if a>0:
##    print("enter the number is positive")
##if a<0:
##    print("enter the number is negative")


#...........if - else statement.............
##Syntax:
##	if condition:
##		Statement(s)
##	else:
##		Statement(s)

##If the condition is TRUE, then if block of statement(s) is executed.
##If the condition is False, the else block of statement is executed.

#.....ex programm: to find the given number is even or odd........

##a=int(input("Enter the number:"))
##if a%2==0:
##    print("Enter the number is even")
##else:
##    print("Enter the number is odd")
    
#.......................Elif(else -if)Statement....................

##1.The elif is short for else if. It allows us to check for multiple conditions.
##2.If the condition for if is False, it checks the condition of the next elif block and so on.
##3.If all the conditions are False, the body of else is executed.
##4.The if block can have only one else block. But it can have multiple elif blocks.
##Syntax:
##	if condition1:
##		statement(s)
##	elif condition2:
##		statement(s)
##	elif condition3:
##		statement(s)
##	else:
##		statement(s)

#.......ex program check the browser name.......................
##browser=input("Enter the browser:")
##if(browser=="chrome"):
##    print("Browser name is chrome")
##elif(browser=="safri"):
##    print("Browser name is safri")
##elif(browser=="Edge"):
##    print("Browser name is Edgei")
##elif(browser=="Firefox"):
##    print("Browser name is firefox")
##else:
##    print("Enter the browser name is not here")

#........Nested if statement.......
#Def:if statement inside another if statement is called Nested If Statement
##Syntax:
##if (condition1):
##   # Executes when condition1 is true
##   if (condition2): 
##      # Executes when condition2 is true
##   # if Block is end here
### if Block is end here

#........ex program.........
##a=int(input("Enter the number"))
##if(a>=0):
##    if(a==0):
##        print("Zero")
##    else:
##        print("positive number")
##else:
##    print("negative number")

#....................................Looping Statement........................
##def:Looping statements in python are used to execute
##a block of statements or code repeatedly for several
##times as specified by the user
###......Types.........
##1.while Loop
##2.For loop
##3.do -while loop
#.........................while loop.........
##def::While loop in python is used to execute multiple statements
##or codes repeatedly until the given condition is true.
## Syntax:
##     while (condition):
##         #block of statement

#......ex program..............
##a=int(input("Enter the number"))
##i=0
##while(i<a):
##    print("The count is::",i)
##    i+=1#i=i+1
##print("end of program")

#............................for loop...............  
##def::The for loop in Python is used to iterate over a
##sequence (list, tuple, string) or other iterable objects. 
##Syntax:
##	for val in sequence:
##		body of for loop
##Here, val is the variable that takes the value
##of the item inside the sequence on each iteration.
##Loop continues until we reach the last item in the sequence 
##

#..........star pattern program using range function.........
##a=int(input("Enter the rows:"))#5
##for i in range(0,a):#0,1,2,3,4
##    for j in range(0,i+1):
##        print("*",end=" ")
##    print()
    
#......continue........

##a="students"
##for i in a:
##    if i=="e":
##        continue
##    print(i)
        
#..........break.....
##a="students"
##for i in a:
##    if i=="e":
##        break
##    print(i)

#........pass........
##str='networkzsystems'
##for letter in str :
##    print("letter:",letter)
####    pass
##print(' Letter :', letter)
#.....another ex program....
##list = [ 1, 2, 4, 3, 6, 5, 7, 10, 9 ]
##for number in list:
##    if(number % 2 ==0):
##        
##        pass
##    else:
##        print('Current number is:', number)


#.....................................Function in python...........
#........USER DEFINED FUNCTIONS.................
##Def::In Python, a user-defined function's declaration begins with the
##keyword def and followed by the function name.
##The function may take arguments(s) as input within
##the opening and closing parentheses, just after
##the function name followed by a colon.
#....Syntax.........
##def function_name(argument1, argument2, ...) :#defined function
##      statement_1
##      statement_2
##      ....
##function_name(argument1, argument2, ...)#calling function name

#.......ex prog.....To find the average of two numbers....
##def averageNumber(a,b):
##    print("Average of a and b is:",(a+b)/2)
##averageNumber(4,6)
#...addition of two number using function.....
##def addition(a,b):
##    return (a+b)
##print("Addition of a and b value is:",addition(3,4))

#.......return statement.....
##def returnstmt(a):
##    return 4*a
##print(returnstmt(2),",",returnstmt(5))

#.....another ex..
##def conversion(a):
##    if(a==1):
##        return "one"
##    if (a==2):
##        return "two"
##    if (a==3):
##        return "three"
##    if (a==4):
##        return "four"
##n=int(input("Enter the number 1 to 4"))
##print(n,"in words",conversion(n))
#.......keyword arguments.............
##def volume(length,breadth=5,height=4):
##    print("volume of cube is",length*breadth*height)
##volume(2)
##volume(3,4)
##volume(4,5,6)

#..........Global variable....
##def::variables that are declared outside of a function are known as global variables.
##
##You can access global variables in Python both inside and outside the function.  

#.....ex program in global variable in function outside....
##a="Welcome to all"
##def globalv():
##    print("Global variable value is:",a)#access global variable in inside
##globalv()
##print("Global variable value is:",a)#access global variable in outside


#............Local variable......
##def::variables that are declared inside of a function are known as local variables.
#We cannot access them outside the function.
#..........ex program...
##def greeting():
##    message="Happy BirthDay"
##    print("Hi shalu,",message)#access local variable in inside
##greeting()
##print("Hi shalu,",message)# we cannot access local variable in outside,name error come
##

##..........Recursion using factorial......
##def factorial(n):  
##        if n==0:  
##            return 1  
##        else:  
##            return n*factorial(n-1)  
##  
##num = int(input("Enter a number: "))  
####print("The factorial of a {0} is: ".format(num), factorial(num))
##print("The factorial of a ",num ,"is: " ,factorial(num))

#....................Module.....................................
##1.A module is a file consisting of a few functions and variables used for a particular task.
##2.A module can be reused in any other program that imports it.
##3.To import a module, use the import statement.
#.......example..............
#............1.The from import statement.........................
##from math import sqrt,factorial
##print(sqrt(10))
##print(factorial(5))
#......import *......
##from math import *
##
##print(sqrt(10))
##print(factorial(5))
##print(pow(2,3))

#...........import calendar....
##import calendar
##print("June Month 2023")
##print(calendar.month(2023,6,4,3))

#....import date and time..............
##import datetime
##x=datetime.datetime.now()
##print(x)

#.....To find day in that year.............
##import datetime
##x=datetime.datetime(2024,1,12)
##print(x.strftime("%A"))
#.....To import random number....
##import random
##x=random.randint(1,50)
##print(x)

#..... To take month and year input from the user
##import calendar
##yy = int(input("Enter year: "))
##mm = int(input("Enter month: "))
####display the calendar
##print(calendar.month(yy, mm))

#......................Object Oriented Programing language............
#......create class and object with two attribute.......
##class rectangle:
##    length=4
##    breadth=5
##    result=length*breadth
##objectrect=rectangle()
##print("Area of rectangle is:",objectrect.result)
#.........call instance variable in class and method.....
##class student():
##    def getDetail(self,id,name,place):
##        self.id=id
##        self.name=name
##        self.place=place
##        print("Student id is:",id)
##        print("Student name is:",name)
##        print("Student place is:",place)
##obj=student()
##obj.getDetail(1,"shalini","Kl")





    










































    














