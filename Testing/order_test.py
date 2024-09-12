import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder:
    '''Tests for Order class'''

    def setup_method(self):
        '''Setup method to initialize test data'''
        # Clear the Order.all list to ensure test isolation
        Order.all = []
        self.customer = Customer('Steve')
        self.coffee = Coffee('Latte')
        self.order = Order(self.customer, self.coffee, 5.0)

    def test_order_initialization(self):
        '''Ensure Order is initialized correctly'''
        assert self.order.customer == self.customer
        assert self.order.coffee == self.coffee
        assert self.order.price == 5.0

    def test_order_repr(self):
        '''Ensure __repr__ method returns correct string'''
        assert repr(self.order) == 'Steve ordered Latte'

    def test_price_setter(self):
        '''Ensure price is set correctly and cannot be changed once set'''
        order = Order(self.customer, self.coffee, 3.0)
        assert order.price == 3.0
        
        with pytest.raises(Exception, match="Price cannot be changed once set."):
            order.price = 4.0  # Attempt to change price
        
        with pytest.raises(ValueError, match="Price must be a number between 1.0 and 10.0 inclusive."):
            order.price = 0.5  # Invalid price
    
    def test_customer_setter(self):
        '''Ensure customer is set correctly and cannot be changed once set'''
        another_customer = Customer('Dima')
        order = Order(self.customer, self.coffee, 5.0)
        
        with pytest.raises(Exception, match="Customer cannot be changed once set."):
            order.customer = another_customer
        
        with pytest.raises(ValueError, match="You must pass a Customer object."):
            order.customer = "NotACustomer"  # Invalid type

    def test_coffee_setter(self):
        '''Ensure coffee is set correctly and cannot be changed once set'''
        another_coffee = Coffee('Espresso')
        order = Order(self.customer, self.coffee, 5.0)
        
        with pytest.raises(Exception, match="Coffee cannot be changed once set."):
            order.coffee = another_coffee
        
        with pytest.raises(ValueError, match="You must pass a Coffee object."):
            order.coffee = "NotACoffee"  # Invalid type

    def test_orders_class_level(self):
        '''Ensure that orders are added to the class-level orders list'''
        # Create a new order to verify the count
        order1 = Order(self.customer, self.coffee, 3.0)
        assert len(Order.all) == 2  # Including the order from setup_method

    def test_orders_for_customer_and_coffee(self):
        '''Ensure that orders are correctly associated with customer and coffee'''
        assert self.order in self.customer.orders()
        assert self.order in self.coffee.orders()

    def test_debugging_orders(self):
        '''Ensure the orders method in Coffee class returns correct orders list'''
        assert self.coffee.orders() == [self.order]
        assert len(self.coffee.orders()) == 1
