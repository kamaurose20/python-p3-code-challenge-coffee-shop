import pytest
from classes.customer import Customer
from classes.coffee import Coffee
from classes.order import Order

class TestCustomer:
    '''Tests for Customer class in customer.py'''

    def test_has_name(self):
        '''Customer is initialized with a name'''
        customer = Customer('Steve')
        assert customer.name == "Steve"

    def test_can_change_name(self):
        '''Customer name cannot be changed after initialization'''
        customer = Customer('Steve')
        with pytest.raises(Exception, match="Name already exists and cannot be changed."):
            customer.name = "Stove"

    def test_customer_name_is_str(self):
        '''Customer name is a string'''
        customer = Customer('Steve')
        assert isinstance(customer.name, str)
        
        with pytest.raises(Exception):
            customer.name = 1
        # ------------------------

    def test_customer_name_length(self):
        '''Customer name must be between 1 and 15 characters'''
        customer = Customer('Steve')
        assert len(customer.name) == 5
        
        # Uncommented
        with pytest.raises(Exception, match="Name must be a string between 1 and 15 characters"):
            customer.name = "NameLongerThan15Characters"

        with pytest.raises(Exception, match="Name must be a string between 1 and 15 characters"):
            customer.name = ""
        # ------------------------
        
    def test_has_many_orders(self):
        '''Customer has many orders'''
        coffee = Coffee("Vanilla Latte")
        customer = Customer('Steve')
        customer_2 = Customer('Dima')
        order_1 = customer.create_order(coffee, 2)
        order_2 = customer.create_order(coffee, 5)
        order_3 = customer_2.create_order(coffee, 5)

        assert len(customer.orders()) == 2
        assert order_1 in customer.orders()
        assert order_2 in customer.orders()
        assert order_3 not in customer.orders()

    def test_orders_of_type_order(self):
        '''Customer orders are of type Order'''
        coffee = Coffee("Vanilla Latte")
        customer = Customer('Steve')
        order_1 = customer.create_order(coffee, 2)
        order_2 = customer.create_order(coffee, 5)

        assert isinstance(customer.orders()[0], Order)
        assert isinstance(customer.orders()[1], Order)

    def test_has_many_orders(self):
          '''Customer has many orders'''
    coffee = Coffee("Vanilla Latte")
    customer = Customer('Steve')
    customer_2 = Customer('Dima')
    
    # Create orders for the first customer
    order_1 = customer.create_order(coffee, 2)
    order_2 = customer.create_order(coffee, 5)
    
    # Create an order for a second customer
    order_3 = customer_2.create_order(coffee, 5)

    # Verify that the first customer has exactly 2 orders
    assert len(customer.orders()) == 2
    assert order_1 in customer.orders()
    assert order_2 in customer.orders()
    
    # Verify that the second customer does not affect the first customer's orders
    assert order_3 not in customer.orders()

    def test_has_unique_coffees(self):
        '''Customer has a unique list of all the coffees they have ordered'''
        coffee = Coffee("Vanilla Latte")
        coffee_2 = Coffee("Flat White")
        customer = Customer('Steve')
        customer.create_order(coffee, 2)
        customer.create_order(coffee, 2)
        customer.create_order(coffee_2, 5)

        assert len(set(customer.coffees())) == len(customer.coffees())
        assert len(customer.coffees()) == 2

    def test_create_order_invalid_coffee(self):
        '''Creating an order with invalid coffee raises an exception'''
        customer = Customer('Steve')
        coffee = "NotACoffeeObject"
        
        with pytest.raises(Exception, match="The coffee must be an instance of Coffee."):
            customer.create_order(coffee, 5)

    def test_create_order_invalid_price(self):
        '''Creating an order with invalid price raises an exception'''
        customer = Customer('Steve')
        coffee = Coffee("Vanilla Latte")

        with pytest.raises(Exception, match="Price must be a number between 1.0 and 10.0 inclusive."):
            customer.create_order(coffee, 0.5)

        with pytest.raises(Exception, match="Price must be a number between 1.0 and 10.0 inclusive."):
            customer.create_order(coffee, 15)

