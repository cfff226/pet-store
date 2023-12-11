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
        price = float(
            input("Please input the price of the item you wish to purchase: ")
        )

        if add_item == 1:
            print("\nYou selected: ", menu[add_item-1])
            quant = int(
                input("\nPlease input the quantity of the item you wish to purchase: ")
            )
            
            if menu[add_item-1] in shopping_cart:
                print("repeated order")
            else:
                print("new selection")
                shopping_cart.append(menu[add_item-1])




            print("\nThis item has been added to your cart successfully\n")


        elif add_item.lower() == "iams senior 7+ cat food with ocean fish":
            shopping_cart.append("Iams Senior 7+ Cat Food With Ocean Fish")
            price_total.append(price)
            print("\nThis item has been added to your cart successfully\n")

        elif add_item.lower() == "iams adult 1+ cat food with fresh chicken":
            shopping_cart.append("Iams Adult 1+ Cat Food With Fresh Chicken")
            price_total.append(price)
            print("\nThis item has been added to your cart successfully\n")

        elif add_item.lower() == "felix as good as it looks cat food mixed selection":
            shopping_cart.append("Felix As Good As It Looks Cat Food Mixed Selection")
            price_total.append(price)
            print("\nThis item has been added to your cart successfully\n")

        elif add_item.lower() == "felix doubley delicious cat food meaty selection":
            shopping_cart.append("Felix Doubley Delicious Cat Food Meaty Selection")
            price_total.append(price)
            print("\nThis item has been added to your cart successfully\n")

        elif add_item.lower() == "winalot wet dog food pouches meaty chunks in jelly":
            shopping_cart.append("Winalot Wet Dog Food Pouches Meaty Chunks In Jelly")
            price_total.append(price)
            print("\nThis item has been added to your cart successfully\n")

        elif add_item.lower() == "bakers whirlers double flavour twisted treats":
            shopping_cart.append("Bakers Whirlers Double Flavour Twisted Treats")
            price_total.append(price)
            print("\nThis item has been added to your cart successfully\n")

        elif add_item.lower() == "chicken and country vegetable dry dog food":
            shopping_cart.append("Chicken And Country Vegetable Dry Dog Food")
            price_total.append(price)
            print("\nThis item has been added to your cart successfully\n")

    if choice == "2":
        print(shopping_cart)
        remove_item = input(
            "Please input item that you would like to remove from your cart: "
        )
        if remove_item in shopping_cart:
            index = shopping_cart.index(remove_item)
            shopping_cart.remove(remove_item)
            price_total.pop(index)
        else:
            print(
                "\n\n---------------- That item is not in your shopping cart ---------------- \n\n"
            )

    elif choice == "3":  # This will include a function for the user to view their cart
        print(
            "\n----------------------------------------------\n\nThis is your shopping cart:\
                   \n\n\n\n\n----------------------------------------------\n"
        )
        cart_quantity = dict(
            (add_item, shopping_cart.count(add_item)) for add_item in shopping_cart
        )

        for item in cart_quantity:
            print(item, ":", cart_quantity)

        total_cost = 0
        for x in price_total:
            total_cost = total_cost + x
        print(f"\n\nThe shopping cart total is £{total_cost}\n")
    elif (
        choice == "4"
    ):  # This will exit the program and include a function for the user to checkout with items
        print("Thank you for shopping with Paws n Cart")
        done = True
    else:
        pass
