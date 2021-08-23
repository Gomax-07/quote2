class Source:
    '''
    Class the defines the sources object
    '''

    def __init__(self, id, name, url, country, description):
        self.id = id
        self.name = name
        self.url = url
        self.country = country
        self.description = description

class Everything:
    '''
    Class That defines the news Objects
    '''

    def __init__(self, author, title, description, url, urlToImage, publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

class Headlines:
    '''
    Class That defines the headlines object
    '''
    def __init__(self, author, title, description, url, urlToImage, publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt


class Tech:
    """
    Class that defines the Tech object
    """
    
    def __init__(self,author, title, description, url, urlToImage, publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt