import argparse


def get_parser():
    parser = argparse.ArgumentParser(
        description="Scrape a recipe from a given URL and return it as a PDF file."
    )
    parser.add_argument("url", help="The URL of the recipe to scrape.")
    parser.add_argument(
        "-md", "--markdown", action="store_true",
        help="Exports the recipe in a Markdown file instead of a PDF file."
    )
    parser.add_argument(
        "--pretty", action="store_true",
        help="Makes the output file prettier."
    )

    return parser.parse_args()
