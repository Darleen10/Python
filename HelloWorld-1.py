
# introduction to python: first program
print ("Hello World!")


# python Syntax: Data types
print (type ("a"))
print (type (2))
print (type (2.5))           


# python Syntax: Variables
length = 10                                             # assignment
width = 2
area = length * width                                   # expression
print (area)


# python Syntax: Expressions, Numbers, and Type Conversions
print (7 + 8.5)                                         # implicit conversion
print ("a" + "b" + "c")
print ("This" + "is" + "pretty" + "neat!")              # Hinweis: remember to add space
print ("This " + "is " + "pretty " + "neat!")      

# python Syntax: Expressions, Numbers, and Type Conversions
base = 6                                                # assignment
height = 3
area = (base * height)/2                                  # expression
print ("The area of the triangle is: " + str(area))     # str() function converts the area to a string


# The following lines assign the variable to the left of the = 
# assignment operator with the values and arithmetic expressions 
# on the right side of the = assignment operator.
hotel_room = 100
tax = hotel_room * 0.08
total = hotel_room + tax
room_guests = 4
share_per_person = total/room_guests 
# This line outputs the result of the final calculation stored
# in the variable "share_per_person"
print("Each person needs to pay: " + str(share_per_person)) # change a data type


# The following 5 lines assign strings to a list of variables.
salutation = "Dr."
first_name = "Prisha"
middle_name = "Jai"
last_name = "Agarwal"
suffix = "Ph.D."
 print(salutation + " " + first_name + " " + middle_name + " " + last_name + ", " + suffix) 
# The comma as a string ", " adds the conventional use of a comma plus a 
# space to separate the last name from the suffix.
# Alternatively, you could use commas in place of the + connector:
print(salutation, first_name, middle_name, last_name,",", suffix)
# However, you will find that this produces a space before a comma within a string.



