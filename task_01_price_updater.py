# Exercise: Updating product prices using Dictionary Items
# Goal: Apply a 20% discount and update the original dictionary

products = {
    "Laptop": 990,
    "Smartphone": 600,
    "Tablet": 250,
    "Headphones": 70
}

for product, price in products.items():
    # Calculation (Reading the value)
    discounted_price = price * 0.8
    # Update (Writing using the Key)
    products[product] = discounted_price
    print(f"New price for {product}: ${discounted_price:.2f}")

print("\nFinal Updated Inventory:", products)