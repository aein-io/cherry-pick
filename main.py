from recipe_scrapers import scrape_me, WebsiteNotImplementedError
from cherry_pick.recipe_to_md import generate_recipe_text


def main():
    try:
        scraper = scrape_me(
            "https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/")
        md_text = generate_recipe_text(scraper)
        print(md_text)
    except WebsiteNotImplementedError:
        print("Sorry! The website is currently not supported by recipe-scrapers 😔")


if __name__ == "__main__":
    main()
