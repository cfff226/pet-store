# A program which allows the user to add, remove and checkout with items that they purchase

# Display the menu and the basket until the user checks out

# done = False
# while (not done):
print("Welcome to Paws n Cart \n\nWhat would you like to do?\n")
print("1. Add an item to your cart")
print("2. Remove an item from your cart")
print("3. View your cart")
print("4. Checkout")

# Request input from user for their menu choice and the item that they would like to add to basket

choice = input(
    "\nPlease enter the number of the option that you would like to choose: "
)

while True:
    if choice == "1":
        add_item = input(
            "Please input the item that you would like to add to your basket: "
        )
    elif choice == "2":
        remove_item = input(
            "Please input the item that you would like to remove from your basket: "
        )
    elif choice == "3":  # This will include a function for the user to view their cart
        pass
    elif (
        choice == "4"
    ):  # This will exit the program and include a function for the user to checkout with items
        print("Thank you for shopping with Paws n Cart")
        done = True
        break
    else:
        break


# Display output to the user to tell them the price of the item

print(f"This item costs ....")

# Display output to the user to tell them that the item has been added to their basket

print("This item has been added to your basket successfully")

# Menu which shows the user the range of items

print("Purina One Cat Salmon - Whole Grain 3KG")
print("Iams Senior 7+ Cat Food With Ocean Fish 2KG")
print("Iams Adult 1+ Cat Food With Fresh Chicken 800KG")
print("Felix As Good As It Looks Cat Food Mixed Selection 40X100G")
print("Felix Doubley Delicious Cat Food Meaty Selection 12x100G")
print("Winalot Wet Dog Food Pouches Meaty Chunks In Jelly 12X100G")
print("Bakers Whirlers Double Flavour Twisted Treats 130G")
print("Chicken And Country Vegetable Dry Dog Food 800KG")
