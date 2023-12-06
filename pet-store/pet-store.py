# A program which allows the user to add, remove and checkout with items that they purchase

# Dictionary of items

Prices = {
    "1. Purina One Cat Salmon - Whole Grain 3KG": 7.99,
    "2. Iams Senior 7+ Cat Food With Ocean Fish 2KG": 5.99,
    "3. Iams Adult 1+ Cat Food With Fresh Chicken 800KG": 3.99,
    "4. Felix As Good As It Looks Cat Food Mixed Selection 40X100G": 7.00,
    "5. Felix Doubley Delicious Cat Food Meaty Selection 12x100G": 4.00,
    "6. Winalot Wet Dog Food Pouches Meaches Chunks In Jelly 12x100G": 3.99,
    "7. Bakers Whirlers Double Flavour Twisted Treats 130G": 4,
    "8. Chicken And Country Vegetable Dry Dog Food 800KG": 6.99,
}


# Display the menu and the basket until the user checks out

done = False
while (not done):
    print("Welcome to Paws n Cart \n\nWhat would you like to do?\n")
    print("1. Add an item to your cart")
    print("2. Remove an item from your cart")
    print("3. View your cart")
    print("4. Checkout")
    choice = input("\nPlease enter the number of the option that you would like to choose: ")
    break

shopping_cart = []

# Request input from user for their menu choice and the item that they would like to add to basket


while True:
    if choice == "1":
        # Menu which shows the user the range of items
        print("\n1. Purina One Cat Salmon - Whole Grain 3KG\n")
        print("2. Iams Senior 7+ Cat Food With Ocean Fish 2KG\n")
        print("3. Iams Adult 1+ Cat Food With Fresh Chicken 800KG\n")
        print("4. Felix As Good As It Looks Cat Food Mixed Selection 40X100G\n")
        print("5. Felix Doubley Delicious Cat Food Meaty Selection 12x100G\n")
        print("6. Winalot Wet Dog Food Pouches Meaty Chunks In Jelly 12X100G\n")
        print("7. Bakers Whirlers Double Flavour Twisted Treats 130G\n")
        print("8. Chicken And Country Vegetable Dry Dog Food 800KG\n")
        add_item = input(
            "\nPlease input the number of the item that you would like to add to your basket: "
        )
        if add_item.lower() == "1":
                    shopping_cart.append("1. Purina One Cat Salmon - Whole Grain 3KG")
                    print(shopping_cart)
                    break
        elif add_item.lower() == "2":
                    shopping_cart.append("2. Iams Senior 7+ Cat Food With Ocean Fish 2KG")
                    print(shopping_cart)
                    break

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





