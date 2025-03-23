#basic
dic={
    "usain bolt": "athlete",
    "virat": "cricketer",
    "michael philips":"swimmer",
    "michael jordan": " basketball player"
}
print(dic["usain bolt"])
print(dic.get("usain bolt"))
print(dic.keys())

for key in dic.keys():
    print(dic[key])
#using user input
dic1= {
    1: "aadi",
    2: "deepti",
    3: "geetanshu",
    4: "gaurav",
    5: "vivek"
}
user_input= int(input("enter the number"))
print(dic1[user_input])

dic2= {
    6:"dada ji",
    7:"dadi ji",
    8:"papa ji",
    9:"mummy ji",
    10:"chachu ji",
    11:"chachi ji"
}

#dic1.update(dic2)
#dic1.clear()
#dic2.pop(6)

print(dic2)

'''Exercise: Python Dict and Tuples
We have following information on countries and their population (population is in crores),

Country	Population
China	143
India	136
USA	32
Pakistan	21
Using above create a dictionary of countries and its population
Write a program that asks user for three type of inputs,
print: if user enter print then it should print all countries with their population in this format,
china==>143
india==>136
usa==>32
pakistan==>21
add: if user input add then it should further ask for a country name to add. If country already exist
in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population 
and add that new country/population in our dictionary and print it
remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary 
then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
query: on this again ask user for which country he or she wants to query. When user inputs that country it will 
print population of that country.'''

countries= {
    "China": 143,
    "India": 136,
    "USA" : 32,
    "Pakistan" : 21
}
print(countries.keys())
for key,value in countries.items():
    print(f"{key}==>{value}")






