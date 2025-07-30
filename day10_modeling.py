import pandas as pd

# Fact Table
sales = pd.DataFrame({
    'sale_id': [1, 2, 3],
    'customer_id': [1, 2, 1],
    'product_id': [1, 2, 2],
    'date': ['2023-01-01', '2023-01-03', '2023-01-05'],
    'amount': [10.0, 100.0, 100.0]
})

# Dimension: Customers
customers = pd.DataFrame({
    'customer_id': [1, 2],
    'name': ['Alice', 'Bob'],
    'address': ['Hyderabad', 'Delhi']
})

# Dimension: Products
products = pd.DataFrame({
    'product_id': [1, 2],
    'product_name': ['Pen', 'Mug'],
    'category': ['Stationery', 'Kitchen'],
    'price': [10.0, 100.0]
})

# Join facts with dimensions:
sales_with_details = sales.merge(customers, on='customer_id', how='left').merge(products, on='product_id', how='left')

print(sales_with_details)
