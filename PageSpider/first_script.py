import os
import argparse


def main(database: str, url_list_path: str):
    print("Working with DB:", database)
    print("File to scan:", url_list_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help="SQLite File Name")
    parser.add_argument("-i", "--input", help="File containing URL to read")
    args = parser.parse_args()
    database_file = args.database
    file_path = args.input
    main(database=database_file, url_list_path=file_path)