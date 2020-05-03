from urllib.request import urlopen
from link_finder import LinkFinder
from general import *


class Spider:
    project_name = ''
    base_url = ''
    page_url = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self):
        
