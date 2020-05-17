import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *


# Adding Project information
PROJECT_NAME = input("Enter name of project:    ")
HOMEPAGE = input("Enter url to start crawling: ")
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 4
thread_queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


# Create multiple spiders for crawling
def create_spiders():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Work function for spiders
def work():
    while True:
        url = thread_queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        thread_queue.task_done()


# create jobs
def create_jobs():
    queued = file_to_set(QUEUE_FILE)
    for links in queued:
        thread_queue.put(links)
    thread_queue.join()
    crawl()


# check if there's any link in queue file, if so crawl them
def crawl():
    queued = file_to_set(QUEUE_FILE)
    if len(queued) > 0:
        print(str(len(queued)) + ' links in the queue')
        create_jobs()


create_spiders()
crawl()
