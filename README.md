# Лабораторные работы по теории алгоритмов

Этот проект включает в себя несколько лабораторных, реализованных на Python.
Каждая лабораторная представлена лежит в своей папке, со своими рекуаираинтсами.

## Структура

### lab0: no name
- `_distance.py`: 1 задача, расстояния между городами
- `_circle.py`: 2 задача, точка в окружности
- `_operations.py`: 3 задача, порядок операций
- `_favorite_movies.py`: 4 задача, фильмы
- `_my_family.py`: 5 задача, моя семья
- `_zoo.py`: 6 задача, зоопарк и множества
- `_songs_list.py`: 7 задача, список песен и длина
- `_secret.py`: 8 задача, расшифровка секретного послания
- `_garden.py`: 9 задача, сады и луг
- `_shopping.py`: 10 задача, цены на сладости
- `_store.py`: 11 задача, товары на складе

## lab1: Particle Calculator

## Описание
Particle Calculator - это приложение для вычисления удельного заряда и комптоновской длины волны элементарных частиц
(электронов, протонов, нейтронов), а также кастомных частиц. Программа поддерживает модульную структуру и ООП.

## Основные функции
- Расчет удельного заряда и комптоновской длины волны для элементарных частиц.
- Создание кастомных частиц с заданными массой и зарядом.
- Сохранение результатов в форматах .docx и .xlsx.

## Основные модули и пакеты проекта
### 1. `particles`
- Этот пакет содержит классы, представляющие различные элементарные частицы, такие как **Электрон**, **Протон** и **Нейтрон**. Эти классы наследуются от абстрактного базового класса `Particle`, который предоставляет интерфейс для всех частиц.
- Использование dunder-методов (`__str__` и `__repr__`) позволяет удобно выводить и форматировать объекты.

### 2. `decorators.py`
- Модуль с декораторами, добавляющими функциональность для валидации данных и логирования вызовов методов.
- Декораторы применяются в методах классов для проверки корректности входных данных при создании пользовательской частицы.

### 3. `main.py`
- Основная программа, которая предоставляет интерфейс командной строки для взаимодействия с пользователем.
- Пользователь может выбрать одну из предустановленных частиц или создать свою, введя массу и заряд.
- Реализованы функции для сохранения результатов в форматах .docx и .xlsx с помощью библиотек **python-docx** и **openpyxl**.

## Информация о системе
- `Версия python`: **3.10.5**
- `ОС`: **Windows 11**
- `CPU`: **AMD Ryzen 5 5500U**
- `RAM`: **8GB**
