import psycopg2
from psycopg2 import sql

from lab2.data.WordsProvider import WordsProvider
from lab2.phase.Adjective import Adjective
from lab2.phase.Noun import Noun
from lab2.phase.Verb import Verb


def _create_word_instance(table_name, word):
    if table_name == 'noun':
        return Noun(word)
    elif table_name == 'verb':
        return Verb(word)
    elif table_name == 'adjective':
        return Adjective(word)
    else:
        raise ValueError(f"Неизвестная таблица: {table_name}")


class PgDbWordsProvider(WordsProvider):
    def __init__(self, host, port, dbname, user, password):
        self.connection_params = {
            'host': host,
            'port': port,
            'dbname': dbname,
            'user': user,
            'password': password
        }

    def _get_words(self, table_name):
        try:
            with psycopg2.connect(**self.connection_params) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(sql.SQL("SELECT word FROM {}").format(sql.Identifier(table_name)))
                    words = cursor.fetchall()
                    f_words = [_create_word_instance(table_name, word[0]) for word in words]
                    return f_words
        except Exception as e:
            print(f"Ошибка при получении слов из таблицы {table_name}: {e}")
            return []

    def _add_word(self, table_name, word):
        try:
            with psycopg2.connect(**self.connection_params) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        sql.SQL("INSERT INTO {} (word) VALUES (%s)").format(sql.Identifier(table_name)),
                        [word]
                    )
                    conn.commit()
        except Exception as e:
            print(f"Ошибка при добавлении слова в таблицу {table_name}: {e}")

    def get_nouns(self):
        return self._get_words('noun')

    def get_verbs(self):
        return self._get_words('verb')

    def get_adjectives(self):
        return self._get_words('adjective')

    def add_noun(self, word):
        self._add_word('noun', word)

    def add_verb(self, word):
        self._add_word('verb', word)

    def add_adjective(self, word):
        self._add_word('adjective', word)
