import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS

class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
    
    def test_default_product_weight(self):
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)
    
    def test_product_flammability(self):
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)
    
    def test_product_methods(self):
        prod = Product('Test Product', weight=100, price=30, flammability=2)
        self.assertEqual(prod.stealability(), 'Very stealable!')
        self.assertEqual(prod.explode(), '...BABOOM!!')

class AcmeReportTests(unittest.TestCase):

    def test_default_num_products(self):
        products = generate_products()
        self.assertEqual(len(products), 30)
    
    def test_legal_names(self):
        products = generate_products()
        for prod in products:
            names = prod.name.split()
            self.assertTrue(names[0] in ADJECTIVES)
            self.assertTrue(names[1] in NOUNS)

if __name__ == '__main__':
    unittest.main()