import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer:
    '''Tests for Customer class'''

    def test_initialization(self):
        '''Ensure Customer is initialized correctly'''
        customer = Customer('Steve')
        assert customer.name == 'Steve'
        assert customer.num_orders() == 0
        assert customer.average_price() == 0

    def test_name_setter(self):
        '''Customer name cannot be changed after initialization'''
        customer = Customer('Steve')
        with pytest.raises(Exception, match="Name already exists and cannot be changed."):
            customer.name = "Stove"

    def test_add_coffee(self):
        '''Ensure that coffees are added correctly to the customer object'''
        coffee = Coffee("Latte")
        customer = Customer('Steve')
        customer.create_order(coffee, 2.0)
        assert coffee in customer.coffees()

    def test_add_coffee_unique(self):
        '''Ensure coffees can be added to customer and are unique'''
        coffee = Coffee("Espresso")
        customer = Customer('Steve')
        
        customer.add_coffee(coffee)
        assert coffee in customer.coffees()

        # Adding the same coffee again should not duplicate
        customer.add_coffee(coffee)
        assert len(customer.coffees()) == 1

    def test_orders_method(self):
        '''Ensure orders method returns all orders'''
        coffee = Coffee("Cappuccino")
        customer = Customer('Steve')
        order1 = customer.create_order(coffee, 3.0)
        order2 = customer.create_order(coffee, 5.0)
        
        orders = customer.orders()
        assert len(orders) == 2
        assert order1 in orders
        assert order2 in orders

    def test_coffees_method(self):
        '''Ensure coffees method returns unique coffees'''
        coffee1 = Coffee("Americano")
        coffee2 = Coffee("Mocha")
        customer = Customer('Steve')
        customer.create_order(coffee1, 3.5)
        customer.create_order(coffee1, 2.5)
        customer.create_order(coffee2, 4.0)
        
        coffees = customer.coffees()
        assert len(coffees) == 2
        assert coffee1 in coffees
        assert coffee2 in coffees

    def test_create_order_invalid_coffee(self):
        '''Creating an order with invalid coffee raises an exception'''
        customer = Customer('Steve')
        invalid_coffee = "NotACoffeeObject"
        
        with pytest.raises(Exception, match="The coffee must be an instance of Coffee."):
            customer.create_order(invalid_coffee, 5.0)

    def test_create_order_invalid_price(self):
        '''Creating an order with invalid price raises an exception'''
        customer = Customer('Steve')
        coffee = Coffee("Latte")

        with pytest.raises(Exception, match="Price must be a number between 1.0 and 10.0 inclusive."):
            customer.create_order(coffee, 0.5)

        with pytest.raises(Exception, match="Price must be a number between 1.0 and 10.0 inclusive."):
            customer.create_order(coffee, 15)

    def test_num_orders(self):
        '''Ensure num_orders returns the correct count'''
        coffee = Coffee("Mocha")
        customer = Customer('Steve')
        customer.create_order(coffee, 3.0)
        customer.create_order(coffee, 4.0)
        
        assert customer.num_orders() == 2

    def test_average_price(self):
        '''Ensure average_price returns the correct average'''
        coffee = Coffee("Latte")
        customer = Customer('Steve')
        customer.create_order(coffee, 2.0)
        customer.create_order(coffee, 4.0)
        customer.create_order(coffee, 6.0)
        
        assert customer.average_price() == 4.0

    def test_average_price_no_orders(self):
        '''Ensure average_price returns 0 if no orders exist'''
        customer = Customer('Steve')
        assert customer.average_price() == 0
