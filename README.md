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

### lab1: Particle Calculator

#### Описание
Particle Calculator - это приложение для вычисления удельного заряда и комптоновской длины волны элементарных частиц
(электронов, протонов, нейтронов), а также кастомных частиц. Программа поддерживает модульную структуру и ООП.

#### Основные функции
- Расчет удельного заряда и комптоновской длины волны для элементарных частиц.
- Создание кастомных частиц с заданными массой и зарядом.
- Сохранение результатов в форматах .docx и .xlsx.

#### Основные модули и пакеты проекта
###### 1. `particles`
- Этот пакет содержит классы, представляющие различные элементарные частицы, такие как **Электрон**, **Протон** и **Нейтрон**. Эти классы наследуются от абстрактного базового класса `Particle`, который предоставляет интерфейс для всех частиц.
- Использование dunder-методов (`__str__` и `__repr__`) позволяет удобно выводить и форматировать объекты.

###### 2. `decorators.py`
- Модуль с декораторами, добавляющими функциональность для валидации данных и логирования вызовов методов.
- Декораторы применяются в методах классов для проверки корректности входных данных при создании пользовательской частицы.

###### 3. `main.py`
- Основная программа, которая предоставляет интерфейс командной строки для взаимодействия с пользователем.
- Пользователь может выбрать одну из предустановленных частиц или создать свою, введя массу и заряд.
- Реализованы функции для сохранения результатов в форматах .docx и .xlsx с помощью библиотек **python-docx** и **openpyxl**.

#### Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ghimik/AlgorythmTheoryLabs.git
   cd ./AlgorythmTheoryLabs/lab1
   ```
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Запуск
   ```bash
   python main.py
   ```
#### Тестирование
- Покрытие кода тестами реализовано с помощью **pytest**. Тесты находятся в папке `tests` и покрывают основные модули,
- включая расчеты и корректность обработки пользовательских частиц.
- Для запуска тестов:
    Запускайте через ИДЕ;)

### lab3: Quote Generator

## Описание
Проект представляет собой гениальный генератор случайных цитат, в котором собраны три различных типа высказываний: пацанские цитаты, романтические и философские. 
В основе системы лежит тщательно продуманная архитектура, которая позволяет получать случайные слова из базы данных и использовать их для создания фраз в стиле "философы в пятницу вечером". 

_ну или на созвоне угарать с пацанами_


![Мемный волк](lab2/server/resources/static/volk.png)

## Архитектура
### Паттерны
Проект использует несколько ключевых паттернов проектирования:

1. **Шаблонный метод (Template Method)**: Этот паттерн явно отображается в классе `WordsProvider` и его потомках. Базовый класс определяет общий алгоритм, а конкретные реализации (`PgDbWordsProvider`, `InMemoryWordsProvider`) реализуют специфические шаги, такие как получение слов и добавление новых данных.

2. **Абстрактная фабрика (Abstract Factory)**: В проекте используются фабрики для генерации различных типов шаблонов (цитат), например, `GangstaTemplateFactory`, `RomanticTemplateFactory`, `PhilosophicalTemplateFactory`. Это классический пример применения абстрактной фабрики, где каждая конкретная фабрика создает объекты (шаблоны) одной "семьи" — цитаты определенного стиля.

3. **Адаптер (Adapter)**: Класс `PgDbWordsProvider` может быть квалифицирован как адаптер. Он адаптирует базовый интерфейс `WordsProvider` под конкретную реализацию работы с базой данных через PostgreSQL, превращая запросы SQL в объекты `Noun`, `Verb`, и `Adjective`.

4. **Стратегия (Strategy)**: В проекте есть разные шаблоны для генерации цитат (пацанские, романтические, философские). Каждый из этих шаблонов реализует свой подход к построению фраз на основе предоставленных слов. Можно рассматривать это как применение паттерна "Стратегия", где стратегия — это конкретная реализация генерации цитаты, а система выбирает, какую стратегию применить в зависимости от выбранного стиля цитаты.

5. **Фабричный метод (Factory Method)**: Паттерн проявляется в реализации классов шаблонов, где, например, в классе `TemplateFactory` определен метод `create_template()`, а конкретные фабрики (такие как `GangstaTemplateFactory` и другие) реализуют этот метод для создания конкретных шаблонов цитат.

### Модули
- **data** — модуль для работы с данными. В нем реализованы адаптеры для взаимодействия с базой данных PostgreSQL (`PgDbWordsProvider`) и для хранения данных в памяти (`InMemoryWordsProvider`).
- **words** — содержит классы слов (Noun, Verb, Adjective) и работу с наборами слов (`WordSet`), которые используются для создания случайных фраз.
- **server** - содержит в себе серверную логику и статические ресурсы и html-template.
### База данных
- Два SQL-скрипта для создания и заполнения базы данных расположены в папке `db`. Они содержат таблицы для хранения существительных, глаголов и прилагательных.
- Настройка подключения (порт, адрес, имя пользователя и пароль) находятся в сервере - только там она и используется.
### Сервер
Проект использует **FastAPI** для реализации API, которое позволяет генерировать цитаты и добавлять новые слова в базу данных. Запуск сервера осуществляется с помощью **uvicorn**.

### Статические файлы
- Картинка "мемный волк" — символ абсурдности цитат.
- Звук: песня "Безумно можно быть первым" (всеми известная мемная композиция).

## API
### GET /gangsta
Возвращает случайную пацанскую цитату.

### GET /romantic
Возвращает случайную романтическую цитату.

### GET /philosophical
Возвращает случайную философскую цитату (погружаемся в бездну смысла).

### POST /add/noun
Добавляет новое существительное в базу.

### POST /add/verb
Добавляет новый глагол в базу.

### POST /add/adjective
Добавляет новое прилагательное в базу.

## Пример использования
1. Зайдите на главную страницу и выберите тип цитаты (пацанская, романтическая или философская).
2. Если хотите добавить свое слово в базу, используйте соответствующие кнопки для существительных, глаголов или прилагательных.
3. Получайте удовольствие.

## Как запускать
### Установите необходимые зависимости:
 - `pip install -r requirements.txt`
### Создайте контейнер с БД:
 - `docker run --name cytaty -p 5430:5432 -e POSTGRES_PASSWORD=admin -d postgres:13.3`
 -  Подключитесь к базе данных через pgAdmin,
 - создайте бд 'cytaty' и импортируйте миграции из директории db.
### Запуск сервера
 -  Для запуска сервера выполните следующую команду:
    `uvicorn server.server:app --host 0.0.0.0 --port 8001`

## Пример цитат
**Пацанская цитата**: "В жизни, как и на районе, рубль всегда найдёт жизнь."  
**Философская цитата**: "Истина заключается в том, что мы должны играть в доту.
**Романтическая цитата**: "Каждый момент с тобой — это машина тьюринга, которое я храню в сердце." 
## Заключение
Этот генератор — не просто инструмент для получения случайных цитат, это способ превратить любую скучную встречу в бесконечный поток смешных (или странных) высказываний. Наслаждайтесь созданием "мудрых" фраз и не забудьте добавить свои слова, чтобы ваш угар был по-настоящему уникальным!

## Информация о системе
- `Версия python`: **3.10.5**
- `ОС`: **Windows 11**
- `CPU`: **AMD Ryzen 5 5500U**
- `RAM`: **8GB**

