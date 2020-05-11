from urllib.parse import urlparse

# Get the required domain name from url
def get_domain_name(url):
    try:
        results = get_subdomain(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


# Parse the url
def get_subdomain(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
