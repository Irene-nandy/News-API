# import os
# class Config:
#     '''
#     General configuration parent class
#     '''
#     NEWS_SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?apiKey=3da9679d84c645fa80b1a7845aa12a71'
#     ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey=3da9679d84c645fa80b1a7845aa12a71'
#     NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
#     SECRET_KEY = os.environ.get('SECRET_KEY')

#     @staticmethod
#     def init_app(app):
#             pass


# class ProdConfig(Config):
#     pass


# class DevConfig(Config):
#     DEBUG = True


# config_options = {
#     'development': DevConfig,
#     'production': ProdConfig

# }