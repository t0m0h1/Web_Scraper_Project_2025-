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
url = "https://www.amazon.co.uk/Jackery-Explorer-Portable-Versatile-Scenarios-Outdoor/dp/B0CYPKY7NQ/ref=sr_1_5?dib=eyJ2IjoiMSJ9._qZ5_VW0VeBfNa8IgKK-nS_MSgbzKHoolzZdegthLxUkNQ72PYMGLQSX_99O9mmyyAVDb7KF1ClYxpRYH5jli_SJAd9KEzKadq3w3aLBQwQDc4mjlieZxD2eikrDpGUf7ZY2X3za-PMn52Z_UUpXjeZEY5oeShYaz2pw1rMJPGJ7UgzEa-fQogaL3l-KnY8hZNhIVaQ-MHVMsntQjd7EDT0Bx6H-nBPblimn7HRjR2A.DvgaV6Vu1QlLCw3-gTLrmHRsrLjDeMhldDCLJDMa1KM&dib_tag=se&keywords=jackery&nsdOptOutParam=true&qid=1737668973&sr=8-5&ufe=app_do%3Aamzn1.fos.d7e5a2de-8759-4da3-993c-d11b6e3d217f&th=1"  # Replace with your Amazon product URL
print(get_amazon_price(url))
