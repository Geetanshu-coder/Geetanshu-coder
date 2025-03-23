#Q1. Using following list of cities per country,
#india = ["mumbai", "banglore", "chennai", "delhi"]
#pakistan = ["lahore","karachi","islamabad"]
#bangladesh = ["dhaka", "khulna", "rangpur"]
#i.Write a program that asks user to enter a city name and it should tell which country the city belongs to
#ii. Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

#i.
city= input("enter the city name")

if city in india:
    print(f"{city} in India")
elif city in pakistan:
    print(f"{city} in Pakistan")
elif city in bangladesh:
    print(f"{city} in Bangladesh")
else:
    print(f"{city} in other country")

#ii
city1= input("enter the city1 name")
city2= input("enter the city2 name")

if city1 in india:
    country1 = "India"
elif city1 in pakistan:
    country1 = "Pakistan"
elif city1 in bangladesh:
    country1 = "Bangladesh"
else:
    country1 = "Other"

# Determine the country for city2
if city2 in india:
    country2 = "India"
elif city2 in pakistan:
    country2 = "Pakistan"
elif city2 in bangladesh:
    country2 = "Bangladesh"
else:
    country2 = "Other"

# Compare the countries of both cities
if country1 == country2:
    if country1 != "Other":
        print(f"Both cities are in {country1}")
    else:
        print("One or both cities are not found in the listed countries")
else:
    print("They don't belong to the same country")


#Q2. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
#Ask user to enter his fasting sugar level
#If it is below 80 to 100 range then print that sugar is low
#If it is above 100 then print that it is high otherwise print that it is normal

#Ask user to enter his fasting sugar level
sugar_level= int(input("enter the sugar level"))
if sugar_level <80:
    print("sugar level is normal")
elif sugar_level >100:
    print("sugar level is high")
else:
    print("sugar level is normal")
    
