class WordsNotFoundException(Exception):
    def __init__(self, table_name):
        message = f"Слова не найдены в таблице '{table_name}'"
        super().__init__(message)