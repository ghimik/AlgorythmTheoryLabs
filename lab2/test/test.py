import pytest

from data.InMemoryWordsProvider import InMemoryWordsProvider
from data.PgDbWordsProvider import PgDbWordsProvider
from words.Noun import Noun
from words.Verb import Verb
from words.Adjective import Adjective

@pytest.fixture
def provider():
    return InMemoryWordsProvider()

def test_get_nouns(provider):
    nouns = provider.get_nouns()
    assert len(nouns) > 0
    assert isinstance(nouns[0], Noun)

def test_get_verbs(provider):
    verbs = provider.get_verbs()
    assert len(verbs) > 0
    assert isinstance(verbs[0], Verb)

def test_get_adjectives(provider):
    adjectives = provider.get_adjectives()
    assert len(adjectives) > 0
    assert isinstance(adjectives[0], Adjective)


def test_add_noun(provider):
    new_noun = Noun("звезда")
    provider.add_noun(new_noun)
    nouns = provider.get_nouns()
    assert new_noun in nouns

def test_add_verb(provider):
    new_verb = Verb("светить")
    provider.add_verb(new_verb)
    verbs = provider.get_verbs()
    assert new_verb in verbs

def test_add_adjective(provider):
    new_adjective = Adjective("блестящий")
    provider.add_adjective(new_adjective)
    adjectives = provider.get_adjectives()
    assert new_adjective in adjectives

@pytest.fixture
def db_provider():
    return PgDbWordsProvider(
        host='localhost',
        port='5430',
        dbname='cytaty',
        user='postgres',
        password='admin'
    )

def test_db_get_nouns(db_provider):
    nouns = db_provider.get_nouns()
    assert len(nouns) > 0
    assert isinstance(nouns[0], Noun)

def test_db_get_verbs(db_provider):
    verbs = db_provider.get_verbs()
    assert len(verbs) > 0
    assert isinstance(verbs[0], Verb)

def test_db_get_adjectives(db_provider):
    adjectives = db_provider.get_adjectives()
    assert len(adjectives) > 0
    assert isinstance(adjectives[0], Adjective)

def test_db_add_noun(db_provider):
    new_noun = "полковник"
    db_provider.add_noun(new_noun)
    nouns = db_provider.get_nouns()
    assert any(n.word == new_noun for n in nouns)

def test_db_add_verb(db_provider):
    new_verb = "гонять"
    db_provider.add_verb(new_verb)
    verbs = db_provider.get_verbs()
    assert any(v.word == new_verb for v in verbs)

def test_db_add_adjective(db_provider):
    new_adjective = "мертвый"
    db_provider.add_adjective(new_adjective)
    adjectives = db_provider.get_adjectives()
    assert any(a.word == new_adjective for a in adjectives)
