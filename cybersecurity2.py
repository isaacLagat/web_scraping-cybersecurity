import requests
from bs4 import BeautifulSoup
def scrape_security_news():
    url = "https://www-security-news.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = soup.find_all('h2, class_="security-headline')
    return [headline.text for headline in headlines]

# For example
security_headlines = scrape_security_news()
print("security_headlines" , security_headlines)