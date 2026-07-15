import requests
from bs4 import BeautifulSoup
import argparse
import json
import csv
import sys
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def scrape_website(url, tag, class_name=None, limit=20, output=None):
    try:
        print(f"Scraping {url} for <{tag}> elements...")

        # Session with retries
        session = requests.Session()
        retries = Retry(total=3, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
        session.mount("http://", HTTPAdapter(max_retries=retries))
        session.mount("https://", HTTPAdapter(max_retries=retries))

        headers = {"User-Agent": "Mozilla/5.0 (compatible; AdvancedScraper/1.0)"}
        response = session.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        elements = soup.find_all(tag, class_=class_name) if class_name else soup.find_all(tag)

        results = []
        for i, element in enumerate(elements[:limit]):
            item = {"index": i+1, "text": element.get_text(strip=True)}
            if element.name == "a":
                item["link"] = element.get("href")
            results.append(item)

        # Output handling
        if output:
            if output.endswith(".json"):
                with open(output, "w", encoding="utf-8") as f:
                    json.dump(results, f, ensure_ascii=False, indent=2)
                print(f"✅ Results saved to {output}")
            elif output.endswith(".csv"):
                with open(output, "w", newline="", encoding="utf-8") as f:
                    writer = csv.DictWriter(f, fieldnames=results[0].keys())
                    writer.writeheader()
                    writer.writerows(results)
                print(f"✅ Results saved to {output}")
            else:
                print("⚠ Unsupported output format. Use .json or .csv")
        else:
            for item in results:
                print(f"{item['index']}: {item['text']}")
                if "link" in item:
                    print(f"   Link: {item['link']}")
                print("-" * 10)

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching URL: {e}")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advanced Web Scraper")
    parser.add_argument("url", help="Website URL to scrape")
    parser.add_argument("tag", help="HTML tag to search for (e.g. h1, a, p, div)")
    parser.add_argument("--class", dest="class_name", help="Filter by class name", default=None)
    parser.add_argument("--limit", type=int, help="Max number of elements to fetch", default=20)
    parser.add_argument("--output", help="Save results to file (.json or .csv)", default=None)

    args = parser.parse_args()
    scrape_website(args.url, args.tag, args.class_name, args.limit, args.output)
