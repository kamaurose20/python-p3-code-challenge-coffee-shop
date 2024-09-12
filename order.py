class Order:
    all = []  # Class-level list to keep track of all orders
    
    def __init__(self, customer, coffee, price):
        # Initialize the order with customer, coffee, and price attributes
        self._customer = None
        self._coffee = None
        self._price = None
        
        # Set customer, coffee, and price using the property setters
        self.customer = customer
        self.coffee = coffee
        self.price = price
        
        # Append the order to the class-level order list
        Order.all.append(self)
        
        # Associate the order with the customer and coffee
        coffee.add_order(self)
        customer.add_order(self)
    
    def __repr__(self):
        # Return a string representation of the order
        return f"{self.customer.name} ordered {self.coffee.name}"
    
    @property 
    def price(self):
        # Return the price of the order
        return self._price
    
    @price.setter
    def price(self, value):
        # Validate and set the price if it's between 1.0 and 10.0 and hasn't been set before
        if isinstance(value, (int, float)) and 1.0 <= value <= 10.0:
            if self._price is None:
                self._price = float(value)
            else:
                raise Exception("Price cannot be changed once set.")
        else:
            raise ValueError("Price must be a number between 1.0 and 10.0 inclusive.")
    
    @property
    def customer(self):
        # Return the customer associated with this order
        return self._customer
    
    @customer.setter
    def customer(self, value):
        from customer import Customer
        # Set the customer if it's a valid Customer instance and hasn't been set before
        if isinstance(value, Customer):
            if self._customer is None:
                self._customer = value
            else:
                raise Exception("Customer cannot be changed once set.")
        else:
            raise ValueError("You must pass a Customer object.")
    
    @property
    def coffee(self):
        # Return the coffee associated with this order
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee
        # Set the coffee if it's a valid Coffee instance and hasn't been set before
        if isinstance(value, Coffee):
            if self._coffee is None:
                self._coffee = value
            else:
                raise Exception("Coffee cannot be changed once set.")
        else:
            raise ValueError("You must pass a Coffee object.")

# Debugging Orders
def orders(self):
    # Add debugging to verify the orders list for the coffee or customer
    print(f"Orders list for {self.name}: {self._orders}")
    return [order for order in self._orders if isinstance(order, Order)]
