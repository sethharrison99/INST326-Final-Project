import math
import time
import random
import re # Favour
import json


class Restaurant:

    # Ruchir
    def __init__(self, name="Customer"):
        self.name=name
    
    def getMenu():
        """
        Returns the restaurant's menu items.

        Returns:
            dict: A dictionary of menu items categorized by type.

        Author: Ruchir
        """
        menu_items = {
            "Appetizers": {"Garlic Bread": 3.00, "Chicken Wings": 5.99, "Quesadilla": 4.00, "Nachos": 4.50, "Onion Rings": 2.99},
            "Entrees": {"Hamburger": 4.99, "Cheeseburger": 5.49, "Chicken Sandwich": 5.99, "Veggie Burger": 4.99, "Pasta": 6.50, "Rice Bowl": 5.00, "Tacos": 3.00, "Burrito": 6.00},
            "Salads": {"Salad": 3.49, "Fruit Salad": 4.00, "Caesar Salad": 4.50, "Greek Salad": 4.75, "Garden Salad": 3.99},
            "Drinks": {"Soda": 1.50, "Ice Tea": 1.50, "Coffee": 2.00, "Milkshake": 3.50},
            "Sides": {"Fries": 2.49, "Cole Slaw": 2.00, "Mashed Potatoes": 2.50},
            "Desserts": {"Ice Cream": 2.50, "Cheesecake": 4.00, "Brownie": 3.00}
        }

        return menu_items
    
    def find_items_by_feature(self, feature):
        """
        Finds all menu items that contain a specific feature or ingredient in their name using a comprehension.

        Args:
            feature (str): The feature or ingredient to search for in the item names.

        Returns:
            list: A list of items that contain the feature in their name.

        Author: Ruchir
        Technique(s): Comprehensions
        """
        menu_items = self.getMenu()
        # Use a comprehension to filter items by feature
        return [name for category, items in menu_items.items() for name in items if feature.lower() in name.lower()]
    
    def serialize_order(self, order):
        """
        Serialize the order to JSON format.

        Args:
            order (dict): The order to serialize.

        Returns:
            str: The JSON string of the order.

        Author: Favour
        Technique(s): Use of json.dumps()
        """
        return json.dumps(order)


    def getOptions():
        options = {
        """
        Returns sub-options for specific menu items.

        Returns:
            dict: A dictionary of item options.

        Author: Ruchir
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
        return options
    
    

    def display_menu(self):
        """
        Displays the restaurant menu.
        
        Author: Seth
        Technique(s): F-strings containing expressions
        """
        menu_items = Restaurant.getMenu()
        for category, items in menu_items.items():
            print(f"\n{category}:")
            for item, price in items.items():
                print(f"  {item}: ${price:.2f}")






    def greet_customer(self, name, greeting='Hello'):
        """
        Greets the customer with an optional greeting.

        Args:
            name (str): The name of the customer.
            greeting (str, optional): The greeting to use. Defaults to 'Hello'.

        Author: Favour
        Technique(s): Optional parameters and/or keyword arguments
        """
        print(f"{greeting}, {self.name}!")

    def display_sorted_menu(self):
        """
        Displays the menu items sorted by category.

        Author: Seth
        Technique(s): Use of a key function with sorted()
        """
        menu_items = self.getMenu()
        sorted_items = sorted(menu_items.items(), key=lambda x: x[0])
        for category, items in sorted_items:
            print(f"\n{category}:")
            for item, price in items.items():
                print(f"  {item}: ${price:.2f}")

    def validate_dining_option(option):
        """
        Validates the dining option using regular expressions.

        Args:
            option (str): The dining option to validate.

        Returns:
            bool: True if the option is valid, False otherwise.

        Author: Favour
        Technique(s): Regular expressions
        """
        if re.match(r"Dine-In|Pickup|Delivery", option, re.IGNORECASE):
            return True
        else:
            return False

    class Order:
        """
        Represents an order with an ID and items.

        Author: Emerald
        """
        def __init__(self, order_id, items):
            """
            Initializes the Order object with an order ID and items.

            Args:
                order_id (str): The unique identifier for the order.
                items (dict): The items included in the order.
            """
            self.order_id = order_id
            self.items = items

        def __str__(self):
            """
            Returns a string representation of the Order object.

            Returns:
                str: The string representation of the order.

            Author: Emerald
            Technique(s): Magic methods other than __init__()
            """
            return f"Order ID: {self.order_id}, Items: {self.items}"



    def customize_item(item, options):
        """
        Customizes an item based on available options using conditional expressions.

        Args:
            item (str): The menu item to customize.
            options (dict): The available customization options.

        Returns:
            str: The customized item description.

        Author: Seth
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

    def add_to_order(self, item, order, options):
        """
        Adds an item to the order and updates its quantity using sequence unpacking.

        Args:
            item (str): The menu item to add to the order.
            order (dict): The current order.
            options (dict): The available item options.

        Author: Emerald
        Technique(s): Sequence unpacking
        """
        if item in options:
            customized_item = Restaurant.customize_item(item, options)
            order[customized_item] = order.get(customized_item, 0) + 1
        else:
            order[item] = order.get(item, 0) + 1

    def validate_menu_item(self, user_input):
        """
    Validates whether the user's input corresponds to a menu item.
    
    Args:
        user_input (str): The input string to validate against the menu items.

    Returns:
        bool: True if the input matches a menu item, False otherwise.

    Author: Emerald
    Technique(s): None claimed for this method.
    """
        menu_items = Restaurant.getMenu()
        for category, items in menu_items.items():
            if user_input in items:
                return True
        return False

    def take_order(self, options):
        """
        Takes the customer's order, allowing them to select and customize items.

        Args:
        options (dict): The dictionary of customization options for specific menu items.

        Returns:
        dict: The completed order with items and quantities.

        Author: Seth
        """
        order = {}
        while True:
            user_input = input("Select an item (or type 'Done' to finish): ")
            if user_input.lower() == 'done':
                break

            if self.validate_menu_item(user_input):
                self.add_to_order(user_input, order, options)
            else:
                print("Item not on the menu. Please try again.")
            
            self.display_current_order(order)

        return order

    def display_current_order(self, order):
        """
        Displays the current order with each item, its quantity, and the total price.

        Args:
        order (dict): The current order containing items and their quantities.

        Author: Emerald
        """
        menu_items = Restaurant.getMenu()
        total_price = 0.0
        print("\nCurrent Order:")
        for item, quantity in order.items():
            base_item = item.split(" - ")[0] if " - " in item else item
            price = next((menu_items[category][base_item] for category in menu_items if base_item in menu_items[category]), 0)
            total_price += price * quantity
            print(f"  {item} x{quantity}: ${price:.2f}")
        print(f"Total Price: ${total_price:.2f}")

    def rewardPoints(self, total_price):
        """
        Calculates reward points based on the total price of the order.

        Args:
            total_price (float): The total price of the order.

        Returns:
            int: The updated reward points after any redemptions.

        Author: Favour               
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
                answer = input(f"Wow {self.name}! You have {users_points}, which enough points to redeem for free items would like to redeem your points. (Yes/Not now)")
                if answer == "Yes" or answer == "yes":
                        print(f"{self.name}! Here is a list of items that can be redeemed based on the number of points you have! (You can only redeem one item at a time)")
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
                            return users_points
                        for item in items_displayed:
                            if item_to_redeem == item:
                                index = items_displayed.index(item)
                                users_points = users_points - price_displayed[index]
                                print(f"You redeemed your points for the {item_to_redeem}, you now have {users_points} points left")
                                return users_points
                else:
                    return users_points
        return users_points


    def generate_order_id():
        """
        Generates a unique order ID.

        Returns:
            str: A unique order ID.

        Author: Favour
        """
        timestamp = int(time.time())
        random_number = random.randint(100, 999)
        return f"Order{timestamp}{random_number}"

    def finalize_order(self, order):
        """
        Finalizes the order, calculates total price, awards points, and generates an ID.

        Args:
            order (dict): The current order.

        Returns:
            tuple: The order ID and dining option.

        Author: Ruchir
        """
        menu_items = Restaurant.getMenu()
        total_price = sum(menu_items[category][item.split(" - ")[0]] * quantity for item, quantity in order.items() for category in menu_items if item.split(" - ")[0] in menu_items[category])
        print("\nFinal Order:")
        self.display_current_order(order)
        points_earned = self.rewardPoints(total_price)
        print(f"Total Price: ${total_price:.2f}")
        print(f"Reward Points: {points_earned} points")

        dining_option = input("Choose your dining option (Dine-In/Pickup/Delivery): ")
        order_id = Restaurant.generate_order_id()
        print(f"Thank you for your order! Your order ID is {order_id}.")
        
        return order_id, dining_option

    def orderStatusTracker(order_id, dining_option):
        """
        Tracks and updates the order status.

        Args:
            order_id (str): The order ID.
            dining_option (str): The chosen dining option.

        Returns:
            str: The final status of the order.

        Author: Ruchir
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
if __name__ == "__main__":

    r= Restaurant("JohnDoe")
    print(r.greet_customer("JohnDoe"))
    print(r.display_menu())
        
    
    options = Restaurant.getOptions()
    order = r.take_order(options)
    order_id, dining_option = r.finalize_order(order)
    final_status = Restaurant.orderStatusTracker(order_id, dining_option)
