#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:
def show():

    # моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
    my_family = ['Mother', 'Father', 'Sister']


    # список списков приблизителного роста членов вашей семьи
    my_family_height = [
        # ['имя', рост],
        ['Mother', 165],
        ['Father', 171],
        ['Sister', 173]
    ]

    # Выведите на консоль рост отца в формате
    #   Рост отца - ХХ см
    print(f'Рост отца - {my_family_height[0][1]} см')


    # Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
    #   Общий рост моей семьи - ХХ см
    total_height = sum([member[1] for member in my_family_height])
    print(f'Общий рост моей семьи - {total_height} см')

