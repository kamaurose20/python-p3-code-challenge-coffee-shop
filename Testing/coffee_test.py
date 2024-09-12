import pytest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee:
    '''Tests for Coffee class'''

    def test_initialization(self):
        '''Ensure Coffee is initialized correctly'''
        coffee = Coffee("Espresso")
        assert coffee.name == "Espresso"
        assert coffee.num_orders() == 0
        assert coffee.average_price() == 0

    def test_name_setter(self):
        '''Ensure the name is set correctly and cannot be changed'''
        coffee = Coffee("Latte")
        assert coffee.name == "Latte"
        
        # Ensure the name cannot be changed
        coffee.name = "Cappuccino"
        assert coffee.name == "Latte"  # Name should not change

    def test_add_order(self):
     '''Ensure that orders are added correctly to the coffee object'''
    coffee = Coffee("Latte")
    customer1 = Customer('Steve')
    customer2 = Customer('Dima')
    order1 = Order(customer1, coffee, 2.0)
    order2 = Order(customer2, coffee, 5.0)
    
    assert len(coffee.orders()) == 2
    assert order1 in coffee.orders()
    assert order2 in coffee.orders()

    def test_add_customer(self):
      '''Ensure that customers are added correctly to the coffee object'''
    coffee = Coffee("Latte")
    customer = Customer('Steve')
    order = Order(customer, coffee, 2.0)
    
    assert customer in coffee.customers()


    def test_orders_method(self):
     '''Ensure that the orders method returns the correct list of orders'''
    coffee = Coffee("Latte")
    customer1 = Customer('Steve')
    customer2 = Customer('Dima')
    order1 = Order(customer1, coffee, 2.0)
    order2 = Order(customer2, coffee, 5.0)
    order3 = Order(customer1, coffee, 3.0)
    order4 = Order(customer2, coffee, 4.0)
    
    assert len(coffee.orders()) == 4
    assert order1 in coffee.orders()
    assert order2 in coffee.orders()
    assert order3 in coffee.orders()
    assert order4 in coffee.orders()

    def test_customers_method(self):
        '''Ensure customers method returns unique customers'''
        coffee = Coffee("Cappuccino")
        customer1 = Customer("Dave")
        customer2 = Customer("Jane")
        order1 = Order(customer1, coffee, 3.0)
        order2 = Order(customer2, coffee, 4.0)
        order3 = Order(customer1, coffee, 2.5)  # Same customer

        coffee.add_order(order1)
        coffee.add_order(order2)
        coffee.add_order(order3)
        
        customers = coffee.customers()
        assert len(customers) == 2
        assert customer1 in customers
        assert customer2 in customers

    def test_num_orders(self):
      '''Ensure that num_orders method returns the correct number of orders'''
    coffee = Coffee("Latte")
    customer1 = Customer('Steve')
    customer2 = Customer('Dima')
    Order(customer1, coffee, 2.0)
    Order(customer2, coffee, 5.0)
    Order(customer1, coffee, 3.0)
    Order(customer2, coffee, 4.0)
    
    assert coffee.num_orders() == 4


    def test_average_price(self):
        '''Ensure average_price returns the correct average'''
        coffee = Coffee("Latte")
        customer = Customer("Grace")
        order1 = Order(customer, coffee, 2.0)
        order2 = Order(customer, coffee, 3.0)
        order3 = Order(customer, coffee, 4.0)
        
        coffee.add_order(order1)
        coffee.add_order(order2)
        coffee.add_order(order3)
        
        assert coffee.average_price() == 3.0

    def test_average_price_no_orders(self):
        '''Ensure average_price returns 0 if no orders exist'''
        coffee = Coffee("Black Coffee")
        assert coffee.average_price() == 0
