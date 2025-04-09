# 🍒 Cherry-Pick: Recipe Scraper & Converter

Cherry Pick is a simple CLI tool that helps you get to the meat of a recipe by cutting through the background noise and serving it on a silver platter as a clean, formatted PDF or Markdown file.

## 🚀 Features
- Extract recipes from supported websites of [recipe-scrapers](https://github.com/hhursev/recipe-scrapers).
- Export recipes as **beautifully formatted PDFs** or **Markdown files**.
- Uses WeasyPrint for **PDF styling**.

## 🛠️ Installation
### 1️⃣ Install Dependencies
Cherry-Pick requires Python **3.10+** and the following system dependencies for WeasyPrint:

#### **For Debian/Ubuntu**
```sh
sudo apt install libpango-1.0-0 libcairo2 libpangoft2-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0
```
#### **For macOS (Homebrew)**
```sh
brew install pango cairo gdk-pixbuf
```
#### **For Windows**
Windows users should install WeasyPrint's required dependencies from [GTK for Windows](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases).

### 2️⃣ Install Cherry-Pick
```sh
git clone https://github.com/aein-io/cherry-pick.git
cd cherry-pick
poetry install
```

## 📌 Usage
Run Cherry-Pick from the command line:
```sh
python poetry run cherry-pick <url> [options]
```

## 📜 Arguments
| Argument            | Description                                            |
| ------------------- | ------------------------------------------------------ |
| `url`               | The URL of the recipe to scrape.                       |
| `-md`, `--markdown` | Export the recipe as a Markdown file instead of a PDF. |
| `--pretty`          | Apply enhanced formatting to the PDF.                  |

## 🛠️ Contributing
1. Fork the repository 🍴
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to your branch (`git push origin feature-branch`)
5. Submit a pull request ✅

## ⚖️ License
This project is licensed under the MIT License.

---
Enjoy your recipe scraping! 🍳✨

