###Introduction to Python programming

# Variables and Multiple Assignment

#Variables are useful for holding information. They are like boxes that store data.
#You can assign multiple variables at once using multiple assignment.
#You can also assign multiple variables to the same value by chaining assignments.

age = 20
print(age)

###

sentence = "my name is Dami"
print(sentence)

###

sarah, bob, mike = 16, 22, 17
print(sarah)
print(bob)
print(mike)

###

sarah = bob = mike = 17
print(sarah)
print(bob)
print(mike)

###

name, age = "Dami", 22
print(name)
print(age)




# Arithmetic Operators and Strings

#There are four arithmetic operators in Python:

#+ for addition
#- for subtraction
#* for multiplication
#/ for division

# Arithmetic operators:
# + - * / %

age1 = 12
age2 = 18

print(age1 + age2)
print(age1 * age2)
print(age1 / age2)
print(age1 % age2)                              #modulus provides the remainder of the operation
print(age2 % age1)   
###

sent1 = "today is a beautiful day"
print(sent1)

###

first_name = "Dami"
last_name = "Ajib"
print(first_name + last_name)                   # without space
print(first_name + " " + last_name)             # without space

###

print("hi" * 10)                                #printing a string multiple times

###

sent = "Dami was playing basketball"             #each character has an index (starting from 0)
print(sent[0])                                   #to get the first character
print(sent[0:4])                                 #Slicing is used to get a range of characters




# Placeholders in Strings

#There are three ways to substitute data into strings in Python:
#Concatenation uses the + operator to combine strings.
#Placeholders use the % operator to insert values into strings.
#Formatted strings use the f prefix to insert values into strings.

#e.g. to design an automated email system that sends out personalized messages to each recipient.
#you can create a generic messagee with placeholder for names and other specific details and python 
#would fill each with the appropriate data.
#placeholders are markers that stands in for some value.

name = "jake"
print(name + " is 15 years old")

###

name = "jake"                                           
sentence = "%s is 15 years old"                                                 #%s is the placeholder for strings
print(sentence % name)

###

sentence = "%s %s was the president of the United States"                       #%s is the placeholder for strings
print(sentence % ("Barack", "Obama"))

###

sentence = "%s is %d years old"                                                 #% is the placeholder for strings
print(sentence % ("Dami", 23))

###

name = "Dami"
print(f"Hello, {name}")                                                         #format strings: f{}

###

x = 10
y = 20
print(f"The sum of x and y is {x + y}")





###Task 1
#1. Write a script that adds 15 and 30 and divides the sum by 2. Print out the answer.
a = 15
b = 30

print ((a + b) /2)

#2. Initialize two variables and use arithmetic operators to add, subtract, multiply, divide, and find the remainder.
a = 15
b = 30
print (a + b)
print (a - b)
print (a * b)
print (a / b)
print (a % b)

#3. Create a variable called name and store your name in it as a string.
name1 = "Dami"
name2 = "Ajibuwa"
name = name1 + " " + name2
print(name)

#4. Create three variables in one line and assign each one a different food item.
fitem1 = "fruits"
fitem2 = "vegetables"
fitem3 = "cereals"
print(fitem1 + " " + fitem2 + " " + fitem3)
print(fitem1, fitem2, fitem3)


#5. Print out "Hello" ten times using arithmetic operators.
print ("Hello" * 10)

#6. Set your name and age variables in one line with multiple assignment
name1 = "Dami"
name2 = "Ajibuwa"
age = 23
name = name1 + " " + name2
print(name + " is", age)

#7. Create two strings and then create a third variable combining both of the two original strings.
name1 = "Dami"
name2 = "Ajibuwa"
name = name1 + " " + name2
print(name)

#8. Create a string and print the fourth letter of the word.
name1 = "Dami"
name2 = "Ajibuwa"
name = name1 + " " + name2
print(name[3])

#9. Create a string and print the letters from index 0 to 5.
name1 = "Dami"
name2 = "Ajibuwa"
name = name1 + " " + name2
print(name[0:6])

#10. Create a variable and print all the letters from the first index until the end.
name1 = "Dami"
name2 = "Ajibuwa"
name = name1 + " " + name2
print(name[1:])





# Introduction to Lists

#Use lists to store ordered sets of items. Lists are mutable, meaning you can change the items in a list after you create it.
#Lists are created using square brackets [].
#Items in a list are separated by commas ,.
#Lists can contain any type of data, including other lists.


#A list is a set of ordered items that have an index and you know the order based on the index
#e.g a shopping list
item1 = 'apples'
item2 = 'oranges'
item3 = 'bananas'
item4 = 'cheese'
#instead of creating lists of variables which is inefficient, create a list
###

shopping_list = ['apples', 'oranges', 'bananas', 'cheese']              #creating a list
print(shopping_list)
print(shopping_list[0])                                                 #index 0 is the first item
print(shopping_list[2])
print(shopping_list[0:2])                                               #Slicing doesnt count the end range
print(shopping_list[0:3])

###
#append: help to add to an existing list
shopping_list.append('blueberries') # add items
print(shopping_list)                                                    #to check
###
#to change/replace an item in a list
shopping_list[0] = 'cherries' # update items
print(shopping_list)

###
#del: to delete an item from a list
del shopping_list[1] # delete items
print(shopping_list)

###

print(len(shopping_list)) # length of list i.e. gives the number of items in a list

###

shopping_list2 = ['bread', 'jam', 'pb']
print(shopping_list + shopping_list2)                               #to add lists together
print(shopping_list * 2)                                            #you can repeat lists

###

list_num = [1,4,7,23,6]
print(max(list_num))                                        #maximum
print(min(list_num))                                        #minimum




# Welcome to Dictionaries!

#Dictionaries in Python are a collection of key-value pairs. They are unordered, changeable, and indexed.
#Dictionaries are written with curly brackets {}
#Have keys and values separated by a colon :.
#Each key-value pair is separated by a comma ,.

students = ['bob', 12, 'rachel', 13, 'emily', 15]
print(students)
#instead of using list which is efficient, create dictionaries.
#e.g a class of students with unique name and age. to find a students e.g age without locating the name
###

students = {'bob': 12, 'rachel': 13, 'emily': 15}           #creating a dictionary with the student name as KEY and the age as VALUE
print(students)
print(students['rachel'])
print(students['bob'])

###

students['rachel'] = 14                                     #to update an existing data in a library E.g rachel tuurns 14
print(students)

### 

del students['emily']                                       #to delete data, e.g emiily leaves thhe school
print(students)

###

print(len(students))

###

students = {'bob': 12, 'bob': 13, 'bob': 15}                #NB: keep key unique since python doesnt know which e.g. bob you need  
print(students)




# Introduction to Tuples

#Tuples are similar to lists, are sequential, but they are immutable. 
# This means that once you create a tuple, you cannot add, remove or change elements. 
#Tuples are created using parentheses ().
#Items in a tuple are separated by commas ,.
#Tuples are useful for consistency, safety

tup = ('oranges', 'apples', 'bananas')
print(tup)
# tup[0] = 'cherries'                                       #this returns an error messageUncomment to see error.
print(tup[0:2])                                             #Slicing is possible in tupples

###

tup2 = (12, 14) 
tup3 = tup + tup2                                           #concatenation is possible with another tuple
print(tup3)



###Tasks 2

#1. Create a list of names and print the second item.
names_list = ["clementina", "Thaminah", "Oyeyimika", "Abass", "Mutiat"]
print(names_list)
print(names_list[1])

#2. Create a list of sports and then replace the second item with another sport.
sports_list = ["Taekwondo", "Football", "Badminton", "Jiujitsu", "Badminton"]
print(sports_list)

sports_list[1] = "volleyball"
print(sports_list)

#3. Create a list containing numbers and delete the fifth number from the array.
numbers_list = [6, 11, 12, 13, 41, 42, 22, 61, 62, 81, 91, 201]
print(numbers_list)

del numbers_list[4]
print(numbers_list)

#4. Create two lists of numbers and merge them.
numbers_list1 = [6, 11, 12, 13, 41, 42]
print(numbers_list1)

numbers_list2 = [22, 61, 62, 81, 91, 201]
print(numbers_list2)

numbers_list = numbers_list1 + numbers_list2

print(numbers_list)

#5. Create a list of numbers and find the length, minimum, and maximum.
numbers_list1 = [6, 11, 12, 13, 41, 42]
numbers_list2 = [22, 61, 62, 81, 91, 201]

numbers_list = numbers_list1 + numbers_list2
print(numbers_list)

print(len(numbers_list))
print(max(numbers_list))
print(min(numbers_list))

#6. Create a dictionary of students and scores and print out a student’s score.
scores_list = {"Andre" : 56, "Sunday" : 51, "Loveth" : 67, "James" : 73, "Jacky" : 61, "Bastien" : 42}
print(scores_list)

print(scores_list ["James"])

#7. Create a dictionary with the key being names and values being ages and then delete the second key/value pair.
nameages_list = {"Andre" : 56, "Sunday" : 51, "Loveth" : 67, "James" : 73, "Jacky" : 61, "Bastien" : 42}
print(nameages_list)
del nameages_list["Sunday"]
print(nameages_list)

#8. Create a dictionary of names and ages and then print out all the keys and values
name_ages_list = {"Andrew" : 56, "Anderson" : 51, "Christabel" : 67, "Jamal" : 73, "Jamil" : 61}
print(name_ages_list)
#print(name_ages_list.keys)
#print(name_ages_list.values)

#9. Create a tuple of your favorite movies
tup = ["Inception", "The Imitation Game", "Vikings", "Money Heist", "Merlin", "Jumong", "Battleship"]
print(tup)

#10. Create a tuple and print all the items from the first to third index.
tup = ["Vikings", "Money Heist", "Merlin", "Jumong", "Battleship"]
print(tup)
print(tup[0:2])



# Conditional Statements

#Conditional statements are used to execute code based on certain conditions. 
# it operates on if (a condition is met) -else(alternative if condition is not met) principle.
#indentation by 1 tabspace is important.
#In Python, we have the following conditional statements:
#if statement
#elif statement
#else statement


if 5 > 3:                                      
  print("hello")
  
###

if 3 < 2:
  print("hello")
else:
  print("condition was not true")

#conditions are built using relational operators

# relation operators
# > < >= <= == !=

# Uncomment the below to see the error
# if 5 = 3:                                             #because = is assinment sign and not for comparism
#   print('hello')
if 5 = 3:
   print('hello')
###

if 5 == 3:
  print('hello')
  
###

age = 16
if age <= 15:
  print("You are younger than 16")
elif age == 16:                                         #elif helps to create multiple if statements within a block
  print("You are 16")
elif age == 17:
  print("You are 17")
else:
  print("You are older than 16")
  
###

#with logical operators we can chain multiple conditions together, e.g if something is within a range
age = 16
if age < 13:
  print("You are a child")
elif age >= 13 and age < 18:                                    #AND operator: both conditions should be true
  print("You are a teenager")
else:
  print("You are an adult")


###

if 5 > 3 or 2 < 1:                                              #OR operator: at least one condition is true
  print("hi")




# Introduction to FOR Loops

#For loops allow us to run a piece of code repeatedly.
#For loops are created using the for ... in syntax.
#We can use for loops to iterate over a sequence of items, such as a list or a tuple.
#We can use the range() function to generate a sequence of numbers.

#For loop: is good for iterating over data structures or navigating through a data structure 
#and performing operations on each items e.g printing, modifying, or extracting information.
list1 = ['apples', 'bananas', 'cherries']                   
tup1 = (2, 6, 10)

for item in list1:                                          #e.g to print every value in a list or in a tuple
  print(item)
  
for item in tup1:
  print(item)
  
###

for i in range(0, 10):                                      #the range index does not include the end index
  print(i)

###

for i in range(1, 11):                                       #e.g print 1 to 10
  print(i)
  
###

for i in range(0, 11, 2):                                   #the range function can skip numbers, 2 is the increment factor
  print(i)                                                  #simply even numbers

###

for i in range(5, 51, 5):                                   #e.g. print the first 10 multiples of 5
  print(i)

###

for i in range(0, 5):
  print(i)

###

for i in range(0, 5):                       #e.g to iterate through the first 5 numbers and then multiply each of those numbers by 0 1 2
  for j in range(0, 3):
    print(i * j)




# Introduction to While Loops

#While loops allow us to run a piece of code repeatedly, i.e it keeps executing, as long as the conditions are true.
#While loops are created using the while keyword.
#Runs repeatedly as long as a condition is True.

#while loops and control statements: e.g a home automation system that needs to regulate heating based on the room's temperature 
c = 0                                               
while c < 5:                                        
  c = c + 1
  print(c)
  
###

#control statement can alter the usual flow of execution in loops
#3 primary control statements: BREAK, CONTINUE, PASS

c = 0
while c < 5:
  c = c + 1
  if c == 3:                                    
    break                                             #to terminate a loop prematurely e.g.when you reach a desired outcome and want to exit the loop
  print(c)

###

c = 0
while c < 5:
  c = c + 1
  if c == 3:
    continue                                         #to continue running a loop, but skips the rest of the current iteration (c=3) and moves onto the next iteration
  print(c)

###

c = 0
while c < 5:
  c = c + 1
  if c == 3:
    pass                                            #is a do-nothing command, it serves as a placeholder to structuure your code when you haven't decided what to go in the block yet
  print(c)





# Try and Except

#Try-except blocks allow us to catch errors in our code.
#Use try ... except to catch exceptions.

#is a control flow used when dealing with codes that might possibly raise exceptions
#e.g fetching data from a website or calling API, and there is a possibility of the webside being down or the API not functioning as expected 
#if the TRY block encounters any error duuring execution, the control gets passed over to the EXCEPT block

try:
  if name > 3:
    print("hello")
except:
  print("An error was detected in your code")

#try:
#  if 5 > 3:
    print("hello")
#except:
#  print("An error was detected in your code")




# Welcome to Functions!

#So far we have used functions. We can also define our own functions.

#Define functions using the def keyword.
#Functions can take arguments.
#Functions can return values.

#functions promote code-reuse and thereby enhacing the efficiency and compactness of a code
#e.g a baker that follows a specific set of steps in making a particular bread
#so this means you can create a function with the set of steps, so you just 
#call the function instead of writing the steps everytime you want to make the bread.
def hello_world():                                      #in this case the () is empty because there is no need for any input parameters
  print("Hello World")                                  #no output because the function is defined but not explicitly called
  
hello_world()                                           #here, there is an output when the function is invoked

###

#e.g. a function that takes a username as input and greets them

def greeting(name):
  print("Hi " + name + "!")

greeting("Dami")

###

def add(num1, num2):                                    #e.g. a function that adds two numbers and prints their sum
  print(num1 + num2)

add(10, 15)

###
# return statement to save the output or result of the function instead of printing it

def add(num1, num2):
  return num1 + num2                                   #return passes back the result of the computation and we can then save the result to a new variable            

num_sum = add(12, 34)
print(num_sum)

def mul(num1, num2):                                        #to chain more functions i.e. a function as an input of another
  return num1 * num2
  print("hello") # would not be run

print(mul(add(1, 2), add(3, 4)))




# Built-in Python Functions

#Python has many built-in functions that we can use.

#abs() - Return the absolute value of a number.
#dir() - Return a list of attributes and methods of an object.
#help() - Get help on a function.
#bool() - Convert a value to a boolean.
#int() - Convert a value to an integer.
#float() - Convert a value to a float.
#str() - Convert a value to a string.

print(abs(-23))
print(bool(0))
print(bool(100))
print(bool(None))
print(dir('hello'))                             #it shows all the methods you can use with a particular object
print(help('hello'.upper))                      #it shows more details of a specific (e.g upper) methods you can use with a particular object

###

sent = "print('hi')"                            
eval(sent)                                      #to run Python code disguised as a string
exec(sent)                                      #to execute strings of codes spanning multiple lines

###
#type conversion functions convert data types
print(str(100))
print("hello " + str(100))
print(int("123") + 456)
print(float("123.45") + 0.23)

###Task: Factorial Generator: Calculate the Factorial of a Number

#Instructions:

#1. Define a function called `calculate_factorial` that takes in one parameter, `number`.
#2. Inside the function, write code to calculate the factorial of the given number.
#3. The factorial of a number is the product of all positive integers less than or equal to that number. For example, the factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.
#4. You can use either loops or recursion to calculate the factorial.
#5. Return the factorial as the output of the function.

#solution: iterative approach (preferably for large n)
#The function factorial_iterative initializes a result variable to 1.
#It then multiplies this result by each integer from 1 up to n.
#The final result is returned as the factorial of the number.
def calculate_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(calculate_factorial(5))

#solution: recursive approach
#The function factorial_recursive checks if n is 0 or 1. If so, it returns 1 because the factorial of 0 and 1 is 1.
#For any other positive number, it returns n multiplied by the factorial of n-1, thus breaking the problem into smaller subproblems.
def calculate_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)

print(calculate_factorial(5))



#object oriented programming
# OOP - Classes and Objects

#The object-oriented programming (OOP) paradigm is based on the concept of "objects".
#Objects are instances of classes, which are templates for creating objects.
#Classes define the properties and behaviors of objects.

#Dammy think:
#class: Dog (the class defines what a dog is) 
#property: the properties of the class includes: name, breed, age, behaviours 
#methods: behaviours are methods in programming terms: bark, eat, sleep 
#but the class is just a concept and it doesn't bark or sleep, meaning it merely describes what a dog is or can do 
#Object: is an instance of a class e.g. Fido and Buddy have the properties of a dog like name, and behaviour like bark eat and sleep
#however Fido and Buddy are distinct entities with different properties:
#e.g Fido, 3yr, german shepherd; Buddy, 5yr, golden retriever


#first of all, real world modeling classes and objects help model real world concepts into code, making it easier to understand and work with.
#Second, reusability. Once you've made a dog class, you can create as many dog objects as you need, saving you the effort of defining dogs again and again.
#last, organization. It helps you organize and structure your code better by creating a class dog.
#you can use it to create any number of dog objects, each with its own set of attributes and behaviors.

#This is the essence of object oriented programming. It allows you to create structured, reusable, and intuitive code.

        #First, let's think of a class as a blueprint or a plan. Example: a person.
        #This person blueprint is our class, and it can contain some basic information that every person has,like a name and an age.
        #But right now it's just a blueprint. It's not a specific person, just a general idea of what a person is.


class Person:                                                       #to define a class/blueprint
  pass

p = Person()                                                       #p is object #to create a specific person /an instance of the person:class/person:object
print(p)

###

class Person:                                                       
  def __init__(self, name, age):               #--init--: to define attributes when creating a new person:object
    self.name = name                           #self keyword is a reference to the current instance of the class and it is used to access its attributes
    self.age = age                             #name and age are the parameters passed in to define what the objects name and age would be 
  
  def getName(self):                           #methods: are functions defined inside a class that performs actions related to the object of the class
    return self.name                           
  
  def getAge(self):
    return self.age

p1 = Person("Bob", 22)                         #Bob and 22 are the attributes of the P1 object
print(p1)
print(p1.getName())                            #to find out the name and age of P1, we simply call these methods on the p1 object
print(p1.getAge())

#object oriented programming in Python is all about creating classes, which are blueprints and objects which are instances of these blueprints.
#It allows us to structure our code in a way that is easy to understand and reuse, mirroring how we categorize and think about the world around us.




# OOP - Class Inheritance

#Inheritance is a powerful feature of object-oriented programming (OOP) that allows us to create new classes based on existing classes.
#The new class is called a "subclass" or "child class".
#The existing class is called a "superclass" or "parent class".


#Dammy think:
#Imagine a car manufacturing company. They make a base model car with common features like an engine, wheels, seats, and so on.
#Now they also produce variations of this base model, such as a sports version with a more powerful engine, or a luxury version with high end seats.
#These variations inherit the common features from the base model, but also add or modify some features.
#That's exactly how inheritance works in programming for classes two.

class Car:                                                      #to create a base class.   
  def __init__(self):                                           #to define attributes of the base class object
    self.wheels = 4
    self.seats = 5
   
  def drive(self):                                              #method: drive
    print("Driving a car...")
    
myCar = Car()                                                   #to define an instance of car
myCar.drive()

###

#to create a sporty car class that inherits from the car class
#the sporty car class would have a more powerful engine and fewer seats
class SportsCar(Car):                                           #in parenthesis is the class you are inheriting from i.e.the car class
  def __init__(self):
    super().__init__()                                          #super: to execute the --init-- method of the parent car class, ensuring we don't lose the attributes initialized there.
    self.engine_power = '400 HP'                                #the sportcar class adds a new attribute called the engine power
    self.seats = 2                                              #the sportcar class modifies the seats attribute
    
  def drive(self):
    print("Driving a sports car...")                            #method: reinitializing the drive function to read...driving a sport car
    
mySportsCar = SportsCar()                                       #to create sport car object
mySportsCar.drive()                                             #to call the sport car method

###

#NB: result If we didn't specify the drive method in sports car
class SportsCar(Car):
  def __init__(self):
    super().__init__()
    self.engine_power = '400 HP'
    self.seats = 2
    
mySportsCar = SportsCar()
mySportsCar.drive()

#three key reasons why class inheritance is important
#1. reusability of code. In our car example, we didn't have to rewrite the attributes for wheels and seats for the sports car. We could inherit them from the car class. 
#2. This also allows for easy maintenance and updates. If we wanted to change a common feature across all car types, we just need to change it in the car class and the subclasses will inherit the changes.
#3. organized structure.It makes logical sense to have a base car class and then subclasses for different types of cars. It makes our code easier to understand and manage.










