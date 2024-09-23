#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calculate_expression():
    expression1 = (1 + 2) * 3 + 4 + 5
    expression2 = 1 * (2 + 3) * 4 + 5
    expression3 = 1 * 2 * 3 + 4 * 5

    print(f"Результат выражения (1 + 2) * 3 + 4 + 5 = {expression1}. Облом!")
    print(f"Результат выражения 1 * 2 * 3 + 4 * 5 = {expression3}. Снова облом!")
    print(f"Результат выражения 1 * (2 + 3) * 4 + 5 = {expression2}. Ура!!")


if __name__ == "__main__":
    calculate_expression()
