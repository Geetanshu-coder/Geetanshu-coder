'''Q1. Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,
1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this ''' 
expenses = [2200, 2350, 2600, 2130, 2190]

# Print the list of expenses
print("Monthly expenses:", expenses)

extra_feb = expenses[1] - expenses[0]
print("1. In Feb, how many dollars you spent extra compare to January? ", extra_feb )

total_expense_in_first_quarter= expenses[0]+expenses[1]+expenses[2]
print("Find out your total expense in first quarter (first three months) of the year. ", total_expense_in_first_quarter)

print("Is '2000' in the list?", 2000 in expenses)

expenses.append(1980)
print("new list of exp with '1980' : ", expenses)

expenses[3]=1930
print("new list of expenses is :", expenses)

'''Q2. You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
  so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
 So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
  Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)'''

heros=['spider man','thor','hulk','iron man','captain america']
print("list of heros is: ", heros)

lenght= len(heros)
print("lenght of heros is: ", lenght)

heros.append('black panther')
print("new heros list: ", heros)

heros.remove('black panther')
heros.insert(3,'black panther')
print("after hulk: ", heros)

heros[1:3] = ['doctor strange']  # Replace the sublist from index 1 to 3 (excluding 3)
print(f"After replacing 'thor' and 'hulk' with 'doctor strange': {heros}")

heros.sort()
print("sorted list: ", heros)
