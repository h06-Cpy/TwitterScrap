import re
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer

tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
stemmer = PorterStemmer()

def preprocess(text:str):
    # remove unnecessary words
    text = re.sub(r'^RT[\s]+', '', text)
    text = re.sub(r'(\\u[0-9A-Fa-f]+)',r'', text)
    text = re.sub(r'[^\x00-\x7f]',r'',text)
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',text)
    text = re.sub(r'#([^\s]+)', r'', text)
    text = re.sub('@[^\s]+','',text)
    text = re.sub(r'[0-9]', '', text)

    # tokenizing and stemming
    tweet_tokens = tokenizer.tokenize(text)
    # tweet_stem = list()
    # for token in tweet_tokens:
    #     tweet_stem.append(stemmer.stem(token))

    # return ' '.join(tweet_stem)

    return ' '.join(tweet_tokens)

print(preprocess('''In honor of 
@MarvelStudios
’ #GotGVol3 we’re giving away this never opened Microsoft Zune. We have no idea if it works. Like and RT for a chance to win! US 18+. Ends 5/17/23. Rules: https://msft.it/6002gX0tC. #ZuneSweepstakes'''))