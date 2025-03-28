import argparse
from recipe_scrapers import scrape_me, WebsiteNotImplementedError
from cherry_pick.recipe_to_md import generate_recipe_text


def main():
    parser = argparse.ArgumentParser(
        description="Scrape a recipe from a given URL and return it as a PDF file.")
    parser.add_argument("url", help="The URL of the recipe to scrape")

    args = parser.parse_args()

    try:
        scraper = scrape_me(str(args.url))
        md_text = generate_recipe_text(scraper)
        print(md_text)
    except WebsiteNotImplementedError:
        print("Sorry! The website is currently not supported by recipe-scrapers.")
    except ValueError:
        print("Oops! The input is not a valid url.")
    except Exception:
        print("Oops! URL could not be accessed, please use a different website.")


if __name__ == "__main__":
    main()
