#basic code on functions
def calculate(a,b):
    return a+b
print(calculate(5,6))
#calcualte area of circle
def calculate_area_circle(radius):
    import math
    return math.pi*radius**2
print(calculate_area_circle(4))
##print a normal statment
def greet(name="Geetanshu"):
    return f"Hello {name}"
print(greet())

#Exercise: Functions in python
'''Q1.Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
area = (1/2)*base*height'''
def calculate_area(base,height):
    return 0.5*base*height
area= calculate_area(5,7)
print("area of triangle is: ", area)

'''Q2.Modify above function to take third parameter shape type. 
It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
rectangle area=length*width
If no shape is supplied then it should take
 triangle as a default shape'''
def calculate_area_rectangle(length,width, shape= "rectangle"):
    return length*width
rectangle_area= calculate_area_rectangle(5,7)

shape= input("enter shape")
if shape=="rectangle":
    print("rectangle area is: ",rectangle_area)
else:
    print("area of triangle is: ", area)

'''Q3. Write a function called print_pattern that takes integer number as an argument 
and prints following pattern if input number is 3,
*
**
***
if input is 4 then it should print

*
**
***
****
Basically number of lines it prints is equal to that number.
(Hint: you need to use two for loops)'''

def print_pattern(integer):
    for i in range(1, integer):
        print('*'*i)#print("\t"+'*'+"\t"*i) another type of patter will occur
star_count= int(input("enter the star number for pattern"))
print(print_pattern(star_count))

    