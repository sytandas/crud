class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = []

    def add_item_to_menu(self, item, price):
        self.menu_items[item] = price

    def book_tables(self, table_number):
        self.book_table.append(table_number)

    def customer_order(self, table_number, order):
        #order_details = (f"table-number is {table_number} and order: {order}")
        order_details = {'table_number': table_number, 'order': order} 
        self.customer_orders.append(order_details)

    def print_menu_items(self):
        for item, price in self.menu_items.items():
            print(f"Menu-items -> item: {item}, price: {price}")

    def print_table_reservations(self):
        for table in self.book_table:
            print(f"Table {table}")

    def print_customer_orders(self):
        for order in self.customer_orders:
            print("Table {}: {}".format(order['table_number'], order['order']))
            #print(f"table_number: {table_number}, order: {order}")
restaurant = Restaurant()

# Add items
restaurant.add_item_to_menu("Rice",    20)
restaurant.add_item_to_menu("Dal",     15)
restaurant.add_item_to_menu("Sabji",   15)
restaurant.add_item_to_menu("Egg", 20)
restaurant.add_item_to_menu("Chicken", 30)

# Book table
restaurant.book_tables(1)
restaurant.book_tables(2)
restaurant.book_tables(3)
# Order items
restaurant.customer_order(1, "Rice")
restaurant.customer_order(1, "Dal")
restaurant.customer_order(2, "Rice")
restaurant.customer_order(2, "Egg")

print("\nPopular dishes in the restaurant along with their prices:")
restaurant.print_menu_items()

print("\nTable reserved in the Restaurant:")
restaurant.print_table_reservations()

print("\nPrint customer orders:")
restaurant.print_customer_orders()
