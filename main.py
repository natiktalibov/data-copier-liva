from config import DB_DETAILS
from util import get_tables


def main():
    db_details = DB_DETAILS['dev']
    # print(db_details)
    tables = get_tables('table_list')
    for table in tables['table_name']:
        print(table)


if __name__ == '__main__':
    main()
