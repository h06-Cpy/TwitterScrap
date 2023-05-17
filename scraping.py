from datetime import datetime, timezone
from snscrape.modules.twitter import TwitterSearchScraper
from models import Tweet
from database import Session
from preproc import preprocess


def scrape_twitter(query: str):
    scraper = TwitterSearchScraper(query)
    end_date = datetime(2019, 5, 1, tzinfo=timezone.utc)
    session = Session()

    i=0
    for tweet in scraper.get_items():
        if tweet.lang=='en':
            content = preprocess(tweet.rawContent)
            t = Tweet(content=content)
            session.add(t)
            session.commit()
            print(i)
            i+=1

        if tweet.date<end_date:
            break


scrape_twitter('microsoft')