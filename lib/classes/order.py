class Order:
    all = []
    
    def __init__(self, customer, coffee, price):
        self._customer = None
        self._coffee = None
        self._price = None
        
        self.customer = customer  
        self.coffee = coffee      
        self.price = price        
        
        Order.all.append(self)
        
        coffee.add_order(self)
        coffee.add_customer(customer)
        
        customer.add_order(self)
        customer.add_coffee(coffee)
        
    def __repr__(self):
        return f"{self.customer.name} ordered {self.coffee.name}"
    
    @property 
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)) and 1.0 <= value <= 10.0:
            if self._price is None:
                self._price = float(value)
            else:
                raise Exception("Price cannot be changed once set.")
        else:
            raise Exception("Price must be a number between 1.0 and 10.0 inclusive.")
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        from classes.customer import Customer
        if isinstance(value, Customer):
            if self._customer is None:
                self._customer = value
            else:
                raise Exception("Customer cannot be changed once set.")
        else:
            raise Exception("You must pass a Customer object.")
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        from classes.coffee import Coffee
        if isinstance(value, Coffee):
            if self._coffee is None:
                self._coffee = value
            else:
                raise Exception("Coffee cannot be changed once set.")
        else:
            raise Exception("You must pass a Coffee object.")
def orders(self):
    # Add debugging to verify orders list
    print(f"Orders list for {self.name}: {self._orders}")
    return [order for order in self._orders if isinstance(order, Order)]
