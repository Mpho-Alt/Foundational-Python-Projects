# This is a simple shopping cart program written in Python.
# The goal is to practice using lists, tuples, loops, and user input.
# A user can add items, remove items, view their cart, or checkout.

Food = []
# This list will store the items in the cart.
# Each item will be stored as a tuple: (item_name, quantity)
# Lists are useful because they can grow and shrink as the user adds or removes items.

price = []
# This list stores the price for each item.
# The price list matches the Food list by index.
# For example: Food[0] goes with price[0].
# This teaches how parallel lists work, which is an important beginner concept.

while True:
    # This creates an infinite loop.
    # The program keeps running until the user chooses to checkout and we break the loop.
    # Infinite loops are commonly used for menus in programs.

    action = input(
        "Would you like to add, remove, view items or checkout? (add/remove/view/checkout): "
    ).lower()
    # We ask the user what they want to do.
    # .lower() makes the input lowercase so the program accepts ADD, Add, or add.
    # This improves user experience and prevents errors.

    if action == "add":
        # This block runs if the user wants to add an item to the cart.

        item = input("Enter the item name: ")
        # The user enters the name of the item.
        # Strings are used here because item names are text.

        qty = int(input("Enter the quantity: "))
        # The user enters how many items they want.
        # int() converts the input from text to a number.
        # Numbers are needed for calculations later.

        cost = float(input("Enter the price per item: "))
        # The user enters the price for one item.
        # float() allows decimal values like 12.99.
        # This is commonly used for money in beginner projects.

        Food.append((item, qty))
        # We add a tuple to the Food list.
        # Tuples are used because the item name and quantity should stay together.
        # Tuples are good when values belong together and should not change separately.

        price.append(cost)
        # We store the price in the price list.
        # This keeps prices aligned with items using the same index position.

        print(f"Added {qty} of {item} at ${cost} each to the cart.")
        # This message confirms to the user that the item was added.
        # Feedback like this is important for user-friendly programs.

    elif action == "remove":
        # This block runs if the user wants to remove an item from the cart.

        item = input("Enter the item name to remove: ")
        # The user enters the name of the item they want removed.

        for i in range(len(Food)):
            # We loop through the Food list using index numbers.
            # range(len(Food)) lets us access both Food and price using the same index.

            if Food[i][0] == item:
                # Food[i][0] refers to the item name inside the tuple.
                # We check if the current item matches what the user typed.

                del Food[i]
                # We delete the item from the Food list.

                del price[i]
                # We also delete the matching price.
                # This keeps both lists in sync.

                print(f"Removed {item} from the cart.")
                # Let the user know the item was removed.

                break
                # Stop the loop once the item is found.
                # This improves efficiency and avoids unnecessary looping.

        else:
            # This else belongs to the for-loop.
            # It runs only if the loop finishes and no break was triggered.

            print(f"{item} not found in the cart.")
            # This tells the user the item does not exist in the cart.

    elif action == "view":
        # This block runs if the user wants to see what's in the cart.

        if not Food:
            # This checks if the Food list is empty.
            # Empty lists evaluate to False in Python.

            print("Your cart is empty.")
            # Inform the user there are no items.

        else:
            # This runs if the cart has items.

            print("Items in your cart:")
            # Header message for clarity.

            for i in range(len(Food)):
                # Loop through all items using their index.

                print(
                    f"{Food[i][0]} - Quantity: {Food[i][1]}, Price per item: ${price[i]}"
                )
                # Display item name, quantity, and price clearly.
                # f-strings make output easier to read and format.

    elif action == "checkout":
        # This block runs when the user is ready to pay and exit.

        total = 0
        # Initialize total cost to zero.
        # This variable will store the final bill.

        for i in range(len(Food)):
            # Loop through all items in the cart.

            total += Food[i][1] * price[i]
            # Multiply quantity by price and add to total.
            # This is basic arithmetic and shows how data is combined.

        print(f"Total amount due: ${total:.2f}")
        # Display the total amount.
        # :.2f formats the number to two decimal places (money format).

        print("Thank you for shopping with us!")
        # Friendly goodbye message.

        break
        # Exit the infinite loop and end the program.

    else:
        # This block runs if the user enters an invalid option.

        print("Invalid action. Please choose add, remove, view, or checkout.")
        # This helps guide the user back to valid choices.
