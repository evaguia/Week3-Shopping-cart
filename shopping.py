# 

articles = ["🧸", "💿", "📷", "💽", "📃", "📓"]

def add_to_cart(to_add):
    cart.append(to_add)
    print (f"{to_add} added to cart.")

def remove(to_remove):
    try: 
        cart.remove(to_remove)
        print(f"{to_remove} removed from cart.")
    except ValueError:
        print(f"{to_remove} is not in your cart...")


cart = []

while True:

    print("============= WELCOME ===============")

    print("Enter 1) to add an element")
    print("Enter 2) to remove an element")
    print("Enter 3) to display cart")
    print("Enter 4) to quit")

    choice = input("Enter: ")

    if choice == "1":
        print(articles)
        to_add = input("Enter an article to add: ")
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
        print("Quitting")
        break

    else: 
        print("Invalid input. Try again.")

