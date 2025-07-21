from datetime import datetime

ERROR_MSG = 'Shopping list is empty.'

class ShoppingCart:
    def __init__(self, customer_name):
        self.__cart_initialized_date = datetime.now().strftime("%B %d, %Y")
        self.__customer_name = customer_name
        self.__menu_title = f"{self.__customer_name}'s Shopping Cart | Date: {self.__cart_initialized_date}"
        self.__cart_quantity = 0
        self.__cart_total = 0
        self.__shopping_list = []

    def __calculate_quantity(self):
        for item in self.__shopping_list:
            self.__cart_quantity += item.get_item_quantity()

    def __calculate_total(self):
        for item in self.__shopping_list:
            self.__cart_total += item.get_item_total_price()

    def __remove_items(self):
        for index, item in enumerate(self.__shopping_list):
            if item.get_item_quantity() <= 0:
                print(f"{item.get_item_name()} removed.")
                self.__shopping_list.pop(index)

    #Add quantity for adding an existing items or update quantity if modifying quantity in cart
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

    def get_cart_item_descriptions(self):
        print(self.__menu_title)
        if len(self.__shopping_list) > 0:
            for item in self.__shopping_list:
                print(f"{item.get_item_name()}:{item.get_item_description()}")
        else:
            print(ERROR_MSG)

    def get_cart_total_cost(self):
        self.__calculate_quantity()
        self.__calculate_total()
        print(self.__menu_title)
        print(f"Number of items: {self.__cart_quantity}")
        for item in self.__shopping_list:
            item.print_item_cost()
        print(f"Total: ${self.__cart_total}")
