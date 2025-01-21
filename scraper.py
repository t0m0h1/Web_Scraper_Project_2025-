import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example: Extract the page title
        title = soup.title.string if soup.title else "No title found"
        print(f"Page Title: {title}")
        
        # Example: Extract all headers (h1, h2, h3)
        print("\nHeaders:")
        for header_tag in ['h1', 'h2', 'h3']:
            headers = soup.find_all(header_tag)
            for header in headers:
                print(f"{header_tag.upper()}: {header.get_text(strip=True)}")
        
        # Example: Extract all links
        print("\nLinks:")
        links = soup.find_all('a', href=True)
        for link in links:
            print(link['href'])
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        

# URL to scrape
website = 'https://www.bbc.co.uk/news'
scrape_website(website)
