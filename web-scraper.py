#!/usr/bin/env python3

# File: recursive_link_scraper.py

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque
import time

def scrape_links_recursive(base_url, max_depth=2):
    """
    Recursively scrape links from a website.
    Args:
        base_url (str): The starting URL.
        max_depth (int): Max depth for recursive scraping.
    Returns:
        set: A set of all unique links found on the site.
    """
    visited = set()
    to_visit = deque([(base_url, 0)])  # (url, depth)
    all_links = set()
    
    while to_visit:
        url, depth = to_visit.popleft()
        if depth > max_depth or url in visited:
            continue

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error accessing {url}: {e}")
            continue

        visited.add(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for link in soup.find_all('a', href=True):
            absolute_url = urljoin(url, link['href'])
            if is_valid_link(absolute_url, base_url):
                all_links.add(absolute_url)
                if absolute_url not in visited:
                    to_visit.append((absolute_url, depth + 1))

        print(f"Visited: {url} (Depth: {depth})")
        time.sleep(0.5)  # Polite delay to avoid overwhelming the server

    return all_links

def is_valid_link(link, base_url):
    """
    Checks if the link is valid and belongs to the same domain.
    """
    parsed_base = urlparse(base_url)
    parsed_link = urlparse(link)
    return parsed_link.scheme in ['http', 'https'] and parsed_base.netloc == parsed_link.netloc

if __name__ == "__main__":
    start_url = input("Enter the base URL to scrape: ").strip()
    max_depth = int(input("Enter the maximum depth to crawl (e.g., 2): ").strip())

    print("Starting scraping...")
    links = scrape_links_recursive(start_url, max_depth=max_depth)
    print("\nFound Links:")
    for link in links:
        print(link)
