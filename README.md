# GPU Price Scraper

This project is a web scraper designed to collect GPU prices from Newegg using Python, BeautifulSoup, and requests. The scraped data is saved into a CSV file for further analysis.

## Features

- Scrapes GPU data from Newegg(https://www.newegg.com/) based on user input.
- Extracts GPU names and their current prices.
- Saves the scraped data into a CSV file.

## Installation

To run this project, you'll need to have Python installed on your system. You can install the required libraries using pip:

```bash
pip install requests beautifulsoup4
```

## Example
Here's an example of how to use the script:

```bash
$ GPUprice.py
What GPU are you looking for? RTX 3080
Total Number of pages: 5
Item: MSI Gaming GeForce RTX 3080
Price: $699.99
...
```

## file structure
- GPUprice.py
- GPUprice.txt

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/)
