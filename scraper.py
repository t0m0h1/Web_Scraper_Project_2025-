import requests
from bs4 import BeautifulSoup

# Function to fetch product price
def get_amazon_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    # Send a GET request to Amazon product page
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Attempt to find the product price using typical Amazon HTML structure
        price = None
        
        # Look for the price in various HTML elements based on common Amazon product pages
        price_section = soup.find('span', {'id': 'priceblock_ourprice'})
        if not price_section:
            price_section = soup.find('span', {'id': 'priceblock_dealprice'})
        
        if price_section:
            price = price_section.text.strip()

        if price:
            return f"The price is: {price}"
        else:
            return "Price not found on this page."
    else:
        return "Failed to retrieve the webpage."

# Example usage
url = "https://www.amazon.co.uk/"  # Replace with your Amazon product URL
print(get_amazon_price(url))
