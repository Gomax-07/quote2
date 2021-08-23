from .main import main
import urllib.request, json
from .models import Everything, Tech, Source, Headlines

# # Getting the API KEY
api_key = None
source_url = None
top_headlines_url = None
everything_url = None
tech_url = None

def configure_request(app):
    global api_key, source_url, top_headlines_url, everything_url, tech_url
    api_key = app.config['NEWS_API_KEY']
    source_url = app.config['SOURCE_API_BASE_URL']
    top_headlines_url = app.config['TOP_HEADLINES_API_BASE_URL']
    everything_url = app.config['EVERYTHING_API_BASE_URL']
    tech_url = app.config['TECH_API_BASE_URL']



def get_news_source():
    '''
    Function that gets the json response to our url request, fetching all the sources data.
    and we'll return all the required news source.
    '''

    news_url = source_url.format(api_key)

    with urllib.request.urlopen(news_url) as url:
        source_data = url.read()
        source_response = json.loads(source_data)
        source_results = None

        if source_response ['sources']:
            source_items = source_response['sources']
            source_results = process_source_data(source_items)

    return source_results


def process_source_data(source_list):
    '''
    Function that proces the source result and transform them to a list of objects

    Args:
        Each source will  required to have diff definations
    '''

    source_processed = []
    for item in source_list:
        id = item.get('id')
        name = item.get('name')
        url = item.get('url')
        country = item.get('country')
        description = item.get('description')
        new_source = Source(id, name, url, country, description)
        source_processed.append(new_source)

    return source_processed

def get_news_headlines(source):
    '''
    Function retrieves top stories/headlines news and passing the json as the
    data intended
    '''

    top_stories_url = top_headlines_url.format(source, api_key)

    with urllib.request.urlopen(top_stories_url) as url:
        headline_data = url.read()
        headline_response = json.loads(headline_data)
        headline_results = None

        if headline_response['articles']:
            headline_items = headline_response['articles']
            headline_results = process_headline_data(headline_items)
        
    return headline_results


def process_headline_data(headline_list):
    '''
    Function Converts data to the class in the model
    '''

    top_story = []
    for item in headline_list:
        author = item.get('author')
        title = item.get('title')
        description = item.get('description')
        url = item.get('url')
        urlToImage = item.get('urlToImage')
        publishedAt = item.get('publishedAt')
        new_headline = Headlines(author, title,  description, url, urlToImage, publishedAt)
        top_story.append(new_headline)

    return top_story


def get_everything():
    '''
    Retrives every news and passing it as json object
    '''
    every_news = everything_url.format(api_key)

    with urllib.request.urlopen(every_news) as url:
        everything_data = url.read()
        everything_response = json.loads(everything_data)
        everything_results = None

        if everything_response['articles']:
            everything_results_list = everything_response['articles']
            everything_results = process_everything(everything_results_list)
            
    return everything_results

def process_everything(everything_results_list):
        '''
        Function Converts data to the class in the Everything class model
        '''
        everything_results = []
        for item in everything_results_list:
            author = item.get('author')
            title = item.get('title')
            description = item.get('description')
            url = item.get('url')
            urlToImage = item.get('urlToImage')
            publishedAt = item.get('publishedAt')

            everything_object = Everything(author, title, description, url, urlToImage, publishedAt)
            everything_results.append(everything_object)
        
        return everything_results


def tech_headlines():
    '''
    Function that gets the Tech News.
    '''

    tech_news_url = tech_url.format(api_key)

    with urllib.request.urlopen(tech_news_url) as url:
        tech_data = url.read()
        tech_response = json.loads(tech_data)
        tech_results = None
        
        if tech_response['articles']:
            tech_results_list = tech_response['articles']
            tech_results = process_tech_results(tech_results_list)

    return tech_results

def process_tech_results(tech_results_list):
    '''
    Function that will convert the data being pulled to a json file
    '''
    tech_results = []
    for item in tech_results_list:
        author = item.get('author')
        title = item.get('title')
        description = item.get('description')
        url = item.get('url')
        urlToImage = item.get('urlToImage')
        publishedAt = item.get('publishedAt')

        tech_object = Tech(author, title, description, url, urlToImage, publishedAt)
        tech_results.append(tech_object)

    return tech_results