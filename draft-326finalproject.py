import math
import time
import random
import re # Favour

# Ruchir
menu_items = {
    "Appetizers": {"Garlic Bread": 3.00, "Chicken Wings": 5.99, "Quesadilla": 4.00, "Nachos": 4.50, "Onion Rings": 2.99},
    "Entrees": {"Hamburger": 4.99, "Cheeseburger": 5.49, "Chicken Sandwich": 5.99, "Veggie Burger": 4.99, "Pasta": 6.50, "Rice Bowl": 5.00, "Tacos": 3.00, "Burrito": 6.00},
    "Salads": {"Salad": 3.49, "Fruit Salad": 4.00, "Caesar Salad": 4.50, "Greek Salad": 4.75, "Garden Salad": 3.99},
    "Drinks": {"Soda": 1.50, "Ice Tea": 1.50, "Coffee": 2.00, "Milkshake": 3.50},
    "Sides": {"Fries": 2.49, "Cole Slaw": 2.00, "Mashed Potatoes": 2.50},
    "Desserts": {"Ice Cream": 2.50, "Cheesecake": 4.00, "Brownie": 3.00}
}

def display_menu():
    """
    Displays the restaurant menu.
    
    Primary Student: Seth
    Technique(s): F-strings containing expressions
    """
    for category, items in menu_items.items():
        print(f"\n{category}:")
        for item, price in items.items():
            print(f"  {item}: ${price:.2f}")


def customize_item(item, options):
    """
    Customizes an item based on available options.

    Primary Student: Ruchir
    Technique(s): Conditional expressions
    """
    if item in options:
        print(f"Choose a flavor for {item}:")
        for option in options[item]:
            print(option)
        choice = input("Your choice: ")
        return f"{item} - {choice}"
    else:
        return item

def add_to_order(item, order, options):
    """
    Adds an item to the order, customized if options are available.

    Primary Student: Ruchir
    Technique(s): Sequence unpacking
    """
    if item in options:
        customized_item = customize_item(item, options)
        order[customized_item] = order.get(customized_item, 0) + 1
    else:
        order[item] = order.get(item, 0) + 1

def greet_customer(greeting='Hello', name='Customer'):
    """
    Greets the customer with an optional greeting and name.

    Primary Student: Favour
    Technique(s): Optional parameters and/or keyword arguments
    """
    print(f"{greeting}, {name}!")

def display_sorted_menu():
    """
    Displays the menu items sorted by category.

    Primary Student: Seth
    Technique(s): Use of a key function with sorted()
    """
    sorted_items = sorted(menu_items.items(), key=lambda x: x[0])
    for category, items in sorted_items:
        print(f"\n{category}:")
        for item, price in items.items():
            print(f"  {item}: ${price:.2f}")

def validate_dining_option(option):
    """
    Validates the dining option using regular expressions.

    Primary Student: Favour
    Technique(s): Regular expressions
    """
    if re.match(r"Dine-In|Pickup|Delivery", option, re.IGNORECASE):
        return True
    else:
        return False

class Order:
    """
    Represents an order with an ID and items.

    Primary Student: Emerald
    """
    def __init__(self, order_id, items):
        """
        Initializes the Order object with an order ID and items.

        """
        self.order_id = order_id
        self.items = items

    def __str__(self):
        """
        Returns a string representation of the Order object.

        Technique(s): Magic methods
        """
        return f"Order ID: {self.order_id}, Items: {self.items}"



def customize_item(item, options):
    """
    Allows customization of a menu item based on available options.
    
    Primary Student: Seth
    Technique(s): Conditional expressions
    """
    if item in options:
        print(f"Choose a flavor for {item}:")
        for option in options[item]:
            print(option)
        choice = input("Your choice: ")
        return f"{item} - {choice}"
    else:
        return item

def add_to_order(item, order, options):
    """
    Adds an item to the order, optionally customized, and updates the order's quantity.

    Primary Student: Emerald
    Technique(s): Sequence unpacking
    """
    if item in options:
        customized_item = customize_item(item, options)
        order[customized_item] = order.get(customized_item, 0) + 1
    else:
        order[item] = order.get(item, 0) + 1

def validate_menu_item(user_input):
    """
    Validates whether the user's input corresponds to a menu item.

    Primary Student: Emerald
    Technique(s): None claimed for this method.
    """
    for category, items in menu_items.items():
        if user_input in items:
            return True
    return False

def take_order(options):
    """
    Takes the customer's order, allowing them to select and customize items.

    Primary Student: Seth
    Technique(s): None claimed for this method.
    """
    order = {}
    while True:
        user_input = input("Select an item (or type 'Done' to finish): ")
        if user_input.lower() == 'done':
            break

        if validate_menu_item(user_input):
            add_to_order(user_input, order, options)
        else:
            print("Item not on the menu. Please try again.")
        
        display_current_order(order)

    return order

def display_current_order(order):
    """
    Displays the current order with each item, its quantity, and the total price.

    Primary Student: Emerald
    Technique(s): None claimed for this method.
    """
    total_price = 0.0
    print("\nCurrent Order:")
    for item, quantity in order.items():
        base_item = item.split(" - ")[0] if " - " in item else item
        price = next((menu_items[category][base_item] for category in menu_items if base_item in menu_items[category]), 0)
        total_price += price * quantity
        print(f"  {item} x{quantity}: ${price:.2f}")
    print(f"Total Price: ${total_price:.2f}")

def rewardPoints(total_price):
    """
    Calculates reward points based on the total price of the order.

    Primary Student: Favour
    Technique(s): None claimed for this method.
    """
    points_per_dollar = 10
    # The list of items, and the corresponding price of the  item
    list_of_items = {"Cheeseburger": 150,
                            "Fries": 300,
                            "Milkshake": 450}
    #The reward points is calculated by multiplying the order amound by 100
    reward_points =  math.floor(total_price * points_per_dollar)

    #the user points is the points the user already has plus the reward points from the order
    users_points = reward_points

    print(f"You have {reward_points} reward points!")

        #The cheapest reward item is 1500, so they are eligible to redeem their points if they have >= 1500 points
    if (users_points >= 150):
            answer = input(f"Hello, You have {users_points}, which enough points to redeem for free items would like to redeem your points. (Yes/Not now)")
            if answer == "Yes" or answer == "yes":
                    print("Here is a list of items that can be redeemed based on the number of points you have! (You can only redeem one item at a time)")
                    count =0
                    items = []
                    items_displayed=[]
                    price_displayed = []
                    for i in list_of_items.keys():
                        items+=[i]
                    for price in list_of_items.values():
                        if users_points == price or users_points>price:
                            items_displayed.append(items[count])
                            price_displayed.append(price)
                            print(f"Item: {items[count]}; Price {price}")
                            count = count+1
                    item_to_redeem = input("Which item would you like to redeem? (Say the item or type 'Changed my mind')")
                    if item_to_redeem == "Changed my mind":
                        return
                    for item in items_displayed:
                        if item_to_redeem == item:
                            index = items_displayed.index(item)
                            users_points = users_points - price_displayed[index]
                            print(f"You redeemed your points for the {item_to_redeem}, you now have {users_points} points left")
                            return users_points
            else:
                    return


def generate_order_id():
    """
    Generates a unique order ID based on the current timestamp and a random number.

    Primary Student: Favour
    Technique(s): None claimed for this method.
    """
    timestamp = int(time.time())
    random_number = random.randint(100, 999)
    return f"Order{timestamp}{random_number}"

def finalize_order(order):
    """
    Finalizes the order by calculating the total price, awarding reward points, and generating an order ID.

    Primary Student: Ruchir
    Technique(s): None claimed for this method.
    """
    total_price = sum(menu_items[category][item.split(" - ")[0]] * quantity for item, quantity in order.items() for category in menu_items if item.split(" - ")[0] in menu_items[category])
    print("\nFinal Order:")
    display_current_order(order)
    points_earned = rewardPoints(total_price)
    print(f"Total Price: ${total_price:.2f}")
    print(f"Reward Points: {points_earned} points")

    dining_option = input("Choose your dining option (Dine-In/Pickup/Delivery): ")
    order_id = generate_order_id()
    print(f"Thank you for your order! Your order ID is {order_id}.")
    
    return order_id, dining_option

def orderStatusTracker(order_id, dining_option):
    """
    Tracks and updates the status of an order based on the chosen dining option.

    Primary Student: Ruchir
    Technique(s): None claimed for this method.
    """
    print(f"Order {order_id} Status Updates:")
    print("Preparing...")
    time.sleep(2)  # Simulating time delay for order preparation

    if dining_option.lower() == "delivery":
        final_status = "Out for Delivery"
    elif dining_option.lower() == "pickup":
        final_status = "Ready for Pickup"
    elif dining_option.lower() == "dine-in":
        final_status = "Delivered to Table"
    else:
        final_status = "Unknown"

    time.sleep(2)  # Simulating time delay for final status
    print(final_status)
    return final_status




# Main program
display_menu()
options = {
    """ 
    The sub options for specfic menu items
    
    Ruchir
    """
        "Quesadilla": ["Chicken", "Cheese", "Steak"],
        "Nachos": ["Chicken", "No Chicken"],
        "Tacos": ["Steak", "Chicken", "Fish", "Shrimp", "Brown Beans", "Black Beans", "None"],
        "Burrito": ["Steak", "Chicken", "Brown Beans", "Black Beans", "None"],
        "Soda": ["Cola", "Diet Cola", "Root Beer", "Orange", "Lemon-Lime", "Ginger Ale", "Grape"],
        "Milkshake": ["Cookies & Cream", "Vanilla", "Strawberry", "Chocolate"],
        "Ice Cream": ["Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip", "Butter Pecan", "Rocky Road", "Cookie Dough", "Neapolitan", "Pistachio", "Salted Caramel"],
        "Cheesecake": ["New York Style", "Chocolate", "Strawberry", "Lemon", "Blueberry"]
}


order = take_order(options)
order_id, dining_option = finalize_order(order)
final_status = orderStatusTracker(order_id, dining_option)
