import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

search_tag = "#flood"
keyword = search_tag.strip("#").lower()
results = []

# === 1. ReliefWeb ===
def scrape_reliefweb():
    print("Scraping ReliefWeb...")
    url = f"https://reliefweb.int/search?search={keyword}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.select("div.search-result")
    for article in articles:
        title_tag = article.find("h4", class_="rw-title")
        if title_tag and title_tag.a:
            link = "https://reliefweb.int" + title_tag.a["href"]
            issue = title_tag.get_text(strip=True)
            location_tag = article.select_one(".profile-location")
            location = location_tag.get_text(strip=True) if location_tag else "Unknown"
            summary = article.select_one(".search-result-body")
            summary_text = summary.get_text(strip=True) if summary else ""
            urgency = "High" if any(word in summary_text.lower() for word in ["emergency", "immediate", "urgent"]) else "Normal"
            results.append({"Source": "ReliefWeb", "Link": link, "Issue": issue, "Location": location, "Urgency": urgency})

# === 2. ECHO Daily Flash ===
def scrape_echo():
    print("Scraping ECHO Daily Flash...")
    url = "https://civil-protection-humanitarian-aid.ec.europa.eu/news_en"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.select("article.node--type-news")
    for article in articles[:10]:  # limit to 10 latest
        title_tag = article.select_one("h2")
        if not title_tag:
            continue
        link_tag = title_tag.find("a")
        issue = link_tag.get_text(strip=True)
        link = "https://civil-protection-humanitarian-aid.ec.europa.eu" + link_tag["href"]
        summary_tag = article.select_one(".field--name-field-news-teaser")
        summary_text = summary_tag.get_text(strip=True) if summary_tag else ""
        if keyword in issue.lower() or keyword in summary_text.lower():
            urgency = "High" if any(k in summary_text.lower() for k in ["emergency", "urgent", "alert"]) else "Normal"
            location = "Unknown"
            results.append({"Source": "ECHO", "Link": link, "Issue": issue, "Location": location, "Urgency": urgency})

# === 3. Google News (Very basic) ===
def scrape_google_news():
    print("Scraping Google News (basic)...")
    url = f"https://news.google.com/search?q={keyword}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.select("article h3")
    for article in articles[:10]:  # limit to 10
        a_tag = article.find("a")
        if a_tag:
            issue = a_tag.get_text(strip=True)
            link = "https://news.google.com" + a_tag["href"][1:]  # remove starting '.'
            urgency = "Check"
            location = "Unknown"
            results.append({"Source": "Google News", "Link": link, "Issue": issue, "Location": location, "Urgency": urgency})

# Run all scrapers
scrape_reliefweb()
time.sleep(2)
scrape_echo()
time.sleep(2)
scrape_google_news()

# Save to Excel
df = pd.DataFrame(results)
df.to_excel("resceu_scrape_results.xlsx", index=False)
print("✅ Scraping complete. Results saved to resceu_scrape_results.xlsx")
