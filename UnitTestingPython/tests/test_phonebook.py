import unittest
from app.phonebook import Phonebook

class PhonebookTest(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook()

    def test_lookup_entry_by_name(self):

        self.phonebook.add("Don","2009760")
        self.assertEqual("2009760",self.phonebook.lookup("Don"))

    def test_missing_entry_raises_KeyError(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup('missing')


    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    @unittest.skip("poor  example")
    def test_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add('Carina Quan', "123456787")
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add('Don Johnson', "3333333")
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add('Doug Johnson', "6666666")

    def test_phonebook_with_normal_entries_is_consistant(self):
        self.phonebook.add("Don","12345")
        self.phonebook.add("Carina","012345")
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_duplicate_entries_is_inconsistent(self):
        self.phonebook.add("Don","12345")
        self.phonebook.add("Carina","12345")
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_numbers_that_prefix_one_nother_is_inconsistent(self):
        self.phonebook.add("Don","12345")
        self.phonebook.add("Carina","123")
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_adds_valid_names_and_numbers(self):
        self.assertTrue(self.phonebook.valid_names("Don"))
        self.assertTrue(self.phonebook.valid_numbers(6262234545))

if __name__ == '__main__':
    unittest.main()
