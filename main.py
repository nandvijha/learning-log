#This is my first Python program
print("Hey, girl!")
# Variable = A container for a value (string, integer, float, boolean)
# A variable behaves as if it was the value it contains.
# (so, from what I understood, a variable is basically assigned value)
print("")

#Strings : within quotes
first_name = "Nandvi" #string
print(f"Hello, {first_name}!") #used an f-string (formatted string).
food = "apples" #string
print(f"Do you like {food}?") #f-string = syntax for embedding variables, expressions, etc.
email = "nvj098123@gmail.com" #string
print("What's your email?")
print(f"My email is {email}.")
print("")

#Integers
age = 19 #Int is not shown with quotations.
print(f"I am {age} years old.")
quantity = 3 #Ints has to be in complete whole numbers
print(f"I would like {quantity} {food}.")
num_of_family_members = 4
print(f"I have {num_of_family_members} family members.")
print(f"They all like {food}.")
#Integers are used in arithmatic expressions, strings are not, not even with numbers as numbers with quotation("") will be strings.
print("")

#Float: Floating point numbers (decimals)
price = 10.99
print(f"The price of {food} is ${price}.")
gpa = 8.7
print("By the way, what was your GPA this year?")
print(f"My gpa is {gpa}.")
print("How much do you run daily?")
distance = 7.5
print(f"My distance is {distance} kilometers.")
print("")

#Boolean: true or false
is_student = True #True or False starts with a capital, always.
print(f"Is {first_name} a student?: {is_student}.")
#Boolean is usually used for "if" or "else" situation.
if is_student: #For true case
    print("You are a student.")
else: #For false case
    print("You are not a student.")
for_sale = False
print(f"Are {food} for sale?")
if for_sale:
    print("Yes, they are.")
else:
    print("No, they are not.")
#Variable: Done.
print("")

#Typecasting = the process of converting a variable from one data type to another
#              str(), int(), float(), bool()
name = "Nandvi Jha"
age = 19
gpa = 8.7
is_student = True
print(type(is_student)) #Can't use type() syntax b'cos it doesn't work. Need to use it with print syntax.
#type() syntax with print identifies type of data/variable input.
#Let's convert the variable now
gpa = int(gpa)#float to integer
print(gpa)
age = float(age)#integer to float
print(age)
age = str(age)#float to string
print(age)
print(type(age))#can confirm the changes with this function
name = bool(name)
print(name)
#If I forgot to put my name, boolean will come as false. Thus, I can check user if the put there name or not. Helpful in handling user input as it is a string, always.
print("")

#(User) input() = A function that prompts the user to enter data
                 #Returns the entered data as string.
name = input("What is your name?")
age = int(age) #This is extra line. No need for this. Instead:
age = int(input("How old are you?")) #We can do this and it works the same.
age = age + 1 #We can use str() with arithmatic operations. Change it to int or float.
print(f"Hello,{name}!")
print("Happy birthday!")
print(f"You are {age} years old.")
print("")

#Arithmatic and Maths
friends = 10
friends = friends + 1
friends += 1                                   #augmentated assignment operator for addition
friends = friends - 2
friends -= 2                                   #for substraction
friends = friends * 3
friends *= 3                                   #multiplication
friends = friends / 2
friends /= 2                                   #division
friends = friends ** 2
friends **= 2                                  #expontents
remainder = friends % 2                        #modulus
print(remainder)
print(friends)
print("")

#Built in math related functions:
x = 3.14
y = 4
z = 5
result = round(x)                             #round function
result = abs(y)                               #absolute value function
result = pow(4, 3)                            #power function, raise the base of the number to certain value
result = max(x, y, z)                         #maximum value function
result = min(x, y, z)                         #minimum value function
print(result)
import math
print(math.pi)
print(math.e)
x = 16
result = math.sqrt(x)                        #squareroot functions
result = math.ceil(x)                        #used for rounding up floats
result = math.floor(x)                       #rounding down
print(result)


# If-Else statements: Conditional statements
# if + Do some code only IF some condition is TRUE, else do something else
age = int(input("What is your age?"))
if age >= 100:
    print("Congratulations, you are a century old! But you can't sign in.")  
elif age >= 18:
    print("You are now signed up.")
elif age < 0:
    print("You haven't been born yet.")
else:
    print("You must be 18+ to sign up.")

response = input("Would you like food? (Y/N): ")
if response == "Y":         #to check two value are equals, you'll use ==
    print("Have some food!.")
else:
    print("No food for you.")

name = input("Enter your name: ")

if name == "":
    print("I SAID, ENTER YOUR NAME!")
else:
    print(f"Hello, {name}!")

for_sale = True
if for_sale:
    print("This is for sale!")
else:
    print("This is NOT for sale!")

online = False
if online:
    print("Yes, they are online.")
else:
    print("No, they are not online.")
    

#Logical Operators = evaluate multiple conditions (or, and, not)
#                    or = at least one condition must be true
#                    and = both conditions must be true
#                    not = inverts the condition (not False, not True)
temp = 30
# or operator
is_raining = False
if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is canceled.")
else:
    print("The outdoor event is still scheduled.")
# and operator   
is_sunny = True
if temp >= 28 and is_sunny:      #in order to operate this code, both conditions need to be true.
    print("It is hot and sunny outside.")
elif temp <= 0 and is_sunny:
    print("It is cold as well as sunny outside.")
elif 28> temp> 0 and is_sunny:
    print("It is warm outside.")
# not operator    
elif temp >= 28 and not is_sunny:     
    print("It is hot outside.")
    print("It is cloudy outside.")
elif temp <= 0 and not is_sunny:
    print("It is cold as well as cloudy outside.")
elif 28> temp> 0 and not is_sunny:
    print("It is warm and cloudy outside.")
