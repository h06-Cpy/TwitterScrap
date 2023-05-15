from datetime import datetime, timezone
from snscrape.modules.twitter import TwitterSearchScraper


def scrape_twitter(query: str, limit: int = 500):
    scraper = TwitterSearchScraper(query)
    end_date = datetime(2019, 5, 1, tzinfo=timezone.utc)
    # i = 0
    # for item in scraper.get_items():
    #     if i == limit:
    #         break
    #     with open(f'./data/tweet{i}.txt', 'w', encoding='utf-8') as f:
    #         if (item.date > end_date) and item.lang == 'en':
    #             f.write(item.rawContent)
    #             i += 1
    #             print(i)

    tweets = scraper.get_items()
    for i in range(limit):
        with open(f'./data/tweet{i}.txt', 'w', encoding='utf-8') as f:
            j=0
            while j<500:
                tweet = next(tweets)
                if (tweet.date > end_date) and tweet.lang == 'en':
                    f.write(tweet.rawContent+'\n')
                    j+=1
        if tweet.date<end_date: break