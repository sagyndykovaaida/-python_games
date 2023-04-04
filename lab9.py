def calculate_delivery_cost(street_name, price):
    delivery_cost = 0
    if street_name in ['Al-Farabi', 'Sain', 'Tashkent', 'Dostyk']:
        if price < 10000:
            delivery_cost = 500
    else:
        if price < 10000:
            delivery_cost = 1000
    return delivery_cost

street_name = input(" street name: ")
price = float(input("price: "))

total_delivery_cost = calculate_delivery_cost(street_name, price)

if total_delivery_cost == 0:
    print("Delivery is free.")
else:
    print(f"The total delivery cost for {street_name} and goods worth {price}tg is {total_delivery_cost}tg.")


