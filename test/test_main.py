import unittest
from recipe_scrapers import scrape_me, WebsiteNotImplementedError


class TestMain(unittest.TestCase):
    def test_websitenotimplemented_err(self):
        with self.assertRaises(WebsiteNotImplementedError):
            scrape_me(
                "https://iwashyoudry.com/last-minute-chicken-recipe/")


if __name__ == "__main__":
    unittest.main()
