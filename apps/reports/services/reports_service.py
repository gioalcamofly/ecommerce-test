from collections import Counter
from django.db.models import F, Sum, QuerySet
from django_mysql.models import GroupConcat
from types import FunctionType

import pandas as pd
from pandas.core.series import Series
from pandas.core.indexes.base import Index

from ..models import Customer, Product, Order, OrderProduct

def _get_uploader(key: str) -> FunctionType:
    if key == 'customers':
        return _upload_customer
    elif key == 'products':
        return _upload_product
    elif key == 'orders':
        return _upload_order
    else:
        raise ValueError(key)
    
# TODO: Validate file columns
def upload_data(data: dict) -> None:
    
    for key, file in data.items():
        uploader = _get_uploader(key)
        dataframe = pd.read_csv(file)
        # Using apply() to execute a function for every row but header. Using dataframe.columns to get position of each column
        # so data is parsed correctly
        dataframe.apply(
            lambda row: uploader(row, dataframe.columns),
            axis=1
        )


def order_prices() -> QuerySet:
    order_prices = OrderProduct.objects \
        .annotate(partial_price=F('product__cost') * F('quantity')) \
        .values('order_id') \
        .annotate(total_price=Sum(F('partial_price'))) \
        .values('order_id', 'total_price') \
        .order_by('order_id')
        
    return order_prices

def product_customers() -> QuerySet:
    product_customers = OrderProduct.objects \
        .annotate(customer_id=F('id')) \
        .values('product_id') \
        .annotate(customer_ids=GroupConcat(F('customer_id'))) \
        .values('product_id', 'customer_ids') \
        .order_by('product_id')
        
    return product_customers

def customer_ranking() -> QuerySet:
    customer_ranking = OrderProduct.objects \
        .annotate(partial_price=F('product__cost') * F('quantity')) \
        .values('order__customer__id') \
        .annotate(total_price=Sum(F('partial_price')), 
                  customer_id=F('order__customer__id'), 
                  customer_name=F('order__customer__firstname'),
                  customer_lastname=F('order__customer__lastname')) \
        .values('customer_id', 'customer_name', 'customer_lastname', 'total_price') \
        .order_by('-total_price')
        
    return customer_ranking

def _upload_customer(data: Series, columns: Index) -> None:
    Customer.objects.get_or_create(
        id=data[columns.get_loc('id')],
        firstname=data[columns.get_loc('firstname')],
        lastname=data[columns.get_loc('lastname')]
    )
    
# TODO: solve problem with get_or_create -> giving duplicate entry integration error
def _upload_product(data: Series, columns: Index) -> None:
    try:
        product = Product.objects.get(id = columns.get_loc('id'))
    except Product.DoesNotExist:
        product = Product(
            id=data[columns.get_loc('id')],
            name=data[columns.get_loc('name')],
            cost=data[columns.get_loc('cost')]        
        )
        product.save()

def _upload_order(data: Series, columns: Index) -> None:
    order, _ = Order.objects.get_or_create(
        id=data[columns.get_loc('id')],
        customer_id=data[columns.get_loc('customer')])
    
    product_ids = data[columns.get_loc('products')].split(' ')
    for product, quantity in Counter(product_ids).items(): # Transform array into dict with keys as array items and values as repetitions
        OrderProduct.objects.get_or_create(
            order=order,
            product=Product.objects.get(id = product),
            quantity=quantity)
    