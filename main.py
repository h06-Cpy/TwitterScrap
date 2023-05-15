from datetime import datetime

from snscrape.modules.twitter import TwitterSearchScraper

scraper = TwitterSearchScraper('microsoft')

result = []

for i, item in enumerate(scraper.get_items()):
    result.append(item)
    if i == 10:
        break

print(result)
