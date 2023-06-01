from snscrape.modules.twitter import TwitterSearchScraper
from sqlalchemy.exc import IntegrityError
from models import Tweet
from database import Session
from datetime import datetime

def scrape_twitter(query: str, companyName: str):
    scraper = TwitterSearchScraper(query)
    session = Session()

    i=0
    for tweet in scraper.get_items():
        hashtags = ' '.join(tweet.hashtags) if tweet.hashtags is not None else None
        t = Tweet(id=tweet.id, rawContent=tweet.rawContent, renderedContent=tweet.renderedContent, lang=tweet.lang,
                  tweetDate=tweet.date, createdDate = datetime.now(), url=tweet.url, replyCount=tweet.replyCount,
                  retweetCount=tweet.replyCount, likeCount=tweet.likeCount, quoteCount=tweet.quoteCount,
                  conversationId=tweet.conversationId, source=tweet.source, sourceUrl=tweet.sourceUrl,
                  sourceLabel=tweet.sourceLabel, viewCount=tweet.viewCount, hashtags=hashtags, companyName=companyName)
        try:
            session.add(t)
            session.commit()
            print(i)
            i+=1
        except IntegrityError:
            session.rollback()

companies = ['apple', 'amazon', 'microsoft', 'google', 'intel', 'ibm', 'qualcomm', 'nvidia', 'tesla']
for company in companies:
    if company == 'apple':
        scrape_twitter('#Apple', company)
        scrape_twitter('@Apple', company)

    else:
        scrape_twitter(f'{company}', company)

