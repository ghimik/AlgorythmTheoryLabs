import logging
import psycopg2
from psycopg2 import sql
from datetime import datetime
import matplotlib.pyplot as plt
from data.WordsProvider import WordsProvider
from words.Adjective import Adjective
from words.Noun import Noun
from words.Verb import Verb
from exceptions.DuplicateWordException import DuplicateWordException
from exceptions.WordNotFoundException import WordsNotFoundException

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("pgdb_words_provider.log"), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

class ActivityLogger:
    def __init__(self):
        self.add_word_times = []

    def log_activity(self, func_name, start_time, end_time):
        execution_time = (end_time - start_time).total_seconds()
        logger.info(f"{func_name} выполнен за {execution_time} секунд.")
        self.add_word_times.append(execution_time)

    def plot_add_word_activity(self):
        if not self.add_word_times:
            logger.info("Нет данных для построения графика активности добавления слов.")
            return
        plt.plot(range(1, len(self.add_word_times) + 1), self.add_word_times, marker='o')
        plt.title('Время выполнения добавления слов')
        plt.xlabel('Номер операции добавления')
        plt.ylabel('Время выполнения (секунды)')
        plt.grid(True)
        plt.show()

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
    def __init__(self, host, port, dbname, user, password, activity_logger=None):
        self.connection_params = {
            'host': host,
            'port': port,
            'dbname': dbname,
            'user': user,
            'password': password
        }
        self.activity_logger = activity_logger
        logger.info(f"Инициализирован PgDbWordsProvider с параметрами: {self.connection_params}")

    def _get_words(self, table_name):
        try:
            logger.debug(f"Получение слов из таблицы: {table_name}")
            with psycopg2.connect(**self.connection_params) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(sql.SQL("SELECT word FROM {}").format(sql.Identifier(table_name)))
                    words = cursor.fetchall()
                    f_words = [_create_word_instance(table_name, word[0]) for word in words]
                    if len(f_words) == 0:
                        raise WordsNotFoundException(table_name)
                    logger.info(f"Успешно получено {len(f_words)} слов из таблицы {table_name}")
                    return f_words
        except WordsNotFoundException:
            logger.error(f"Слова в таблице {table_name} не найдены.")
            return []
        except Exception as e:
            logger.error(f"Ошибка при получении слов из таблицы {table_name}: {e}")
            return []

    def _add_word(self, table_name, word):
        start_time = datetime.now()
        try:
            existing_words = self._get_words(table_name)
            if word in (w.word for w in existing_words):
                raise DuplicateWordException(word, table_name)

            with psycopg2.connect(**self.connection_params) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        sql.SQL("INSERT INTO {} (word) VALUES (%s)").format(sql.Identifier(table_name)),
                        [word]
                    )
                    conn.commit()
                    logger.info(f"Слово '{word}' успешно добавлено в таблицу {table_name}")
        except DuplicateWordException as e:
            logger.error(e)
            raise
        except Exception as e:
            logger.error(f"Ошибка при добавлении слова '{word}' в таблицу {table_name}: {e}")
        finally:
            end_time = datetime.now()
            if self.activity_logger:
                self.activity_logger.log_activity(f"Добавление слова в {table_name}", start_time, end_time)

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
