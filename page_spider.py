#!/usr/bin/python3
import os
import argparse
from utilities import url_utilities
from utilities import database_utilities


def main(database: str, url_list_file: str):
    print('Python Spider:\n')
    print('We are going to work with "{}" database and we going to scan "{}"'
          .format(database, url_list_file))

    big_word_list = []
    urls = url_utilities.load_urls_from_file(url_list_file)
    for url in urls:
        print('reading {}'.format(url))
        page_content = url_utilities.load_page(url=url)
        words = url_utilities.scrape_page(page_content)
        big_word_list.extend(words)

    # Database commands:
    os.chdir(os.path.dirname(__file__))  # current path
    # set a new path for DB file, should work the same for Win OS and Linux
    path = os.path.join(os.getcwd(), database)
    print('path: {}'.format(path))

    database_utilities.create_database(database_path=path)
    database_utilities.save_words_to_database(database_path=path, words_list=words)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-db', '--database', help='SQLite File Name')
    parser.add_argument('-i', '--input', help='File containing urls to read')
    args = parser.parse_args()
    database_file = args.database
    input_file = args.input

    main(database=database_file, url_list_file=input_file)
