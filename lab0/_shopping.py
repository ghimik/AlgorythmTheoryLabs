#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_sweets_with_prices(shops):
    """Создаёт словарь с ценами на продукты из магазинов."""
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

    return sweets


def print_sweets(sweets):
    """Выводит на экран информацию о сладостях и их ценах."""
    for sweet, details in sweets.items():
        print(f"{sweet}:")
        for detail in details:
            print(f"  {detail['shop']}: {detail['price']:.2f}")


def get_user_input():
    """Получает информацию о сладостях от пользователя."""
    user_shops = {}
    while True:
        shop_name = input("Введите название магазина (или 'stop' для завершения): ")
        if shop_name.lower() == 'stop':
            break

        products = []
        while True:
            product_name = input("Введите название продукта (или 'stop' для завершения): ")
            if product_name.lower() == 'stop':
                break
            price = input(f"Введите цену для {product_name}: ")
            products.append({'name': product_name, 'price': float(price)})

        user_shops[shop_name] = products
    return user_shops


def main():
    """Основная функция для работы с магазинами и сладостями."""
    default_shops = {
        'ашан': [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
        'пятерочка': [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
        'магнит': [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
    }

    print(
        "Вы можете ввести информацию о сладостях. Если хотите, просто нажмите Enter для использования значений по умолчанию.")
    user_shops = get_user_input()

    if not user_shops:
        user_shops = default_shops

    sweets = get_sweets_with_prices(user_shops)
    print_sweets(sweets)


if __name__ == "__main__":
    main()
