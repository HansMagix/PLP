def calculate_discount(price, discount_percent):
    return (price*discount_percent)/100 if discount_percent >= 20 else price

print(calculate_discount(90, 30))
print(calculate_discount(50, 10))