

#Excercise 1: Calculate the Area of a geometrical figure.
#Rectangle:
length = float(input("Enter the length: ")) #float * float = possible
width = int(input("Enter the width: ")) #integer * integer + possible
area = length * width #Can't multiply string. float * integer = possible
print(f"The area is: {area} cm².") #to add superscript: Num lock(on); hold Alt + (type)0178.
print("")
print("")
print("")

#Exercise 2: Shopping Cart Program
item = input("Enter the item: ")
price = float(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))
total_price = price * quantity
print(f"The total price is ${total_price}.")
print("")
print("")
print("")

#Excercise 3: circumference of a circle
import math
radius = float(input("Enter the radius: "))
circumference = 2* math.pi * radius
print(f"Circumference: {round(circumference, 2)}cm")
print("")
print("")
print("")

#Exercise 4: Area of a circle
import math
radius = float(input("Enter radius: "))
# area = math.pi * radius ** 2 ....OR:
area = math.pi * pow(radius, 2)
print(f"The area of the circle is: {round(area)}cm²")
print("")
print("")
print("")

#Exercise 5: Hypotenuse
import math
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b,2))
print(f" Side C = {c}")
