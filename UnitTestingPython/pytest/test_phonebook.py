import pytest
from phonebook import Phonebook

@pytest.fixture
def phonebook(tmpdir):
    """Provides empty Phonebook"""
    phonebook = Phonebook(tmpdir)
    return phonebook

def test_add_and_lookup_entry(phonebook):
    phonebook.add("Don","1234")
    assert "1234" == phonebook.lookup("Don")

def test_phonebook_gives_access_to_names_and_numbers(phonebook):
    phonebook.add("Carina","12345")
    phonebook.add("Don","1234")
    assert set(phonebook.names()) == {"Carina","Don"}
    assert "12345" in phonebook.numbers()

def test_missing_entry_raises_KeyError(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("missing")
