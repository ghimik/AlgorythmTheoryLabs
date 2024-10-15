class DuplicateWordException(Exception):
    def __init__(self, word, table_name):
        message = f"Слово '{word}' уже существует в таблице '{table_name}'"
        super().__init__(message)