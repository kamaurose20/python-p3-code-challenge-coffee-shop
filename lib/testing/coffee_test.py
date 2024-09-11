import pytest
from classes.coffee import Coffee
from classes.customer import Customer
from classes.order import Order

class TestCoffee:
    '''Test suite for Coffee class in coffee.py'''

    def test_has_name(self):
        '''Coffee is initialized with a name'''
        coffee = Coffee("Mocha")
        assert coffee.name == "Mocha"

    def test_name_is_string(self):
        '''Coffee name is of type str'''
        coffee = Coffee("Mocha")
        assert isinstance(coffee.name, str)

    def test_name_setter(self):
        '''Cannot change the name of the coffee after initialization'''
        coffee = Coffee("Mocha")
        # Try changing name after initialization.
        with pytest.raises(AttributeError):
            coffee.name = "Peppermint Mocha"

    def test_has_many_orders(self):
        '''Coffee has many orders'''
        coffee = Coffee("Hazelnut Latte")
        coffee_2 = Coffee("Mocha")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer, coffee, 5)
        order_3 = Order(customer, coffee_2, 5)  

        assert len(coffee.orders()) == 2
        assert order_1 in coffee.orders()
        assert order_2 in coffee.orders()
        assert order_3 not in coffee.orders()

    def test_orders_of_type_order(self):
        '''Orders associated with coffee are of type Order'''
        coffee = Coffee("Vanilla Latte")
        customer = Customer("Steve")
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer, coffee, 5)

        assert isinstance(coffee.orders()[0], Order)
        assert isinstance(coffee.orders()[1], Order)

    def test_has_many_customers(self):
        '''Coffee has many customers'''
        coffee = Coffee("Flat White")
        customer = Customer("Steve")
        customer_2 = Customer("Dima")
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer_2, coffee, 5)

        assert customer in coffee.customers()
        assert customer_2 in coffee.customers()

    def test_has_unique_customers(self):
        '''Coffee has unique list of customers that ordered it'''
        coffee = Coffee("Vanilla Latte")
        customer = Customer("Steve")
        customer_2 = Customer("Dima")
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer_2, coffee, 2)
        order_3 = Order(customer, coffee, 5)  # Same customer ordering again

        assert len(set(coffee.customers())) == len(coffee.customers())
        assert len(coffee.customers()) == 2  # Should still be 2 unique customers

    def test_customers_of_type_customer(self):
        '''Customers of coffee are of type Customer'''
        coffee = Coffee("Vanilla Latte")
        customer = Customer("Steve")
        customer_2 = Customer("Dima")
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer_2, coffee, 5)

        assert isinstance(coffee.customers()[0], Customer)
        assert isinstance(coffee.customers()[1], Customer)

    def test_get_number_of_orders(self):
        '''Test num_orders method'''
        coffee = Coffee("Mocha")
        customer = Customer("Steve")
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer, coffee, 5)

        assert coffee.num_orders() == 2

    def test_average_price(self):
        '''Test average_price method'''
        coffee = Coffee("Mocha")
        customer = Customer("Steve")
        customer_2 = Customer("Dima")
        Order(customer, coffee, 2)
        Order(customer_2, coffee, 5)

        assert coffee.average_price() == 3.5  # Average of 2 and 5 is 3.5
