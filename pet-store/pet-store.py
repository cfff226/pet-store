# A program which allows the user to add, remove and checkout with items that they purchase

# Display the menu and the basket until the user checks out

#done = False
#while (not done):
print("Welcome to Paws n Cart \n\nWhat would you like to do?\n")
print("1. Add an item to your cart")
print("2. Remove an item from your cart")
print("3. View your cart")
print("4. Checkout")

# Request input from user for their menu choice and the item that they would like to add to basket

choice = input("\nPlease enter the number of the option that you would like to choose: ")

while True:
    if choice == "1":
        add_item = input("Please input the item that you would like to add to your basket: ")
    elif choice == "2":
        remove_item = input("Please input the item that you would like to remove from your basket: ")


# Display output to the user to tell them the price of the item

print(f"This item costs ....")

# Display output to the user to tell them that the item has been added to their basket

print("This item has been added to your basket successfully")

# Break out of the loop if the user selects choice 4 to checkout

if choice == "4":
    # Exit the program
    print("Thank you for shopping with Paws n Cart")
    done = True

# Menu which shows the user the range of items
