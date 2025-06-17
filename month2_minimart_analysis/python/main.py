# Entry point for the MiniMart data reporting system
# Sample products data as nested dictionary
products = {
    1: {"name": "Wireless Mouse", "price": 25.99},
    2: {"name": "Bluetooth Speaker", "price": 45.50},
    3: {"name": "Coffee Mug", "price": 12.00},
    4: {"name": "Yoga Mat", "price": 35.75},
    5: {"name": "Desk Lamp", "price": 28.40},
}

# Sample orders simulated as list of dictionaries
orders = [
    {"customer_id": 1, "product_id": 1, "quantity": 2},
    {"customer_id": 2, "product_id": 3, "quantity": 5},
    {"customer_id": 1, "product_id": 4, "quantity": 1},
    {"customer_id": 3, "product_id": 2, "quantity": 3},
    {"customer_id": 2, "product_id": 5, "quantity": 4},
]

# Use conditionals to flag large orders (e.g., total > $100)
for order in orders:
    product = products[order["product_id"]]
    total = product["price"] * order["quantity"]
    if total > 100:
        order["large_order"] = True
        print(total)
    else:
        order["large_order"] = False

# Convert product prices to another currency and apply conditional discounts
# Assuming initial price is in USD
usd_to_eur = 0.9

for order in orders:
    product = products[order["product_id"]]
    price_eur = product["price"] * usd_to_eur
    total_eur = price_eur * order["quantity"]

    # Apply 10% discount if total > 100 EUR
    if total_eur > 100:
        total_eur *= 0.9  # 10% discount

    order["total_eur"] = total_eur

print(products[1]['price'])

# ---------------------------------

"""Generate a dictionary report including:
Total products sold
Most popular product
Revenue per customer """

report = {
    "total_products_sold": 0,
    "popular_sales": {},  # changed from product_sales
    "revenue_per_customer": {}
}

for order in orders:
    qty = order["quantity"]
    product_id = order["product_id"]
    customer_id = order["customer_id"]
    price = products[product_id]["price"]

    # Update total products
    report["total_products_sold"] += qty

    # Update popular sales
    if product_id in report["popular_sales"]:
        report["popular_sales"][product_id] += qty
    else:
        report["popular_sales"][product_id] = qty

    # Update revenue per customer
    total = qty * price
    if customer_id in report["revenue_per_customer"]:
        report["revenue_per_customer"][customer_id] += total
    else:
        report["revenue_per_customer"][customer_id] = total

# Determine most popular product
most_popular = max(report["popular_sales"], key=report["popular_sales"].get)

print("Total products sold :", report["total_products_sold"])

print("Most popular product :", products[most_popular]["name"])

print("Revenue per customer :", report["revenue_per_customer"])
