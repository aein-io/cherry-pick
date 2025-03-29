from recipe_scrapers import scrape_me, WebsiteNotImplementedError
from cherry_pick.recipe_to_md import generate_recipe_text
from cherry_pick.md_converters import md_to_pdf, md_to_mdfile


def scrape_recipe(url):
    try:
        scraper = scrape_me(url)
        return scraper
    except WebsiteNotImplementedError:
        raise WebsiteNotImplementedError(
            "❌ Sorry! The website is currently not supported by recipe-scrapers.")
    except ValueError:
        raise ValueError("❌ Oops! The input is not a valid URL.")
    except Exception as e:
        raise Exception(
            f"❌ Oops! An error occured while accessing the website: {str(e)}")


def process_recipe(scraper, md_flag, pretty_flag):
    md_text = generate_recipe_text(scraper, pretty_flag)

    if md_flag:
        md_to_mdfile(md_text, f"{scraper.title()}.md")
    else:
        md_to_pdf(md_text, f"{scraper.title()}.pdf", pretty_flag)
