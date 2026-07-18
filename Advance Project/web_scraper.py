import requests
from bs4 import BeautifulSoup
import csv

def scrape_site(url, output_file="scraped_data.csv"):
    # Send request
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code != 200:
        print("⚠ Failed to retrieve page")
        return
    
    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Example: scrape article titles + links
    articles = soup.find_all("a")
    
    data = []
    for a in articles:
        title = a.get_text(strip=True)
        link = a.get("href")
        if title and link:
            data.append([title, link])
    
    # Save to CSV
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Link"])
        writer.writerows(data)
    
    print(f"✅ Scraped {len(data)} items → {output_file}")

# CLI demo
if __name__ == "__main__":
    url = input("Enter website URL: ")
    scrape_site(url)
