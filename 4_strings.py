#Q1. Create 3 variables to store street, city and country, now create address variable to store entire address. Use two ways of creating this variable, one using + operator and the other using f-string. Now Print the address in such a way that the street, city and country prints in a separate line
street= input("enter the street name")
city= input("enter the city name")
country= input("enter the country name")
address="\n"+ street+ "\n " +city+ "\n "+country
print("Address is: ", address)
print(f"the street name is {street} \n city name is {city} \n the country name is {country} ")

#Q2. Create a variable to store the string "Earth revolves around the sun"
#Print "revolves" using slice operator
#Print "sun" using negative index
solar_system= "Earth revolves around the sun"
print("using slice:", solar_system[6:14])
print("using negative index: ", solar_system[-3:])

#Q3. Create two variables to store how many fruits and vegetables you eat in a day. Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.
vegetables= 4
fruits= 3
print(f"I eat {vegetables} veggies and {fruits} fruits daily")

#Q4. I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.
s='maine 200 banana khaye'
s = s.replace("200","10")
s= s.replace("banana", "samosa")
print("replace 200 by 10 and banana by samosa: \n",s)

#one line replace
s=s.replace("banana", "samosa").replace("200","10")
print(s)

