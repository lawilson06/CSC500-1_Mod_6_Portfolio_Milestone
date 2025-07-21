"""
CSC500-1 Module 6 Portfolio Milestone
Lawrence Wilson
July 21, 2025
"""

from ItemToPurchase import ItemToPurchase
from ShoppingCart import ShoppingCart

ERROR_MSG = "Please enter a valid selection."
ERROR_MSG2 = "Please enter a valid value."

user_items = []
customer_name = input('Enter the customer name: ').strip()
shopping_cart = ShoppingCart(customer_name)

# Function to obtain user inputs for two items as outlined in assignment (name, description, quantity, and price) try-except
def user_inputs():
    print("Enter your shopping cart item ✏✏") #Update for add item
    print("----------------------")
    while True:
        try:
            temp_name = input("Enter the item name: ")
            temp_description = input("Enter the item description: ")
            while True:
                temp_quantity = int(input("Enter the item quantity: "))
                if temp_quantity <= 0:
                    print(ERROR_MSG2)
                else:
                    break
            temp_price = float(input("Enter the item price: "))
            temp_item_dict = {
                'user_item_name': temp_name,
                'user_item_quantity': temp_quantity,
                'user_item_price': temp_price,
                'user_item_description': temp_description
            }
            user_items.append(temp_item_dict)
            break
        except ValueError as e:
            print(e, ERROR_MSG2)

# Menu selection list as outlined in assignment
def user_menu_selection():
    while True:
        selection_list = ['A','R','U','I','O','Q']
        user_selection = ""
        print('Menu\nA - Add Item to cart\nR - Remove item from cart\nU - Update item\nI - Output item description'
              '\nO - Output shopping cart\nQ - Quit')
        try:
            user_selection = input('Please enter your selection: ').upper().strip()
        except ValueError:
            print(ERROR_MSG)

        if user_selection in selection_list:
            break
        else:
            print(ERROR_MSG)
    return user_selection

# Match case statements are used to implement the add item, remove item, update item (change item), output item descriptions, output shopping cart, and quit options
while True:
    menu_option = user_menu_selection()

    match menu_option:
        case 'A':
            user_inputs()
            existing_record, item_position = shopping_cart.check_existing_item(user_items[-1]['user_item_name'])
            if existing_record:
                print('Item already exists. Making updates instead. Make further updates using "Update" option.')
                shopping_cart.modify_existing_item(item_position=item_position,price=user_items[-1]['user_item_price'],
                                                   quantity=shopping_cart.get_shopping_list_item(item_position).
                                                   get_item_quantity() + user_items[-1]['user_item_quantity'])
                print(shopping_cart.get_shopping_list_item(item_position).get_item_quantity())
            else:
                shopping_item = ItemToPurchase()
                shopping_item.set_item_name(user_items[-1]['user_item_name'])
                shopping_item.set_item_description(user_items[-1]['user_item_description'])
                shopping_item.set_item_price(user_items[-1]['user_item_price'])
                shopping_item.set_item_quantity(user_items[-1]['user_item_quantity'])
                shopping_cart.set_shopping_item(shopping_item)
        case 'R':
            remove_name = input('Which item do you wish to remove? Enter the name: ')
            can_remove, remove_position = shopping_cart.check_existing_item(remove_name)
            if can_remove:
                shopping_cart.get_shopping_list_item(remove_position).print_item_data()
                try:
                    remove_quantity = int(input("Enter the quantity you wish to remove: "))
                    shopping_cart.modify_existing_item(item_position=remove_position, quantity=shopping_cart.
                                                       get_shopping_list_item(remove_position).get_item_quantity()
                                                                                               - remove_quantity)
                except ValueError:
                    print(ERROR_MSG2)
            else:
                print(ERROR_MSG)
        case 'U':
            update_items = ['name','price','quantity','description','done']
            shopping_cart.get_cart_data()
            update_name = input('Which item do you wish to update?  Enter the name: ')
            can_update, update_position = shopping_cart.check_existing_item(update_name)
            if can_update:
                while True:
                    update_choice = input('What do you wish to update?  Name, price, quantity, or '
                                          'description? Enter "Done" when finished.\n').lower().strip()
                    if update_choice in update_items:
                        match update_choice:
                            case 'name':
                                u_name = input("Enter the new name: ")
                                shopping_cart.modify_existing_item(item_position=update_position, name=u_name)
                            case 'description':
                                u_description = input("Enter the new description: ")
                                shopping_cart.modify_existing_item(item_position=update_position,
                                                                   description=u_description)
                            case 'price':
                                while True:
                                    try:
                                        u_price = float(input("Enter the new price: "))
                                        shopping_cart.modify_existing_item(item_position=update_position, price=u_price)
                                        break
                                    except ValueError:
                                        print(ERROR_MSG2)
                            case 'quantity':
                                while True:
                                    try:
                                        u_quantity = int(input('Enter the new quantity: '))
                                        shopping_cart.modify_existing_item(item_position=update_position, quantity=u_quantity)
                                        break
                                    except ValueError:
                                        print(ERROR_MSG2)
                            case 'done':
                                shopping_cart.get_shopping_list_item(update_position).print_item_data()
                                print('Updates complete.')  # Add print on item updated
                                break
                    else:
                        print(ERROR_MSG)
        case 'I':
            shopping_cart.get_cart_item_descriptions()
        case 'O':
            shopping_cart.get_cart_total_cost()
        case 'Q':
            print('Exiting the program.')
            break


