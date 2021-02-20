import random
from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    """Randomly generatle list of products

    Args:
        num_products (int, optional): [description]. Defaults to 30.
    """
    
    products = []

    for _ in range(num_products):
        name = ADJECTIVES[randint(0, 4)] + \
               ' ' + \
               NOUNS[randint(0, 4)]

        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0., 2.5)

        product = Product(name=name, 
                       price=price,
                       weight=weight,
                       flammability=flammability)
        products.append(product)
    return products

def inventory_report(products):
    """Print a summary of the list of products
    """

    product_count = len(products)
    if product_count <= 0:
        return "No products!"
  
    total_price, total_weight, total_flam = 0, 0, 0
    for prod in products:
        total_price += prod.price
        total_weight += prod.weight
        total_flam += prod.flammability
   
    avg_price = total_price / product_count
    avg_weight = total_weight / product_count
    avg_flam = total_flam / product_count
  
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print("Unique product names:", len(set(products)))
    print("Average price:", avg_price)
    print("Average weight:", avg_weight)
    print("Average flammability:", avg_flam)

if __name__ == '__main__':
    inventory_report(generate_products())