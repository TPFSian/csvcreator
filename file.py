import requests
from bs4 import BeautifulSoup
import csv

def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        data = []
        
        # Modify these selectors according to the structure of the website
        title_elements = soup.select('.post-title')
        content_elements = soup.select('.post-content')
        
        for title, content in zip(title_elements, content_elements):
            data.append({
                'Title': title.get_text(),
                'Content': content.get_text()
            })
        
        return data
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return None

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Content']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow(item)

if __name__ == "__main__":
    target_url = "https://example.com"  # Replace with the URL you want to scrape
    scraped_data = scrape_website(target_url)
    
    if scraped_data:
        output_filename = "scraped_data.csv"
        save_to_csv(scraped_data, output_filename)
        print(f"Scraping completed. Data saved to {output_filename}")
