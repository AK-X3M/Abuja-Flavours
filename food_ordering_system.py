def breakfast_menu():
    return int(
        input(
            """Breakfast Menu:
                                1. Egg Roll  -  $1.50
                                2. Akara - $1
                                3. Noodles  =  $1
                                4. Gari and Peanut - $2
                                5. Back
                                6. Checkout
                                7. View Cart
                            """
        )
    )


def lunch_menu():
    return int(
        input(
            """Lunch Menu:
            1. Jollof Rice  -  $3
            2. Fried Rice - $3
            3. Draw Soup  -  $3
            4. Egusi Soup - $3
            5. Back
            6. Checkout
            7. View Cart
            """
        )
    )


def supper_menu():
    return int(
        input(
            """Supper Menu:
            1. Nsala Soup -  $3
            2. Bitterleaf Soup - $3
            3. Afro-Style Pizza  -  $3
            4. Pepper Soup - $3
            5. Back
            6. Checkout
            7. View Cart
            """
        )
    )


def beverage_menu():
    return int(
        input(
            """Beverages:
            1. Palm Wine  -  $2
            2. Coconut Milk - $1
            3. Cocoa Milk  -  $1
            4. Malt - $1
            5. Back
            6. Checkout
            7. View Cart
            """
        )
    )


def global_menu():
    return int(
        input(
            f"""Hello, {username}
                          We value your experience!
                          Here is the menu:
                          1. Breakfast Meals
                          2. Lunch Meals
                          3. Supper Meals
                          4. Beverages
                          5. Checkout
                          6. View Cart
                          """
        )
    )


def view_cart():
    print("Your cart:")
    for key in cart:
        print(
            f"""
              Meal Item: {key}
              Quantity: {int((cart[key]//meals[key]))}
              Price: ${float(cart[key])}0
              """
        )
        delete_choice = input("Do you want to delete item (y/n)")
        if delete_choice == "y":
            removing()
        else:
            pass
        global total
        total += cart[key]
    print(f"Total cost = {float(total)}0")


def checkout():
    print("Your cart:")
    for key in cart:
        print(
            f"""
              Meal Item: {key}
              Quantity: {int((cart[key]//meals[key]))}
              Price: ${float(cart[key])}0
              """
        )
        global total
        total += cart[key]
        tax = (15/100) * total
        delete_choice = input("Do you want to delete item (y/n)")
        if delete_choice == "y":
            removing()
        else:
            pass
    print(f"""Gross cost: {float(total)}0
Tax: {float(tax)}0
Net cost: {float(total + tax)}0""")
    confirmation = int(
        input(
            """How do you want to pay
                         1. EcoCash 
                         2. Credit Card
                         """
        )
    )
    while True:
        if confirmation == 1:
            phone_number = input("What is your EcoCash Number    ")
            pin = input("Enter your PIN   ")
            print(
                f"You have purchased goods worth ${float(total + tax)}0 from Abuja Flavours using EcoCash. Enjoy your day"
            )
            break
        if confirmation == 2:
            phone_number = input("What is your Credit Number Number")
            pin = input("Enter your PIN")
            print(
                f"You have purchased goods worth ${float(total + tax)}0 from Abuja Flavours using Credit Card. Enjoy your day"
            )
            break
        else:
            pass

def removing():
    del cart[input("Which item are you going to remove from your cart?")]
    
total = 0


def price_calculation(food):
    quantity = int(input("How many will you take     "))
    price = quantity * meals[food]
    cart[food] = price


accounts = {}
flag = False
meals = {
    "Egusi Soup": 3,
    "Egg Roll": 1.50,
    "Akara": 1,
    "Noodles": 1,
    "Gari and Peanuts": 2,
    "Jollof Rice": 3,
    "Fried Rice": 3,
    "Draw Soup": 3,
    "Nsala Soup": 3,
    "Bitterleaf Soup": 3,
    "Afro-Style Pizza": 3,
    "Pepper Soup": 3,
    "Palm Wine": 2,
    "Coconut Milk": 1,
    "Cocoa Milk": 1,
    "Malt": 1,
}
cart = {}


while flag == False:
    account_accessing = int(
        input(
            """Welcome to Abuja Flavours!
          How do you want to proceed:
          1. Sign Up
          2. Log In
          """
        )
    )
    if account_accessing == 1:
        username = input("Enter a Username:")
        password = input("Enter a Password:")
        accounts[username] = password

    elif account_accessing == 2:
        flag == True
        auth = False
        while auth == False:
            username = input("Enter your Username:")
            password = input("Enter your Password:")

            if username in accounts and password == accounts[username]:
                auth = True
                while True:
                    meal_type = global_menu()
                    if meal_type == 1:
                        while True:
                            breakfast_options = breakfast_menu()
                            if breakfast_options == 1:
                                price_calculation("Egg Roll")
                            elif breakfast_options == 2:
                                price_calculation("Akara")
                            elif breakfast_options == 3:
                                price_calculation("Noodles")
                            elif breakfast_options == 4:
                                price_calculation("Gari and Peanuts")
                            elif breakfast_options == 5:
                                break
                            elif breakfast_options == 6:
                                checkout()
                                break
                            elif breakfast_options == 7:
                                view_cart()
                            else:
                                print("Invalid Option")
                    elif meal_type == 2:
                        while True:
                            lunch_options = lunch_menu()
                            if lunch_options == 1:
                                price_calculation("Jollof Rice")
                            elif lunch_options == 2:
                                price_calculation("Fried Rice")
                            elif lunch_options == 3:
                                price_calculation("Draw Soup")
                            elif lunch_options == 4:
                                price_calculation("Egusi Soup")
                            elif lunch_options == 5:
                                break
                            elif lunch_options == 6:
                                checkout()
                                break
                            elif lunch_options == 7:
                                view_cart()
                            else:
                                print("Invalid Option")
                    elif meal_type == 3:
                        while True:
                            supper_options = supper_menu()
                            if supper_options == 1:
                                price_calculation("Nsala Soup")
                            elif supper_options == 2:
                                price_calculation("Bitterleaf Soup")
                            elif supper_options == 3:
                                price_calculation("Afro-Style Pizza")
                            elif supper_options == 4:
                                price_calculation("Pepper Soup")
                            elif supper_options == 5:
                                break
                            elif supper_options == 6:
                                checkout()
                                break
                            elif supper_options == 7:
                                view_cart()
                            else:
                                print("Invalid Option")
                    elif meal_type == 4:
                        while True:
                            beverage_options = beverage_menu()
                            if beverage_options == 1:
                                price_calculation("Palm Wine")
                            elif beverage_options == 2:
                                price_calculation("Coconut Milk")
                            elif beverage_options == 3:
                                price_calculation("Cocoa Milk")
                            elif beverage_options == 4:
                                price_calculation("Malt")
                            elif beverage_options == 5:
                                break
                            elif beverage_options == 6:
                                checkout()
                                break
                            elif beverage_options == 7:
                                view_cart()
                            else:
                                print("Invalid Option")
                    elif meal_type == 5:
                        checkout()
                    elif meal_type == 6:
                        view_cart()

            else:
                print("Account not found")

    else:
        print("Enter valid option")
