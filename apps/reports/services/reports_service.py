from re import M
import pandas as pd

from ..models import Customer, Product, Order


    

def _get_uploader(key):
    if key == 'customers':
        return _upload_customer
    elif key == 'products':
        return _upload_product
    elif key == 'orders':
        return _upload_order
    else:
        raise ValueError(key)
    
# TODO: Validate file columns
def upload_data(data):
    
    for key, file in data.items():
        uploader = _get_uploader(key)
        dataframe = pd.read_csv(file)
        # Using apply() to execute a function for every row but header. Using dataframe.columns to get position of each column
        # so data is parsed correctly
        dataframe.apply(
            lambda row: uploader(row, dataframe.columns),
            axis=1
        )
            
    return

def order_prices():
    return []

def product_customers():
    return []

def customer_ranking():
    return []

def _upload_customer(data, columns):
    Customer.objects.get_or_create(
        id=data[columns.get_loc('id')],
        firstname=data[columns.get_loc('firstname')],
        lastname=data[columns.get_loc('lastname')]
    )
    
# TODO: solve problem with get_or_create -> giving duplicate entry integration error
def _upload_product(data, columns):
    try:
        product = Product.objects.get(id = columns.get_loc('id'))
    except Product.DoesNotExist:
        product = Product(
            id=data[columns.get_loc('id')],
            name=data[columns.get_loc('name')],
            cost=data[columns.get_loc('cost')]        
        )
        product.save()

def _upload_order(data, columns):
    order, _ = Order.objects.get_or_create(
        id=data[columns.get_loc('id')],
        customer_id=data[columns.get_loc('customer')]
    )
    
    for product in data[columns.get_loc('products')].split(' '):
        order.products.add(
            Product.objects.get(id = product)
        )
    