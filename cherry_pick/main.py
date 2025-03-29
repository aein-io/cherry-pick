import argparse
from recipe_scrapers import scrape_me, WebsiteNotImplementedError
from cherry_pick.recipe_to_md import generate_recipe_text
from cherry_pick.md_converters import md_to_pdf, md_to_mdfile


def main():
    parser = argparse.ArgumentParser(
        description="Scrape a recipe from a given URL and return it as a PDF file.")
    parser.add_argument("-md", "--markdown", action="store_true",
                        help="Exports the recipe in a Markdown file instead of a PDF file.")
    parser.add_argument("--pretty", action="store_true",
                        help="Makes the output file prettier.")
    parser.add_argument("url", help="The URL of the recipe to scrape.")

    args = parser.parse_args()

    try:
        scraper = scrape_me(str(args.url))
        md_text = generate_recipe_text(scraper, args.pretty)
        if args.markdown:
            md_to_mdfile(md_text, f"{scraper.title()}.md")
        else:
            md_to_pdf(md_text, f"{scraper.title()}.pdf", args.pretty)
    except WebsiteNotImplementedError:
        print("Sorry! The website is currently not supported by recipe-scrapers.")
    except ValueError:
        print("Oops! The input is not a valid url.")
    except Exception:
        print("Oops! URL could not be accessed, please use a different website.")


if __name__ == "__main__":
    main()
