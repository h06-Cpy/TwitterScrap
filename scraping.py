from snscrape.modules.twitter import TwitterSearchScraper
from sqlalchemy.exc import IntegrityError
from models import Tweet
from database import Session
from datetime import datetime


def scrape_twitter(query: str, companyName: str):
    scraper = TwitterSearchScraper(query)
    session = Session()

    i = 0
    tmp_i = 0
    no_change_cnt = 0
    for tweet in scraper.get_items():
        tmp_i = i
        hashtags = ' '.join(tweet.hashtags) if tweet.hashtags is not None else None
        t = Tweet(id=tweet.id, rawContent=tweet.rawContent, renderedContent=tweet.renderedContent, lang=tweet.lang,
                  tweetDate=tweet.date, createdDate=datetime.now(), url=tweet.url, replyCount=tweet.replyCount,
                  retweetCount=tweet.replyCount, likeCount=tweet.likeCount, quoteCount=tweet.quoteCount,
                  conversationId=tweet.conversationId, source=tweet.source, sourceUrl=tweet.sourceUrl,
                  sourceLabel=tweet.sourceLabel, viewCount=tweet.viewCount, hashtags=hashtags, companyName=companyName)
        try:
            session.add(t)
            session.commit()
            print(i)
            i += 1
            no_change_cnt = 0
        except IntegrityError:
            session.rollback()

        if i - tmp_i == 0:
            no_change_cnt += 1

        if no_change_cnt > 199: # 연속으로 200번 트윗 못긁어오면 중지
            print('too many conflicts with tweets in db')
            break


companies = ['apple', 'amazon', 'microsoft', 'google', 'nvidia', 'tesla']
# companies = ['tesla']

for company in companies:
    if company == 'apple':
        scrape_twitter('#Apple', company)
        scrape_twitter('@Apple', company)

    else:
        scrape_twitter(f'{company}', company)
    scrape_twitter(f'{company}', company)
