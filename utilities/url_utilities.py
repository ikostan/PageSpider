#!/usr/bin/python3
from urllib.request import urlopen


def load_urls_from_file(file_path: str):
    """
    Read the text file with the URL in it
    :type file_path: object str
    """
    try:
        with open(file_path) as file:
            content = file.readline()
            return content
    except FileNotFoundError as e:
        print('{}: {}'.format(e.strerror, e.filename))
        exit(2)
    except Exception as e:
        print(e)
        exit(2)


def load_page(url: str):
    """
    Reads the URL
    :type url: object str
    """
    response = urlopen(url)
    html = response.read.decode('utf-8')
    return html


def scrape_page(page_content: str):
    """
    Analyzes the text
    :type page_content: object str
    """
    # TODO: analyzes the text
    pass
