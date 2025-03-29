from cherry_pick.get_parser import get_parser
from cherry_pick.recipe_handlers import scrape_recipe, process_recipe
from recipe_scrapers import WebsiteNotImplementedError


def main():
    args = get_parser()

    try:
        scraper = scrape_recipe(str(args.url))
        process_recipe(scraper, args.markdown, args.pretty)
    except (WebsiteNotImplementedError, ValueError, Exception) as e:
        print(e)


if __name__ == "__main__":
    main()
