
import webbrowser
import requests
from bs4 import BeautifulSoup

# Function to scrape hospital details
def scrape_hospital_data(url):
    try:
        # Send a GET request to the hospital website
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example: Find contact information and services
        contact_info = soup.find_all(string=lambda text: 'contact' in text.lower())
        services = soup.find_all(string=lambda text: 'service' in text.lower())

        # Print or process the data
        print("Contact Information:")
        for info in contact_info:
            print(info.strip())

        print("\nServices Offered:")
        for service in services:
            print(service.strip())

        # Scrape social media links if available
        social_links = {
            "Instagram": None,
            "Facebook": None
        }

        # Scrape all links present in the page
        all_links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            all_links.append(href)  # Collect all links

            # Check for social media links specifically
            if 'instagram.com' in href:
                social_links["Instagram"] = href
            elif 'facebook.com' in href:
                social_links["Facebook"] = href

        # Print social media links
        print("\nSocial Media Links:")
        for platform, link in social_links.items():
            print(f"{platform}: {link if link else 'Not found'}")

        # Print all other links
        print("\nAll Links Found on the Page:")
        for link in all_links:
            print(link)

    except Exception as e:
        print(f"An error occurred: {e}")

# Step 1: Perform a Google Search
search_query = "Hubli dharwad multispeciality hospital websites"
url = f"https://www.google.com/search?q={search_query.replace(' ', '+')}"
webbrowser.open(url)

# Step 2: Get user input for the hospital URL after manual selection
hospital_url = input("\nEnter the URL of the hospital website you want to scrape: ")
scrape_hospital_data(hospital_url)
