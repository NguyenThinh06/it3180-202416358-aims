import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearch(unittest.TestCase):
    def test_search_by_title_case_insensitive(self):
        items = [DigitalVideoDisc("The Lion King", "Animation", cost=19.95)]
        res = search_by_title(items, "lion")
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0].title, "The Lion King")


if __name__ == "__main__":
    unittest.main()
