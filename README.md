# 📰 News Web Scraper

A simple Python script that scrapes the latest news headlines from [Al Jazeera News](https://www.aljazeera.com/news/) and saves them into a `.txt` file.

## Objective

To automate the extraction of top news headlines from a public website using Python and store them in a human-readable format for future reference or analysis.

## Tools & Libraries

- `requests` – To send HTTP requests and fetch the webpage content
- `BeautifulSoup` – For parsing HTML and extracting data

## Project Structure

WebScraper/
│
├── news_scrapper.py       # Main Python script
└── headlines.txt           # Output file containing scraped headlines


## How It Works

1. **Fetch**: Sends a GET request to the news site.
2. **Parse**: Uses BeautifulSoup to find all `<h3>` tags (commonly used for headlines).
3. **Save**: Writes the extracted headlines into `headlines.txt` file.


## Example Output

The `headlines.txt` will look like this:

1. Israel's war on Gaza: List of key events, day 303
2. Ukrainian drone strikes Russian landing ship near Crimea
3. UN urges global action over spiralling climate disasters
...

### How to Run

Make sure Python is installed. Then, install the required libraries:

```bash
pip install requests beautifulsoup4
```

### Run the Script

```bash
python news_scrapper.py
```

If successful, it will print:
Headlines successfully saved to headlines.txt
