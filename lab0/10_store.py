#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

table_code = goods['Стол']
tables_quantity = store[table_code][0]['quantity'] + store[table_code][1]['quantity']
tables_price_1 = store[table_code][0]['price']
tables_price_2 = store[table_code][1]['price']
tables_cost = (store[table_code][0]['quantity'] * tables_price_1 +
               store[table_code][1]['quantity'] * tables_price_2)
print(f'Стол - {tables_quantity} шт, стоимость {tables_cost} руб')

sofa_code = goods['Диван']
sofas_quantity = store[sofa_code][0]['quantity'] + store[sofa_code][1]['quantity']
sofas_price_1 = store[sofa_code][0]['price']
sofas_price_2 = store[sofa_code][1]['price']
sofas_cost = (store[sofa_code][0]['quantity'] * sofas_price_1 +
              store[sofa_code][1]['quantity'] * sofas_price_2)
print(f'Диван - {sofas_quantity} шт, стоимость {sofas_cost} руб')

chair_code = goods['Стул']
chairs_quantity = store[chair_code][0]['quantity'] + store[chair_code][1]['quantity'] + store[chair_code][2]['quantity']
chairs_price_1 = store[chair_code][0]['price']
chairs_price_2 = store[chair_code][1]['price']
chairs_price_3 = store[chair_code][2]['price']
chairs_cost = (store[chair_code][0]['quantity'] * chairs_price_1 +
               store[chair_code][1]['quantity'] * chairs_price_2 +
               store[chair_code][2]['quantity'] * chairs_price_3)
print(f'Стул - {chairs_quantity} шт, стоимость {chairs_cost} руб')
