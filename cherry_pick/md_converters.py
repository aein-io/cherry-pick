import markdown
from weasyprint import HTML, CSS
import os

pretty_css_path = os.path.join(os.path.dirname(__file__), "pretty-styles.css")
css_path = os.path.join(os.path.dirname(__file__), "styles.css")


def md_to_pdf(md_text, filename, pretty_flag):
    html_content = markdown.markdown(md_text)
    if pretty_flag:
        full_html = f'<div class="recipe-container">{html_content}</div>'
        HTML(string=full_html).write_pdf(
            filename, stylesheets=[CSS(filename=pretty_css_path)])
    else:
        HTML(string=html_content).write_pdf(
            filename, stylesheets=[CSS(filename=css_path)])
    print(f"✅ PDF saved as {filename}")


def md_to_mdfile(md_text, filename):
    try:
        with open(filename, 'w') as md_file:
            md_file.write(md_text)
        print(f"✅ Markdown file saved as {filename}")
    except Exception as e:
        print(f"❌ Error saving markdown file: {e}")
