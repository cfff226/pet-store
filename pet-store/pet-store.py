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

        while True:
            try:
                add_item = int(
                    input(
                        "\nPlease input the number of the item that you would like to add to your cart: "
                    )
                )
                break
            except ValueError:
                continue

        while True:
            try:
                quant = int(
                    input(
                        "\nPlease input the quantity of the item you wish to purchase: "
                    )
                )
                break
            except ValueError:
                print("\n\nYou've entered an incorrect value")
                continue

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
            "\n-----------------------------------------------------------------------------------------------------\n\n                                    This is your shopping cart:\
                        \n\n-----------------------------------------------------------------------------------------------------\n"
        )

        for i in range(len(shopping_cart)):
            idx = menu.index(shopping_cart[i])
            unit_price = prices[idx]
            print(
                f"Item {i + 1}: {shopping_cart[i]} Quantity: {shopping_quant[i]}         Price: £{unit_price}\n"
            )

        while True:
            try:
                remove_item = int(
                    input(
                        "\nPlease input the number of the item that you would like to remove from your cart: "
                    )
                )
                print("\nYou selected: ", shopping_cart[remove_item - 1])
                break
            except ValueError:
                print("You have entered an incorrect value")
                continue
            except IndexError:
                print("This item does not exist in your cart")
                continue

        while True:
            try:
                quant = int(
                    input(
                        "\nPlease input the quantity of the item you wish to remove: "
                    )
                )
                break
            except ValueError:
                print("You have entered an incorrect value")
                continue

        if shopping_cart[remove_item - 1] in shopping_cart:
            idx = shopping_cart.index(shopping_cart[remove_item - 1])
            shopping_quant[idx] = shopping_quant[idx] - quant

            print(f"Your shopping quantity of this item is: {shopping_quant[idx]}")
            if shopping_quant == 0:
                print(shopping_quant)
                shopping_cart.remove(shopping_cart[remove_item - 1])
                print(shopping_cart)

        else:
            print("\n\n\n\nthis item is not your cart")

    # At the moment there is an error where instead of deleting the entire item, the program reduces
    # the quantity to 0. This is something I am working on fixing

    elif choice == "3":  # This will include a function for the user to view their cart
        print(
            "\n-----------------------------------------------------------------------------------------------------\n\n                                      This is your shopping cart:\
                \n\n-----------------------------------------------------------------------------------------------------\n"
        )

        for i in range(len(shopping_cart)):
            idx = menu.index(shopping_cart[i])
            unit_price = prices[idx]
            print(
                f"Item: {shopping_cart[i]} Quantity: {shopping_quant[i]}        \
                      Price: £{unit_price}\n\n-----------------------------------------------------------------------------------------------------\n"
            )

    elif (
        choice == "4"
    ):  # This will exit the program and include a function for the user to checkout with items
        print("Thank you for shopping with Paws n Cart")
        done = True
    else:
        pass
