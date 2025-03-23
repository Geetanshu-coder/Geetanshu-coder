#Q1.You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
field_lenght= 92
field_width= 48.8
area_of_football_field= field_lenght*field_width
print("area of football field is: ", area_of_football_field)

#Q2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?
quantity_of_chips_packets= 9
cost_of_one_packet= 1.49
total_amount= 20
total_price= quantity_of_chips_packets*cost_of_one_packet
total_balanced_left= total_amount-total_price
print("cost of 9 chips packets is: ", total_price)
print("amount shopkeeper going to give you back: ", total_balanced_left)

#Q3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
area_of_bathroom= 5.5**2
total_cost_of_bathroom_tiles= area_of_bathroom*500
print("area of bathroom is: ", area_of_bathroom)
print("total cost to buy tiles for the bathroom is: ", total_cost_of_bathroom_tiles)

#Q4. Print binary representation of number 17
number= 17
binary_representation= bin(number)
print(f"The binary representation of {number} is: {binary_representation[2:]}")
#The first two characters (0b) are a prefix indicating that the string represents a binary number.
#By using [2:], we slice the string starting from the 3rd character (index 2) to remove the 0b prefix.
#The result is just the binary digits ('10001').