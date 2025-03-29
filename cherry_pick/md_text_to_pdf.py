import os
import markdown
from xhtml2pdf import pisa

# Define font path
FONT_PATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../fonts/NotoColorEmoji.ttf"))

# HTML Template with CSS Styling
HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{
            font-family: 'Noto Sans', sans-serif;
            font-size: 14px;
        }}
        h1 {{ font-size: 24px; color: #333; }}
        h2 {{ font-size: 20px; color: #555; }}
        ul, ol {{ margin-left: 20px; }}
    </style>
</head>
<body>
    {content}
</body>
</html>
"""


def md_text_to_pdf(md_text: str, filename: str):
    """Convert Markdown to PDF with proper emoji and formatting support."""

    # Convert Markdown to HTML
    html_content = markdown.markdown(md_text)

    # Wrap content in the template
    full_html = HTML_TEMPLATE.format(content=html_content)

    # Write to PDF
    with open(filename, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(full_html, dest=pdf_file)

    if pisa_status.err:
        print("❌ Error: Could not generate PDF")
    else:
        print(f"✅ PDF saved as {filename}")
