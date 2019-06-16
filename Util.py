from urllib.request import URLError, urlopen

def get_source(url):
    src = [
    'nytimes',
    'dj',
    'yahoo',
    'economist',
    'google',
    'marketwatch',
    'reuters',
    'bloomberg'
    ]
    url = url.lower()
    for i in src:
        if i in url:
            if i == '.dj.':
                return 'WSJ'
            if i == 'reuters':
                return 'Bloomberg'
            return i[0].upper() + i[1:]
    return url

def internet_on():
    try:
        urlopen('https://www.google.com', timeout=1)
        return True
    except URLError as err:
        return False