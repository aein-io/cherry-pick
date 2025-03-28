import pytest
from recipe_scrapers import scrape_me, WebsiteNotImplementedError


class TestErrors:
    def test_websitenotimplemented_err(self):
        with pytest.raises(WebsiteNotImplementedError):
            scrape_me(
                "https://iwashyoudry.com/last-minute-chicken-recipe/")

    def test_exception(self):
        with pytest.raises(Exception):
            scrape_me("https://www.teaforturmeric.com/chicken-biryani/")
