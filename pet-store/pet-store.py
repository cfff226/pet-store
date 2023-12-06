# A program which allows the user to add, remove and checkout with items that they purchase

# Dictionary of items

shopping_cart = []
price_total = []

# Display the menu and the cart until the user checks out

done = False
while not done:
    print("Welcome to Paws n Cart \n\nWhat would you like to do?\n")
    print("1. Add an item to your cart")
    print("2. Remove an item from your cart")
    print("3. View your cart")
    print("4. Checkout")
    choice = input(
        "\nPlease enter the number of the option that you would like to choose: "
    )

    if choice == "1":
        # Menu which shows the user the range of items
        print("\nPurina One Cat Salmon - Whole Grain 3KG - £7.99\n")
        print("Iams Senior 7+ Cat Food With Ocean Fish 2KG - £5.99\n")
        print("Iams Adult 1+ Cat Food With Fresh Chicken 800KG £3.99\n")
        print("Felix As Good As It Looks Cat Food Mixed Selection 40X100G £7.00\n")
        print("Felix Doubley Delicious Cat Food Meaty Selection 12x100G £4.00\n")
        print("Winalot Wet Dog Food Pouches Meaty Chunks In Jelly 12X100G £3.99\n")
        print("Bakers Whirlers Double Flavour Twisted Treats 130G £4.00\n")
        print("Chicken And Country Vegetable Dry Dog Food 800KG £6.99\n")
        add_item = input(
            "\nPlease input the item that you would like to add to your cart: "
        )
        price = float(
            input("Please input the price of the item you wish to purchase: ")
        )
        if add_item.lower() == "purina one cat salmon - whole grain 3kg":
            shopping_cart.append("Purina One Cat Salmon - Whole Grain 3KG")
            price_total.append(price)
            print(shopping_cart)
            print(price_total)
        elif add_item.lower() == "iams senior 7+ cat food with ocean fish 2kg":
            shopping_cart.append("Iams Senior 7+ Cat Food With Ocean Fish 2KG")
            price_total.append(price)
            print(shopping_cart)
            print(price_total)

    if choice == "2":
        print(shopping_cart)
        remove_item = input(
            "Please input item number that you would like to remove from your cart: "
        )
        if remove_item in shopping_cart: 
            index = shopping_cart.index(remove_item)
            shopping_cart.remove(remove_item)
            price_total.pop(index)

    elif choice == "3":  # This will include a function for the user to view their cart
        pass
    elif (
        choice == "4"
    ):  # This will exit the program and include a function for the user to checkout with items
        print("Thank you for shopping with Paws n Cart")
        done = True
    else:
        # Request input from user for their menu choice and the item that they would like to add to basket

        # Display output to the user to tell them the price of the item

        print(f"This item costs ....")

# Display output to the user to tell them that the item has been added to their basket

print("This item has been added to your cart successfully")
