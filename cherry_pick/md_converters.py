import markdown
from weasyprint import HTML, CSS
import os

pretty_css_path = os.path.join(os.path.dirname(__file__), "pretty-styles.css")
css_path = os.path.join(os.path.dirname(__file__), "styles.css")


def md_to_pdf(md_text: str, filename: str, pretty_flag: bool) -> None:
    """Saves the Markdown text to a styled PDF file.

    This function converts the Markdown text to HTML and generates a PDF using WeasyPrint. 
    If the `pretty_flag` is set to `True`, it applies different styling that results in
    a more visually appealing output.

    Args:
        md_text (str): The desired content of the PDF file.
        filename (str): Filename of the generated PDF file.
        pretty_flag (bool): If True, applies enhanced styling using `pretty-styles.css`

    Returns:
        None
    """
    html_content = markdown.markdown(md_text)
    if pretty_flag:
        full_html = f'<div class="recipe-container">{html_content}</div>'
        HTML(string=full_html).write_pdf(
            filename, stylesheets=[CSS(filename=pretty_css_path)])
    else:
        HTML(string=html_content).write_pdf(
            filename, stylesheets=[CSS(filename=css_path)])


def md_to_mdfile(md_text: str, filename: str) -> None:
    """Saves the Markdown text into a Markdown file.

    Args:
        md_text (str): The desired content of the markdown file.
        filename (str): Filename of the generated markdown file.

    Raises:
        Exception: Raised when an error occurs while saving the file.

    Returns:
        None
    """
    try:
        with open(filename, 'w') as md_file:
            md_file.write(md_text)
    except Exception as e:
        raise Exception(f"❌ Error saving markdown file: {e}")
