tea_menu = ["1. Classic Milk Tea", "2. Thai Milk Tea", "3. Honey Milk Tea", "4. Honeydew Milk Tea", 
            "5. Mango Milk Tea", "6. Peach Milk Tea", "7. Jasmine Milk Tea", "8. Taro Milk Tea",
            "9. Matcha Milk Tea", "10. Ginger Milk Tea", "11. Guava Milk Tea", "12. Passion Fruit Milk Tea"]

tea_prices = [5.50, 5.50, 5.75, 6.00, 6.00, 6.00, 6.25, 6.50, 6.50, 6.50, 6.50, 6.75, 6.75]

user_order = []

 # display welcome message
def welcome_messages():
    print("=======================================")
    print("     WELCOME TO X MILK TEA")
    print("=======================================")

    # print("Pick your favourite milk tea from our menu ^^: ")
    print()

# display the menu
def menu():
    user_choice = input("Would you like to look at the menu? [y/n] ")
    if user_choice == "y": 
        selection()
    if user_choice == "n":
         print("Thank you! See you again! ")


# display the user selection
def selection():
    print()

    for i in range(0, len(tea_menu)):
            print(tea_menu[i])

    # extract the number of out the list 
    tea_list_numbers = [int(item.split(".")[0]) for item in tea_menu]

    print()

    # user choose the tea by the number
    user_choice = int(input("Your tea choice: "))

    if user_choice in tea_list_numbers:
        idx = tea_list_numbers.index(user_choice)
        price = tea_prices[idx]
        print("Your milk tea costs ${}".format(price))
    else:
        print("Tea not in the menu")

if __name__ == "__main__":
    welcome_messages()
    menu()
