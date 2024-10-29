import pytest
from tasks.first import generate_random_notes
from tasks.second import multiples_of_three
from tasks.third import filter_valid_emails

notes = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']


def test_generate_random_notes():
    generated_notes = generate_random_notes()
    assert len(generated_notes) == 20
    assert all(note in notes for note in generated_notes)


def test_multiples_of_three():
    gen = multiples_of_three(0)
    assert next(gen) == 0
    assert next(gen) == 3
    assert next(gen) == 6

    gen_negative = multiples_of_three(-3)
    assert next(gen_negative) == -3
    assert next(gen_negative) == 0
    assert next(gen_negative) == 3



def test_filter_valid_emails():
    emails_input = "@test@example.com wrong_email.com another.correct@domain.com"
    filtered_emails = filter_valid_emails(emails_input)
    assert filtered_emails == ["another.correct@domain.com"]

    emails = "test@domain.com invalid@com user@domain.org no-at-symbol.com"
    assert filter_valid_emails(emails) == ["test@domain.com", "user@domain.org"]

    assert filter_valid_emails("") == []
