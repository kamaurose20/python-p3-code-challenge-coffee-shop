import pytest
from classes.coffee import Coffee
from classes.customer import Customer
from classes.order import Order

class TestOrder:
    '''Tests for Order class in order.py'''

    def test_has_price(self):
        '''Order is initialized with a price'''
        coffee = Coffee("Mocha")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer, coffee, 5)

        assert order_1.price == 2
        assert order_2.price == 5

    def test_has_price_number(self):
        '''Price is a number and must be set within the valid range'''
        coffee = Coffee("Mocha")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2)
        
        with pytest.raises(Exception, match="Price must be a number between 1.0 and 10.0 inclusive."):
            order_1.price = "Peppermint Mocha"

    def test_price_cannot_be_changed(self):
        '''Price cannot be changed once set'''
        coffee = Coffee("Mocha")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2)
        
        with pytest.raises(Exception, match="Price cannot be changed once set."):
            order_1.price = 5

    def test_has_a_customer(self):
        '''Order has a customer'''
        coffee = Coffee("Mocha")
        customer_1 = Customer('Wayne')
        customer_2 = Customer('Dima')
        order_1 = Order(customer_1, coffee, 2)
        order_2 = Order(customer_2, coffee, 5)

        assert order_1.customer == customer_1
        assert order_2.customer == customer_2

    def test_customer_of_type_customer(self):
        '''Customer associated with the order is of type Customer'''
        coffee = Coffee("Vanilla Latte")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2)

        assert isinstance(order_1.customer, Customer)

    def test_has_a_coffee(self):
        '''Order has a coffee'''
        coffee_1 = Coffee("Mocha")
        coffee_2 = Coffee("Peppermint Mocha")
        customer = Customer('Wayne')
        order_1 = Order(customer, coffee_1, 2)
        order_2 = Order(customer, coffee_2, 5)

        assert order_1.coffee == coffee_1
        assert order_2.coffee == coffee_2

    def test_coffee_of_type_coffee(self):
        '''Coffee associated with the order is of type Coffee'''
        coffee = Coffee("Vanilla Latte")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2)

        assert isinstance(order_1.coffee, Coffee)

    def test_get_all_orders(self):
        '''Test Order class all attribute'''
        Order.all = []
        coffee = Coffee("Mocha")
        customer = Customer('Wayne')
        customer_2 = Customer('Dima')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer_2, coffee, 5)

        assert len(Order.all) == 2
        assert order_1 in Order.all
        assert order_2 in Order.all

