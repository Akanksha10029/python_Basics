import sqlite3

class connection_db:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        """Connect to SQLite database"""
        self.conn = sqlite3.connect('bakery.db')
        # Create a cursor object using the connection
        self.cursor = self.conn.cursor()

    def close(self):
        """Close the SQLite database connection"""
        # Close the database connection if it exists
        if self.conn:
            self.conn.close()

    def create_tables(self):
        # Create Customers table
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customers (
            customer_id INTEGER PRIMARY KEY,
            name TEXT,
            address TEXT,
            contact_no TEXT
            )
        ''')

        # Create Products table
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            product_id INTEGER PRIMARY KEY,
            name TEXT,
            category TEXT,
            available_quantity INTEGER,
            price REAL
            )
        ''')

        # Create Orders table
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Orders (
            order_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            order_date TEXT,
            delivery_date TEXT,
            total_amount REAL,
            FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
            )
        ''')

        # Create OrderItems table
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS OrderItems (
            order_item_id INTEGER PRIMARY KEY,
            order_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            FOREIGN KEY (order_id) REFERENCES Orders(order_id),
            FOREIGN KEY (product_id) REFERENCES Products(product_id)
            )
        ''')

        # Create Suppliers table
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Suppliers (
            supplier_id INTEGER PRIMARY KEY,
            name TEXT,
            address TEXT,
            contact_info TEXT
            )
        ''')    

        # Create Feedback table
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Feedback (
            feedback_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            product_id INTEGER,
            rating INTEGER,
            comments TEXT,
            FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
            FOREIGN KEY (product_id) REFERENCES Products(product_id)
            )
        ''')
        
    # insert data------------->
    
    def insert_customer(self, name, address, contact_no):
        self.cursor.execute('''
        INSERT INTO Customers (name, address, contact_no)
        VALUES (?, ?, ?)
        ''', (name, address, contact_no))
        self.conn.commit()

    def insert_product(self, name, category, available_quantity, price):
        self.cursor.execute('''
        INSERT INTO Products (name, category, available_quantity, price)
        VALUES (?, ?, ?, ?)
        ''', (name, category, available_quantity, price))
        self.conn.commit()

    def insert_order(self, customer_id, order_date, delivery_date, total_amount):
        self.cursor.execute('''
        INSERT INTO Orders (customer_id, order_date, delivery_date, total_amount)
        VALUES (?, ?, ?, ?)
        ''', (customer_id, order_date, delivery_date, total_amount))
        self.conn.commit()

    def insert_order_item(self, order_id, product_id, quantity):
        self.cursor.execute('''
        INSERT INTO OrderItems (order_id, product_id, quantity)
        VALUES (?, ?, ?)
        ''', (order_id, product_id, quantity))
        self.conn.commit()

    def insert_supplier(self, name, address, contact_info):
        self.cursor.execute('''
        INSERT INTO Suppliers (name, address, contact_info)
        VALUES (?, ?, ?)
        ''', (name, address, contact_info))
        self.conn.commit()

    def insert_feedback(self, customer_id, product_id, rating, comments):
        self.cursor.execute('''
        INSERT INTO Feedback (customer_id, product_id, rating, comments)
        VALUES (?, ?, ?, ?)
        ''', (customer_id, product_id, rating, comments))
        self.conn.commit()
        
    # Retreive data----------->    

    def get_customers(self):
        self.cursor.execute('SELECT * FROM Customers')
        return self.cursor.fetchall()

    def get_products(self):
        self.cursor.execute('SELECT * FROM Products')
        return self.cursor.fetchall()

    def get_orders(self):
        self.cursor.execute('SELECT * FROM Orders')
        return self.cursor.fetchall()

    def get_order_items(self):
        self.cursor.execute('SELECT * FROM OrderItems')
        return self.cursor.fetchall()

    def get_suppliers(self):
        self.cursor.execute('SELECT * FROM Suppliers')
        return self.cursor.fetchall()

    def get_feedback(self):
        self.cursor.execute('SELECT * FROM Feedback')
        return self.cursor.fetchall()
    
    def delete_order(self, order_id):
        # Check if the order ID exists in the database
        self.cursor.execute('SELECT * FROM Orders WHERE order_id = ?', (order_id,))
        order = self.cursor.fetchone()
        
        if order:
            # Fetch customer details for the success message
            self.cursor.execute('SELECT name FROM Customers WHERE customer_id = ?', (order[1],))
            customer = self.cursor.fetchone()
            
            if customer:
                # Delete order items first
                self.cursor.execute('DELETE FROM OrderItems WHERE order_id = ?', (order_id,))
                # Delete the order
                self.cursor.execute('DELETE FROM Orders WHERE order_id = ?', (order_id,))
                self.conn.commit()
                customer_name = customer[0]
                print(f"The order for customer '{customer_name}' (ID: {order[1]}) has been cancelled successfully.")
            else:
                print("Customer associated with this order does not exist.")
        else:
            print("The order ID is incorrect or does not exist.")
    
# # Insert data
# db.insert_customer('Alice', '123 Main St', '555-1234')
# db.insert_product('Chocolate Cake', 'Cake', 10, 15.99)
# db.insert_order(1, '2023-07-15', '2023-07-16', 15.99)
# db.insert_order_item(1, 1, 1)
# db.insert_supplier('Baking Supplies Co.', '456 Supplier St', '555-5678')
# db.insert_feedback(1, 1, 5, 'Delicious cake!')

def main_menu():
    print("Welcome to the Sasta kirana store Management System")
    print("1. Add Customer")
    print("2. View Customers")
    print("3. Add Product")
    print("4. View Products")
    print("5. Add Order")
    print("6. View Orders")
    print("7. Add Order Item")
    print("8. View Order Items")
    print("9. Add Supplier")
    print("10. View Suppliers")
    print("11. Add Feedback")
    print("12. View Feedback")
    print("13. cancel customer order")
    print("14. Exit")

from tabulate import tabulate

def add_customer(db):
    name = input("Enter customer name: ")
    address = input("Enter customer address: ")
    contact_no = input("Enter customer contact number: ")
    db.insert_customer(name, address, contact_no)
    print("Customer added successfully!")

def view_customers(db):
    customers = db.get_customers()
    if not customers:
        print("The customer data is empty.")
    else:
        headers = ["Customer_id", "Name", "Address", "Contact No"]
        print(tabulate(customers, headers, tablefmt="pretty"))

def add_product(db):
    name = input("Enter product name: ")
    category = input("Enter product category: ")
    available_quantity = int(input("Enter available quantity: "))
    price = float(input("Enter product price: "))
    db.insert_product(name, category, available_quantity, price)
    print("Product added successfully!")

def view_products(db):
    products = db.get_products()
    headers = ["Product_id", "Name", "Category", "Available Quantity", "Price"]
    print(tabulate(products, headers, tablefmt="pretty"))

def add_order(db):
    customer_id = int(input("Enter customer ID: "))
    order_date = input("Enter order date (YYYY-MM-DD): ")
    delivery_date = input("Enter delivery date (YYYY-MM-DD): ")
    total_amount = float(input("Enter total amount: "))
    db.insert_order(customer_id, order_date, delivery_date, total_amount)
    print("Order added successfully!")

def view_orders(db):
    orders = db.get_orders()
    headers = ["Order ID", "Customer ID", "Order Date", "Delivery Date", "Total Amount"]
    print(tabulate(orders, headers, tablefmt="pretty"))

def add_order_item(db):
    order_id = int(input("Enter order ID: "))
    product_id = int(input("Enter product ID: "))
    quantity = int(input("Enter quantity: "))
    db.insert_order_item(order_id, product_id, quantity)
    print("Order item added successfully!")

def view_order_items(db):
    order_items = db.get_order_items()
    headers = ["Order Item ID", "Order ID", "Product ID", "Quantity"]
    print(tabulate(order_items, headers, tablefmt="pretty"))

def add_supplier(db):
    name = input("Enter supplier name: ")
    address = input("Enter supplier address: ")
    contact_info = input("Enter supplier contact info: ")
    db.insert_supplier(name, address, contact_info)
    print("Supplier added successfully!")

def view_suppliers(db):
    suppliers = db.get_suppliers()
    headers = ["Supplier ID", "Name", "Address", "Contact Info"]
    print(tabulate(suppliers, headers, tablefmt="pretty"))

def add_feedback(db):
    customer_id = int(input("Enter customer ID: "))
    product_id = int(input("Enter product ID: "))
    rating = int(input("Enter rating (1-5): "))
    comments = input("Enter comments: ")
    db.insert_feedback(customer_id, product_id, rating, comments)
    print("Feedback added successfully!")

def view_feedback(db):
    feedback = db.get_feedback()
    headers = ["Feedback ID", "Customer ID", "Product ID", "Rating", "Comments"]
    print(tabulate(feedback, headers, tablefmt="pretty"))

def cancel_order(db):
    order_id = int(input("Enter order ID to cancel: "))
    db.delete_order(order_id)
    print("Order cancelled successfully!")

def main():
    db = connection_db()
    db.connect()
    db.create_tables()

    while True:
        main_menu()
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                add_customer(db)
            case 2:
                view_customers(db)
            case 3:
                add_product(db)
            case 4:
                view_products(db)
            case 5:
                add_order(db)
            case 6:
                view_orders(db)
            case 7:
                add_order_item(db)
            case 8:
                view_order_items(db)
            case 9:
                add_supplier(db)
            case 10:
                view_suppliers(db)
            case 11:
                add_feedback(db)
            case 12:
                view_feedback(db)
            case 13:
                cancel_order(db)
            case 14:
                db.close()
                print("Exiting...")
                break
            case _:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()