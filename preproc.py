import re
from nltk.tokenize import TweetTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk
import string

nltk.download('stopwords')
nltk.download('wordnet')

tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
stop_words = stop_words | {'would', 'im', 'ive', 'thing', 'thats', 'probably', 'someone', 'think', 'actually', 'cant',
                           'much', 'anything', 'something', 'lol', 'stuff', 'bit', 'really', 'still', 'shit',
                           'literally', 'even', 'always', 'time', 'never', 'little', 'yeah', 'didnt', 'pretty',
                           'friend', 'nothing', 'maybe', 'look', 'lot', 'came', 'isnt', 'theyre', 'dont', 'doesnt',
                           'um', 'ye', 'hmm', 'un', 'uh', 'eh', 'huh', 'ya', 'yo', 'yea', 'ah', 'nah', 'fuck',
                           'fucking'}

def preprocess(text:str, comp_name: str):

    stop_words.add(comp_name)

    # remove unnecessary words
    text = re.sub(r'^RT[\s]+', '', text)
    text = re.sub(r'(\\u[0-9A-Fa-f]+)',r'', text)
    text = re.sub(r'[^\x00-\x7f]',r'',text)
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',text)
    text = re.sub(r'[0-9]', '', text)
    text = re.sub(r'#', '', text)
    text = re.sub('@[^\s]+','',text)
    text = text.translate(str.maketrans('', '', string.punctuation))

    # tokenizing and lemmatization
    tweet_tokens = tokenizer.tokenize(text)
    tweet_tokens = [t for t in tweet_tokens if t not in stop_words]
    if len(tweet_tokens)<4:
        return None
    lemm_tokens = [lemmatizer.lemmatize(token) for token in tweet_tokens]
    return ' '.join(lemm_tokens)


def removeUnicode(text):
    """ Removes unicode strings like "\u002c" and "x96" """
    text = re.sub(r'(\\u[0-9A-Fa-f]+)',r'', text)
    text = re.sub(r'[^\x00-\x7f]',r'',text)
    return text

def replaceURL(text):
    """ Replaces url address with "url" """
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','url',text)
    text = re.sub(r'#([^\s]+)', r'\1', text)
    return text

def replaceAtUser(text):
    """ Replaces "@user" with "atUser" """
    text = re.sub('@[^\s]+','atUser',text)
    return text

def removeHashtagInFrontOfWord(text):
    """ Removes hastag in front of a word """
    text = re.sub(r'#([^\s]+)', r'\1', text)
    return text

def removeNumbers(text):
    """ Removes integers """
    text = re.sub(r'[0-9]', '', text)
    return text

def replaceMultiExclamationMark(text):
    """ Replaces repetitions of exlamation marks """
    text = re.sub(r"(\!)\1+", ' multiExclamation ', text)
    return text

def replaceMultiQuestionMark(text):
    """ Replaces repetitions of question marks """
    text = re.sub(r"(\?)\1+", ' multiQuestion ', text)
    return text

def replaceMultiStopMark(text):
    """ Replaces repetitions of stop marks """
    text = re.sub(r"(\.)\1+", ' multiStop ', text)
    return text

def removeEmoticons(text):
    """ Removes emoticons from text """
    text = re.sub(':\)|;\)|:-\)|\(-:|:-D|=D|:P|xD|X-p|\^\^|:-*|\^\.\^|\^\-\^|\^\_\^|\,-\)|\)-:|:\'\(|:\(|:-\(|:\S|T\.T|\.\_\.|:<|:-\S|:-<|\*\-\*|:O|=O|=\-O|O\.o|XO|O\_O|:-\@|=/|:/|X\-\(|>\.<|>=\(|D:', '', text)
    return text
# print(preprocess('''In honor of
# @MarvelStudios
# ’ #GotGVol3 we’re giving away this never opened Microsoft Zune. We have no idea if it works. Like and RT for a chance to win! US 18+. Ends 5/17/23. Rules: https://msft.it/6002gX0tC. #ZuneSweepstakes'''))