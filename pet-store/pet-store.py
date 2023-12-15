import math

# A program which allows the user to add, remove and checkout with items that they purchase

# Dictionary of items

shopping_cart = []
shopping_quant = []
price_total = []

menu = [
    "Purina One Cat Salmon - Whole Grain               ",
    "Iams Senior 7+ Cat Food With Ocean Fish           ",
    "Iams Adult 1+ Cat Food With Fresh Chicken         ",
    "Felix As Good As It Looks Cat Food Mixed Selection",
    "Felix Doubley Delicious Cat Food Meaty Selection  ",
    "Winalot Wet Dog Food Pouches Meaty Chunks In Jelly",
    "Bakers Whirlers Double Flavour Twisted Treats     ",
    "Chicken And Country Vegetable Dry Dog Food        ",
]

prices = [7.99, 5.99, 3.99, 7.00, 4.00, 3.99, 4.00, 6.99]

# Display the menu and the cart until the user checks out

print("Welcome to Paws n Cart \n\nWhat would you like to do?\n")

done = False
while not done:
    print("1. Add an item to your cart")
    print("2. Remove an item from your cart")
    print("3. View your cart")
    print("4. Checkout")
    choice = input(
        "\nPlease enter the number of the option that you would like to choose: "
    )

    if choice == "1":
        # Menu which shows the user the range of items

        for i in range(len(menu)):
            print(str(i + 1) + ". " + menu[i], prices[i])

        add_item = int(
            input(
                "\nPlease input the number of the item that you would like to add to your cart: "
            )
        )

        if add_item < 5:
            print("\nYou selected: ", menu[add_item - 1])
            quant = int(
                input("\nPlease input the quantity of the item you wish to purchase: ")
            )

            if menu[add_item - 1] in shopping_cart:
                print("repeated order")
                idx = shopping_cart.index(menu[add_item - 1])
                print(idx)
                shopping_quant[idx] += quant
            else:
                print("new selection")
                shopping_cart.append(menu[add_item - 1])
                shopping_quant.append(quant)

            print("\nThis item has been added to your cart successfully\n")

    if choice == "2":
        # This will include a function for the user to remove items from their cart

        print(
            "\n----------------------------------------------\n\nThis is your shopping cart:\
                        \n\n\n\n\n----------------------------------------------\n"
        )

        for i in range(len(shopping_cart)):
            idx = menu.index(shopping_cart[i])
            unit_price = prices[idx]
            print(
                f"Item: {shopping_cart[i]} Quantity: {shopping_quant[i]}         Price: £{unit_price}\n"
            )

        remove_item = int(
                input(
                    "\nPlease input the number of the item that you would like to remove from your cart: "
                )
            )
        if remove_item < 5:
            print("\nYou selected: ", menu[remove_item - 1])
            quant = int(
                input(
                    "\nPlease input the quantity of the item you wish to remove: "
                )
            )

            print("\nThis item has been removed from your cart successfully\n")

       

    elif choice == "3":  # This will include a function for the user to view their cart
        print(
            "\n----------------------------------------------\n\nThis is your shopping cart:\
                \n\n\n\n\n----------------------------------------------\n"
        )

        for i in range(len(shopping_cart)):
            idx = menu.index(shopping_cart[i])
            unit_price = prices[idx]
            print(
                f"Item: {shopping_cart[i]} Quantity: {shopping_quant[i]}         Price: £{unit_price}\n"
            )

    elif (
        choice == "4"
    ):  # This will exit the program and include a function for the user to checkout with items
        print("Thank you for shopping with Paws n Cart")
        done = True
    else:
        pass
