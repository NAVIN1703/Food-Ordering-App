#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class FoodItem:
    def __init__(self, food_id, name, quantity, price, discount, stock):
        self.food_id = food_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock


class Admin:
    def __init__(self):
        self.food_items = []

    def add_food_item(self, name, quantity, price, discount, stock):
        food_id = len(self.food_items) + 1
        food_item = FoodItem(food_id, name, quantity, price, discount, stock)
        self.food_items.append(food_item)
        print("Food item added successfully!")

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                print("Food item updated successfully!")
                break
        else:
            print("Food item not found!")

    def remove_food_item(self, food_id):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                self.food_items.remove(food_item)
                print("Food item removed successfully!")
                break
        else:
            print("Food item not found!")

    def view_food_items(self):
        if not self.food_items:
            print("No food items available!")
        else:
            for food_item in self.food_items:
                print(f"FoodID: {food_item.food_id}")
                print(f"Name: {food_item.name}")
                print(f"Quantity: {food_item.quantity}")
                print(f"Price: {food_item.price}")
                print(f"Discount: {food_item.discount}")
                print(f"Stock: {food_item.stock}")
                print("--------------------------")


class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.order_history = []

    def place_new_order(self, food_items):
        if not food_items:
            print("No food items selected!")
        else:
            order_total = sum(food_item.price for food_item in food_items)
            order_details = [food_item.name for food_item in food_items]
            order_history_entry = {
                "Order Details": order_details,
                "Order Total": order_total
            }
            self.order_history.append(order_history_entry)
            print("Order placed successfully!")

    def view_order_history(self):
        if not self.order_history:
            print("No order history available!")
        else:
            for index, order_entry in enumerate(self.order_history):
                print(f"Order {index+1}:")
                print("Order Details:", order_entry["Order Details"])
                print("Order Total:", order_entry["Order Total"])
                print("--------------------------")

    def update_profile(self, full_name=None, phone_number=None, email=None, address=None, password=None):
        if full_name:
            self.full_name = full_name
        if phone_number:
            self.phone_number = phone_number
        if email:
            self.email = email
        if address:
            self.address = address
        if password:
            self.password = password
        print("Profile updated successfully!")


admin = Admin()
users = {}

while True:
    print("Welcome to the Food Delivery App!")
    print("1. Admin Login")
    print("2. User Register")
    print("3. User Login")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Admin Login
        admin_username = input("Enter admin username: ")
        admin_password = input("Enter admin password: ")

        # Perform admin login validation here
        # ...

        print("Admin logged in successfully!")
        while True:
            print("-------------------------------- Admin ----------------------------------")
            print("1. Add new food items")
            print("2. Edit food items")
            print("3. View list of all food items")
            print("4. Remove a food item")
            print("5. Log out as admin")

            admin_choice = input("Enter your choice: ")

            if admin_choice == "1":
                # Add new food item
                name = input("Enter food item name: ")
                quantity = input("Enter food item quantity: ")
                price = float(input("Enter food item price: "))
                discount = float(input("Enter food item discount: "))
                stock = int(input("Enter food item stock: "))
                admin.add_food_item(name, quantity, price, discount, stock)

            elif admin_choice == "2":
                # Edit food item
                food_id = int(input("Enter the FoodID of the food item: "))
                name = input("Enter food item name: ")
                quantity = input("Enter food item quantity: ")
                price = float(input("Enter food item price: "))
                discount = float(input("Enter food item discount: "))
                stock = int(input("Enter food item stock: "))
                admin.edit_food_item(food_id, name, quantity, price, discount, stock)

            elif admin_choice == "3":
                # View list of all food items
                admin.view_food_items()

            elif admin_choice == "4":
                # Remove a food item
                food_id = int(input("Enter the FoodID of the food item: "))
                admin.remove_food_item(food_id)

            elif admin_choice == "5":
                # Log out as admin
                print("Logging out as admin...")
                break

            else:
                print("Invalid choice. Please try again.")

    elif choice == "2":
        # User Register
        full_name = input("Enter your full name: ")
        phone_number = input("Enter your phone number: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")
        password = input("Enter your password: ")

        user = User(full_name, phone_number, email, address, password)
        users[email] = user
        print("User registered successfully!")

    elif choice == "3":
        # User Login
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        user = users.get(email)

        if user and user.password == password:
            print("User logged in successfully!")

            while True:
                print("-------------------------------- User ----------------------------------")
                print("1. Place New Order")
                print("2. Order History")
                print("3. Update Profile")
                print("4. Log out as user")

                user_choice = input("Enter your choice: ")

                if user_choice == "1":
                    # Place New Order
                    print("Food Menu:")
                    print("1. Tandoori Chicken (4 pieces) [INR 240]")
                    print("2. Vegan Burger (1 Piece) [INR 320]")
                    print("3. Truffle Cake (500gm) [INR 900]")

                    food_item_numbers = input("Enter the numbers of the food items you want to order (separated by commas): ")
                    food_item_numbers = [int(num) for num in food_item_numbers.split(",")]
                    selected_food_items = []

                    for number in food_item_numbers:
                        if number == 1:
                            selected_food_items.append(FoodItem(1, "Tandoori Chicken", "4 pieces", 240, 0, 100))
                        elif number == 2:
                            selected_food_items.append(FoodItem(2, "Vegan Burger", "1 piece", 320, 0, 50))
                        elif number == 3:
                            selected_food_items.append(FoodItem(3, "Truffle Cake", "500gm", 900, 0, 20))
                        else:
                            print("Invalid food item number!")

                    user.place_new_order(selected_food_items)

                elif user_choice == "2":
                    # Order History
                    user.view_order_history()

                elif user_choice == "3":
                    # Update Profile
                    full_name = input("Enter your full name (leave blank to skip): ")
                    phone_number = input("Enter your phone number (leave blank to skip): ")
                    email = input("Enter your email (leave blank to skip): ")
                    address = input("Enter your address (leave blank to skip): ")
                    password = input("Enter your password (leave blank to skip): ")

                    user.update_profile(full_name, phone_number, email, address, password)

                elif user_choice == "4":
                    # Log out as user
                    print("Logging out as user...")
                    break

                else:
                    print("Invalid choice. Please try again.")

        else:
            print("Invalid email or password. Please try again.")

    elif choice == "4":
        # Exit
        print("Exiting the application...")
        break

    else:
        print("Invalid choice. Please try again.")


# In[ ]:




