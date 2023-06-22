menu_and_prices = {
                    "1": {"item" :"Classic Milk Tea", "price": 5.50},
                    "2": {"item" :"Thai Milk Tea", "price": 5.50},
                    "3": {"item" :"Honey Milk Tea", "price": 5.7},
                    "4": {"item" :"Honeydew Milk Tea", "price": 6.00}, 
                    "5": {"item" :"Mango Milk Tea", "price": 6.00},
                    "6": {"item" :"Peach Milk Tea", "price": 6.00},
                    "7": {"item" :"Jasmine Milk Tea", "price": 6.25},
                    "8": {"item" :"Taro Milk Tea", "price": 6.50},
                    "9": {"item" :"Matcha Milk Tea", "price": 6.50},
                    "10": {"item" :"Ginger Milk Tea", "price": 6.50},
                    "11": {"item" :"Guava Milk Tea", "price": 6.75},
                    "12": {"item" :"Passion Fruit Milk Tea", "price": 6.75},
                    }

user_order = []

# display the menu
def display_menu():
    for key, value in menu_and_prices.items():
        print(f"{key}. {value['item']}: ${value['price']}")

# display the user selection
def add_order(item):
    if item in menu_and_prices:
        user_order.append(menu_and_prices[item])
        print(f"{menu_and_prices[item]['item']} added to order.")
    else:
        print("Invalid item.")

def view_order():
    if len(user_order) > 0:
        print("View order: ")
        for item in user_order:
            print(f"{item['item']}: ${item['price']}")
    else:
        print("Your order is empty.")
   
def calculate_total():
    total = sum(item["price"] for item in user_order)
    print(f"Total price: ${total}")

def welcome_message():
    print("=======================================")
    print("     WELCOME TO X MILK TEA")
    print("=======================================")

    while True:
        print("\n1. Display Menu")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Calculate Total")
        print("5. Exit\n")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            print("\nThis is the menu: ")
            display_menu()
        elif choice == '2':
            item = input("Enter the item number to add to cart: ")
            add_order(item)
        elif choice == '3':
            view_order()
        elif choice == '4':
            calculate_total()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    welcome_message()

