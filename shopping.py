# Shopping cart

articles = {
    "🧸": 3,
    "💿": 3,
    "📷": 3,
    "💽": 3,
    "📃": 3,
    "📓": 3
}

def add_to_cart(to_add):
    if articles[to_add] != 0:
      cart.append(to_add)
      print (f"{to_add} added to cart.")
      articles[to_add] -= 1
    else:
        print(f"{to_add} is sold out !")


def remove(to_remove):
    try:  
        cart.remove(to_remove)
        articles[to_remove] += 1
        print(f"{to_remove} removed from cart.")
    except ValueError:
        print(f"{to_remove} is not in your cart...")

def check_stock():
    for article, stock in articles.items():
        print(f"{article} - {stock}")


cart = []

while True:

    print("============= WELCOME ===============")

    print("Enter 1) to add an element")
    print("Enter 2) to remove an element")
    print("Enter 3) to display cart")
    print("Enter 4) to check stock")
    print("Enter 5) to quit")

    choice = input("Enter: ")

    if choice == "1":
        print(list(articles))
        to_add = input("Enter an article to add: ")
        if to_add not in articles:
            print(f"{to_add} is not available.")
        else:
            add_to_cart(to_add)
    
    elif choice == "2":
        if not cart:
            print("Your cart is empty.")
        else:
            print(cart)
            to_remove = input("Enter an article to remove: ")
            remove(to_remove)

    elif choice == "3":
        if not cart:
            print("You cart is empty.")
        else:
            print(f"Your cart is composed of {cart}")
    
    elif choice == "4":
        check_stock()

    elif choice == "5":
        print("Quitting")
        break

    else: 
        print("Invalid input. Try again.")

