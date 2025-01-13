# Ukol, kde delam eshop s objekty
# ===============================

# vytvorim triedy Brand, Category, Product

class Brand:
    def __init__(self, name):
        self.name = name
        self.products = []
    
    def count_products(self):
        return len(self.products)
    
    def print_products(self):
        for product in self.products:
            print(product)


class Category:
    def __init__(self, name):
        self.name = name
        self.products = []
    
    def count_products(self):
        return len(self.products)
    
    def print_products(self):
        for product in self.products:
            print(product)


class Product:
    def __init__(self, name, price: int, colour, category: Category, brand: Brand,  stock=1):
        self.name = name
        self.price = price
        self.colour = colour
        
        # priradime atributy nadradenych objektov : category a brand ako atribut
        self.category = category  
        self.brand = brand
        
        # pridame atribut stock - pocet kusov - tu som chcel nieco do buducna
        self.stock = stock
        
        # pridame produkt do zoznamov produktov category a brand
        self.category.products.append(self)
        self.brand.products.append(self)
        
        # automaticky vypise, ze produkt bol vytvoreny
        print(f'Product {self.name} was created in category: {self.category.name} and brand: {self.brand.name}')

    def __str__(self):
        return f'{self.name}, price: {self.price}, colour: {self.colour}, category: {self.category.name}, brand: {self.brand.name}'
      
        
### RUN ###

# 2. Vytvor objekty Category
category_suit = Category('Suits')
category_drogery = Category('Drogery')
category_toys = Category('Toys')
category_elektro = Category('Electronics')
category_no_category = Category('No Category')

# 3. Vytvor objekty Brand
brand_adidas = Brand('Adidas')
brand_nike = Brand('Nike')
brand_sony = Brand('Sony')
brand_unknown = Brand('Unknown')

# 4. Vytvor objekty Product
product_mikna_adidas = Product('Mikina Adidas', 1000, 'black', category_suit, brand_adidas)
product_body_nike = Product('Body Nike', 200, 'white', category_suit, brand_nike)
product_lego_car = Product('Lego Car', 500, '', category_toys, brand_nike)
product_sony_headphones = Product('Sony Headphones', 1500, 'black', category_elektro, brand_sony)


### TEST ###
print(f'=====================================================================\n')
print(f'{product_mikna_adidas}\n')

print(f'Kategoria suit obsahuje: {category_suit.count_products()} produktov\n')

print('Obsah kategorie suit:')
category_suit.print_products()