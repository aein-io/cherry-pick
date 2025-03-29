from recipe_scrapers import scrape_me, WebsiteNotImplementedError
from cherry_pick.recipe_to_md import generate_recipe_text
from cherry_pick.md_converters import md_to_pdf, md_to_mdfile
from tqdm import tqdm
import time


def scrape_recipe(url: str) -> object:
    """Scrapes the recipe using `scrape_me` and handles errors.

    Args:
        url (str): The url of the recipe to be scraped.

    Raises:
        WebsiteNotImplementedError: Raised when the URL is not supported by `recipe-scrapers`.
        ValueError: Raised when the input is not a valid URL format.
        Exception: Raised other unexpected errors.

    Returns:
        An object containing the scraped recipe details.
    """
    try:
        with tqdm(total=1, desc="Scraping Recipe", unit="step") as pbar:
            scraper = scrape_me(url)
            time.sleep(1)
            pbar.update(1)
            return scraper
    except WebsiteNotImplementedError:
        raise WebsiteNotImplementedError(
            "❌ Sorry! The website is currently not supported by recipe-scrapers.")
    except ValueError:
        raise ValueError("❌ Oops! The input is not a valid URL.")
    except Exception as e:
        raise Exception(
            f"❌ Oops! An error occured while accessing the website: {str(e)}")


def process_recipe(scraper: object, md_flag: bool, pretty_flag: bool) -> None:
    """Processes the scraped recipe and saves it as either a Markdown or PDF file.

    Based on user input, this function extracts the recipe text and either:
    - Saves it as a Markdown file if `md_flag` is True.
    - Converts into a PDF otherwise.
    - If `pretty_flag` is True, enhanced styling (`pretty-styles.css`) is applied.

    Args:
        scraper (RecipeScraper): Contains the scraped recipe's details.
        md_flag (bool): If True, the text will be saved to a Markdown file.
        pretty_flag (bool): If True, applies enhanced styling using `pretty-styles.css`

    Returns:
        None
    """
    steps = ["Generating Markdown text", "Saving file"]

    with tqdm(total=len(steps), desc="Processing Recipe", unit="step") as pbar:
        md_text = generate_recipe_text(scraper, pretty_flag)
        pbar.update(1)

        filename = f"{scraper.title()}.md" if md_flag else f"{scraper.title()}.pdf"

        if md_flag:
            md_to_mdfile(md_text, filename)
        else:
            md_to_pdf(md_text, filename, pretty_flag)

        pbar.update(1)

    if md_flag:
        print(f"✅ Markdown file saved as {filename}")
    else:
        print(f"✅ PDF saved as {filename}")
