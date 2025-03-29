import pytest
from recipe_scrapers import scrape_me, WebsiteNotImplementedError
from cherry_pick.recipe_handlers import scrape_recipe, process_recipe


class TestErrors:
    def test_websitenotimplemented_err(self):
        with pytest.raises(WebsiteNotImplementedError):
            scrape_recipe(
                "https://iwashyoudry.com/last-minute-chicken-recipe/")

    def test_value_err(self):
        with pytest.raises(ValueError):
            scrape_recipe("asdfghjkl")

    def test_exception(self):
        with pytest.raises(Exception):
            scrape_recipe("https://www.teaforturmeric.com/chicken-biryani/")
