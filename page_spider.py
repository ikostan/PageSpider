#!/usr/bin/python3

import os
import argparse


def main(database: str, url_list_file: str):
    print('Python Spider:\n')
    print('We are going to work with "{}" database and we going to scan "{}"'
          .format(database, url_list_file))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-db', '--database', help='SQLite File Name')
    parser.add_argument('-i', '--input', help='File containing urls to read')
    args = parser.parse_args()
    database_file = args.database
    input_file = args.input
    main(database=database_file, url_list_file=input_file)
