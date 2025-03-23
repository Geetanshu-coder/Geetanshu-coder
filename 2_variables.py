#Q1.Create a variable called break and assign it a value 5. 
a=int(input("enter the number"))
print("break=", a)

#Q2.Create two variables. One to store your birth year and another one to store current year. Now calculate your age using these two variables
birth_year=int(input("enter the birth year"))
current_year=int(input("enter the current year"))
age=current_year-birth_year
print("current age is:", age)

#Q3.  Create two variables. One to store your birth year and another one to store current year. Now calculate your age using these two variables
first_name= input("enter the first name")
middle_name= input("enter the middle name")
last_name= input("enter the last name")
full_name= first_name+" "+middle_name+" "+last_name
print("full name is: ", full_name)

#Q4. Answer which of these are invalid variable names: "_nation, 1record, record1, record_one, record-one, record^one, continue"
import keyword

# List of variable names to check
variable_names = ["_nation", "1record", "record1", "record_one", "record-one", "record^one", "continue"]

# Function to check if a variable name is valid
def is_valid_variable(name):
    if name.isidentifier() and not keyword.iskeyword(name):
        return True
    return False

# Check each variable name
for name in variable_names:
    if is_valid_variable(name):
        print(f"'{name}' is a valid variable name.")
    else:
        print(f"'{name}' is an invalid variable name.")