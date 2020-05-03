from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):

    def __init__(self):
        super().__init__()

    def error(self):
        pass

    def handle_starttag(self, tag):
        print(tag)


#finder = LinkFinder()
#finder.feed('<html><head><title>Page Title</title></head><body>'
            '<h1>This is a Heading</h1><p>This is a paragraph.</p></body></html>')
