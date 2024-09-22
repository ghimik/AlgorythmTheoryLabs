#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами
def show():


    shops = {
        'ашан':
            [
                {'name': 'печенье', 'price': 10.99},
                {'name': 'конфеты', 'price': 34.99},
                {'name': 'карамель', 'price': 45.99},
                {'name': 'пирожное', 'price': 67.99}
            ],
        'пятерочка':
            [
                {'name': 'печенье', 'price': 9.99},
                {'name': 'конфеты', 'price': 32.99},
                {'name': 'карамель', 'price': 46.99},
                {'name': 'пирожное', 'price': 59.99}
            ],
        'магнит':
            [
                {'name': 'печенье', 'price': 11.99},
                {'name': 'конфеты', 'price': 30.99},
                {'name': 'карамель', 'price': 41.99},
                {'name': 'пирожное', 'price': 62.99}
            ],
    }

    # Создайте словарь цен на продкты следующего вида (писать прямо в коде)
    sweets = {}

    for shop, products in shops.items():
        for product in products:
            name = product['name']
            price = product['price']

            if name not in sweets:
                sweets[name] = []

            sweets[name].append({'shop': shop, 'price': price})

    for name, prices in sweets.items():
        sorted_prices = sorted(prices, key=lambda x: x['price'])[:2]
        sweets[name] = sorted_prices


    for sweet, details in sweets.items():
        print(f"{sweet}:")
        for detail in details:
            print(f"  {detail['shop']}: {detail['price']:.2f}")
