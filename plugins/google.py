import logging
from pygoogle import Google


def get(lighthouse, query):
    g = Google(query, pages=1, log_level=logging.CRITICAL)
    urls = g.get_urls()
    if urls:
        lighthouse.add_item(urls[0], "xdg-open " + urls[0])