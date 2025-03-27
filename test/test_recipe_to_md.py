import pytest
from recipe_scrapers import scrape_me
from cherry_pick.recipe_to_md import safe_call


class TestSafeCall:
    @classmethod
    def setup_class(cls):
        cls.scraper = scrape_me(
            "https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/")

    def test_valid_scraper_method(self):
        result = safe_call(self.scraper.title)
        assert result == "Spinach and Feta Turkey Burgers"

    def test_invalid_scraper_method(self):
        result = safe_call(self.scraper.dietary_restrictions)
        assert result == "None"
