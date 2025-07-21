from datetime import datetime

ERROR_MSG = 'Shopping list is empty.'

class ShoppingCart:
    def __init__(self, customer_name):
        self.__cart_initialized_date = "January 1, 2020"
        self.__assign_current_date()
        self.__customer_name = customer_name
        self.__menu_title = f"{self.__customer_name}'s Shopping Cart | Date: {self.__cart_initialized_date}"
        self.__cart_quantity = 0
        self.__cart_total = 0
        self.__shopping_list = []

    def __assign_current_date(self):
        self.__cart_initialized_date = datetime.now().strftime("%B %d, %Y")

    # Private helper function to calculate cart's total quantity
    def __calculate_quantity(self):
        for item in self.__shopping_list:
            self.__cart_quantity += item.get_item_quantity()

    # Private helper function to calculate cart's total cost
    def __calculate_total(self):
        for item in self.__shopping_list:
            self.__cart_total += item.get_item_total_price()

    # Private remove items helper function is utilized in modify function to remove items if quantity is 0 or under
    def __remove_items(self):
        for index, item in enumerate(self.__shopping_list):
            if item.get_item_quantity() <= 0:
                print(f"{item.get_item_name()} removed.")
                self.__shopping_list.pop(index)

    # Add quantity for adding an existing items or update quantity if modifying quantity in cart
    def modify_existing_item(self, item_position, description=None, name=None, price=None, quantity=None):

        if quantity is not None:
            self.__shopping_list[item_position].set_item_quantity(quantity)
            self.__remove_items()

        if price is not None:
            self.__shopping_list[item_position].set_item_price(price)

        if name is not None:
            self.__shopping_list[item_position].set_item_name(name)

        if description is not None:
            self.__shopping_list[item_position].set_item_description(description)

    def check_existing_item(self, name):
        found_item = False
        item_position = None
        for index, item in enumerate(self.__shopping_list):
            if item.get_item_name().lower().strip() == name.lower().strip():
                found_item = True
                item_position = index
                break
        return found_item, item_position

    def set_shopping_item(self, item):
        self.__shopping_list.append(item)

    def get_shopping_list_item(self, position):
        return self.__shopping_list[position]

    def get_cart_date(self):
        return self.__cart_initialized_date

    def get_cart_data(self):
        print(self.__menu_title)
        for item in self.__shopping_list:
            item.print_item_data()

    # print cart item descriptions
    def get_cart_item_descriptions(self):
        print(self.__menu_title)
        if len(self.__shopping_list) > 0:
            for item in self.__shopping_list:
                print(f"{item.get_item_name()}:{item.get_item_description()}")
        else:
            print(ERROR_MSG)

    # get num items in cart
    def get_cart_quantity(self):
        self.__calculate_quantity()
        return self.__cart_quantity

    # get cost of cart
    def get_cart_cost(self):
        self.__calculate_total()
        return self.__cart_total

    # print cart total
    def get_cart_total_cost(self):
        print(self.__menu_title)
        print(f"Number of items: {self.get_cart_quantity()}")
        for item in self.__shopping_list:
            item.print_item_cost()
        print(f"Total: ${self.get_cart_cost()}")
