import unittest

class TestShoppingCart(unittest.TestCase):
    def setUp(self) -> None:
        self.cart = ShoppingCart()

        #creating products for test case
        self.product0 = Product("Phone", 1000)
        self.product1 = Product("Computer", 2000)



    def test_AddItem(self): #how many itesm is being aded to the shopping cart
        self.cart.AddItem(self.product0, 2)
        self.assertEqual(len(self.cart.items), 1)
    

    def test_removeItem(self): # to remove an item
        self.cart.AddItem(self.product0, 5)
        self.cart.RemoveItem(self.product0, 2)
        self.assertEqual(self.cart.items[0]['quantity'], 3) # item inside inside in the shoppping caart would keep the quanitity 


    def test_CalculateTotal(self):
        self.cart.AddItem(self.product0,2)
        self.cart.AddItem(self.product1,5)
        total = self.cart.CalculateTotal()
        self.assertEqual(total, 12000)  # that is 1000 * 2, 2000 * 5 = 12000

    
# test 2
class ShoppingCart:
    def __init__(self):
        self.items = []
        pass

    def AddItem(self, product, quantity = 1):
        self.items.append({'product' : product, 'quantity': quantity}) #adding items to the list


    def RemoveItem(self, product, quantity = 1):
        for item in self.items:
            if item['product'] == product:
                item['quamtity'] -= quantity
                if item['quantity'] <= 0:
                    self.items.remove(item)

    def CalculateTotal(self):
        total = sum(item['product'].price * item['quantity'] for items in self.items)
        return total


class Product:
     def __init__(self, name, price):
         pass







if __name__ == "__main__":
    unittest.main()







