tea_menu = ["Classic Milk Tea", "Thai Milk Tea", "Honey Milk Tea", "Honeydew Milk Tea", 
            "Mango Milk Tea", "Peach Milk Tea", "Jasmine Milk Tea", "Taro Milk Tea",
            "Matcha Milk Tea", "Ginger Milk Tea", "Guava Milk Tea", "Passion Fruit Milk Tea"]

tea_prices = [5.50, 5.50, 5.75, 6.00, 6.00, 6.00, 6.25, 6.50, 6.50, 6.50, 6.50, 6.75, 6.75]
 
def welcome_messages():
    print("=======================================")
    print("     WELCOME TO X BUBBLE MILK TEA")
    print("=======================================")

    print("Pick your favourite milk tea from our menu ^^: ")
    print()

def menu():
  for i in range(0, len(tea_menu)):
      print(tea_menu[i])
      
def selection():
    menu()
    print()
    choice = int(input("Your tea choice: "))
    if choice > 0 and choice <= 13:
        quantity()

def quantity():
    drink_quantity = int(input("How many would you like? "))

if __name__ == "__main__":
    welcome_messages()
    selection()
