# webScraper-py

# Recursive Web Scraper

A Python script to recursively scrape all unique links from a website, including links found on pages linked from the base page. It uses `requests` and `BeautifulSoup` for efficient and flexible web scraping.

## Features
- Scrapes links from the specified website.
- Recursively crawls links up to a user-defined depth.
- Filters links to ensure they belong to the same domain.
- Includes a polite delay between requests to avoid server overload.

## Requirements
- Python 3.6 or higher
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Leslie-23/webScraper-py.git
   cd recursive-web-scraper
Install the dependencies:
```
pip install beautifulSoup4 requests
```
Usage
Run the script:

```
python3 web-scraper.py
Enter the required input when prompted:
```
Base URL: The starting point for scraping (e.g., https://example.com).
Maximum Depth: The maximum recursion depth for crawling (e.g., 2).
Example:

```
Enter the base URL to scrape: https://example.com
Enter the maximum depth to crawl (e.g., 2): 2
The script will display the links it finds:
```

```
Found Links:
https://example.com
https://example.com/about
https://example.com/contact
```
Configuration
Modify the following variables in the script as needed:

max_depth: Set the maximum recursion depth for crawling.
time.sleep(0.5): Adjust the delay between requests to balance speed and server load.
Notes
The script only scrapes links within the same domain as the base URL.
Ensure the target website permits scraping by checking its robots.txt file.
Respect website terms of service and scraping policies.
Contributing
Contributions are welcome! Please follow these steps:

```
Fork the repository.
Create a new branch (git checkout -b feature-name).
Commit your changes (git commit -m "Add feature").
Push to the branch (git push origin feature-name).
Open a pull request.
```
License
This project is licensed under the MIT License.

Acknowledgements
This script uses:

Requests for HTTP requests.
BeautifulSoup for parsing HTML.
Happy Scraping!
