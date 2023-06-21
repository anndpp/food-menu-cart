def welcome_messages():
    print("=======================================")
    print("     WELCOME TO X BUBBLE MILK TEA")
    print("=======================================")

    print("Pick your favourite milk tea from our menu ^^")

def menu():
    print("1. Classic Milk Tea")
    print("2. Thai Milk Tea")
    print("3. Honey Milk Tea")
    print("4. Honeydew Milk Tea")
    print("5. Mango Milk Tea")
    print("6. Peach Milk Tea")
    print("7. Jasmine Milk Tea")
    print("9. Taro Milk Tea")
    print("10. Matcha Milk Tea")
    print("11. Ginger Milk Tea")
    print("12. Guava Milk Tea")
    print("13. Passion Fruit Milk Tea")

def selection():
    menu()
    print()
    choice = int(input("Your drink choice: "))
    if choice > 0 and choice <= 13:
        quantity()

def quantity():
    print("How many drink would you like?")

if __name__ == "__main__":
    welcome_messages()
    selection()
