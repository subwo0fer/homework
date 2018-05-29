from datetime import datetime
from pony.orm import *

db = Database()



class Product(db.Entity):
    """Товар"""
    category = Required('Category')
    title = Required(str)
    unit = Required(str)
    price = Required(float)
    description = Optional(str)
    #alt_categories = Set('Category')
    #amount = int # сколько товаров в магазине сейчас
    history = Set('ProductHistory')
    cartitem = Optional('CartItem')
    orderitem = Optional('OrderItem')

class ProductHistory(db.Entity):
    product = Required('Product')
    created = Optional(datetime, default=datetime.now)
    price = Required(float)
	
class Category(db.Entity):
    """Категория"""
    parent = Optional('Category', reverse='parent')
    title = Required(str)
    products = Set(Product)

class Customer(db.Entity):
    """Покупатель"""
    email = Optional(str)
    phone = Optional(str)
    name = Required(str)
    address = Optional('Address')
    cart = Optional('Cart')
    order = Optional('Order')

class Address(db.Entity):
    """адрес"""
    customer = Required('Customer')
    country = Required(str)
    city = Required(str)
    street = Required(str)
    zip_code = Required(str)
    house = Required(int)


class Cart(db.Entity):
    """Коризна с товарами"""
    customer = Optional('Customer') # or None
    products = Set('CartItem')

class CartItem(db.Entity):
    """Элемент корзины"""
    cart = Required('Cart')
    product = Required('Product')
    amount = int # 1 единица товара

class Order(db.Entity):
    """Заказ"""
    customer = Required('Customer')
    created = Required(datetime)
    products = Set('OrderItem')
    status = Required('Status')
    cost = float

class Status(db.Entity):
    """Статус"""
    name = str
    order = Optional('Order')

class OrderItem(db.Entity):
    """Товар (одна позиция) в заказе"""
    order = Required('Order')
    product = Required('Product')
    amount = int #1 единица товара


class Menu(db.Entity):
    """Меню"""

set_sql_debug(True)

db.bind(provider='sqlite', filename='database.sqlite', create_db=True)

db.generate_mapping(create_tables=True)

with db_session:
	category_cpu = Category(title="CPU's")
	category_video_carts = Category(title="Video carts")
	category_ram = Category(title="RAM")
	
	intel_4770k = Product(category=category_cpu,
						  title='Intel Core i5 4770k',
						  unit='1', price=12228)
	amd_ryzen_6 = Product(category=category_cpu,
						  title='AMD Ryzen 6',
						  unit='1', price=9228)
	gtx_760 = Product(category=category_video_carts,
					  title='GeForce GTX 760',
					  unit='1', price=8000)
	amd_ddr3_2gb = Product(category=category_ram,
						  title='AMD DDR3 2gb',
						  unit='1', price=2000)					  
