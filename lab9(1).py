def calculate_delivery_cost(street_name, goods_price):
    delivery_cost = 0
    if street_name in ['Al-Farabi', 'Sain', 'Tashkent', 'Dostyk']:
        if goods_price < 10000:
            delivery_cost = 500
    else:
        if goods_price < 10000:
            delivery_cost = 1000
    return delivery_cost


