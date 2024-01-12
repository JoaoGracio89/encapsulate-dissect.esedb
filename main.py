# cli.py
import argparse

import dissect.esedb.record
from dissect.esedb import EseDB


def main():
    parser = argparse.ArgumentParser(description='Command-line interface for mylibrary.')

    parser.add_argument('file', type=str, help='edb file to parse')

    parser.add_argument('--available-table-columns', '-c', type=str, help='Check available table columns')
    parser.add_argument('--available-table-records', '-r', type=str, help='Check available table records')

    args = parser.parse_args()

    with open(args.file, 'rb') as fh:
        edb = EseDB(fh)
        print("Tables in file: ")
        for table in edb.tables():
            print(table.name + ", ", end="")
            '''
            for column in table.columns:
                print(f'\t{column.name}')
            print()
            '''

        if args.available_table_columns:
            columns = edb.table(args.available_table_columns).columns
            print()
            print()
            print("Columns Names for: " + args.available_table_columns)
            for column in columns:
                print(column.name, end=", ")

        if args.available_table_records:
            records = edb.table(args.available_table_records).records()
            columns = edb.table(args.available_table_records).columns
            print()
            print()
            print("Records for: " + args.available_table_records)
            for record in records:
                for column in columns:
                    if type(record.get(column.name)) is bytes:
                        try:
                            print(column.name + ": " + record.get(column.name).decode('utf-8'))
                        except:
                            print(column.name)


if __name__ == '__main__':
    main()
