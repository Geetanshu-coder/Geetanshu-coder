#Q1. After flipping a coin 10 times you got this result,
#result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
#Using for loop figure out how many times you got heads

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
heads_count=0
for flip in result:
    if flip=="heads":
        heads_count+=1
print("number of heads is : ", heads_count)
        
#Q2. Print square of all numbers between 1 to 10 except even numbers
for i in range(1,11):
    print(i**2)

#Q3. Your monthly expense list (from Jan to May) looks like this,
#expense_list = [2340, 2500, 2100, 3100, 2980]
#Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. If expense is not found then it should print that as well.

expense_list = [2340, 2500, 2100, 3100, 2980]
months= ["Jan","Feb","Mar", "Apr", "May"]
expense = float(input("Enter an expense amount: "))
found= False
total=0
for i in range (len(expense_list)):
    if expense_list[i]==expense:
        print(f"The expense of {expense} occurred in {months[i]}.")
        found = True
        break

# If the expense was not found, inform the user
if not found:
    print(f"Expense of {expense} not found in any month.")

#Q4. Lets say you are running a 5 km race. Write a program that,

#Upon completing each 1 km asks you "are you tired?"
#If you reply "yes" then it should break and print "you didn't finish the race"
#If you reply "no" then it should continue and ask "are you tired" on every km
#If you finish all 5 km then it should print congratulations message

# Total distance of the race
total_km = 5

# Loop through each kilometer
for km in range(1, total_km + 1):
    # Ask if you're tired after each kilometer
    tired = input(f"After {km} km, are you tired? (yes/no): ").lower()

    # If the answer is 'yes', break the loop and print that you didn't finish
    if tired == "yes":
        print("You didn't finish the race.")
        break
# If the loop completes without breaking (meaning you didn't say "yes" for all 5 km)
else:
    print("Congratulations! You finished the race.")

#Q5. Write a program that prints following shape

#*
#**
#***
#****
#*****

for i in range(1, 6):
    print('*' * i)

    
