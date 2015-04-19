import logging
from pygoogle import Google


def get(lighthouse, query):
    g = Google(query, log_level=logging.CRITICAL)
    g.pages = 1
    urls = g.get_urls()
    if urls:
        lighthouse.add_item(urls[0], "xdg-open " + urls[0])