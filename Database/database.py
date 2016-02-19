import sqlite3 as sql

from ..Resource.enumerations import SortingOrder


class Database:
    # Object management #
    def __init__(self, name):
        self.name = name
        self.tables = dict()
        self.__connect()

    def __del__(self):
        self.__close()

    def __connect(self):
        self.connection = sql.connect(self.name + ".db")
        self.connection.row_factory = sql.Row
        self.cursor = self.connection.cursor()
        self.__get_database_info()

    def __close(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    # Info #
    def __get_database_info(self):
        tables = self.cursor.execute("SELECT name FROM sqlite_master WHERE\
                                     type='table'")
        for table in tables:
            name = table['name']
            columns = self.cursor.execute("PRAGMA table_info({})".format(name))
            self.tables[name] = [column['name'] for column in columns]

    def row_count(self, table):
        self.cursor.execute("SELECT COUNT(*) AS value FROM {0}".format(table))
        return self.next()['value']

    def row_exists(self, table, values):
        columns = self.tables[table]
        wheres = ["`" + str(column) + "`=\'" + str(value) + "\'" for column,
                  value in zip(columns, values)]
        self.cursor.execute("SELECT COUNT(*) AS value FROM {0} WHERE {1}"
                            .format(table, " AND ".join(wheres)))
        return self.next()['value'] > 0

    # Fetching #
    def all_from_table(self, table):
        self.cursor.execute("SELECT * FROM {0}".format(table))

    def next(self):
        return self.cursor.fetchone()

    def next_from_table(self, table):
        self.all_from_table(table)
        return self.cursor.fetchone()

    # Modifying #
    def create_table(self, table, columns):
        self.tables[table] = columns
        self.cursor.execute("CREATE TABLE IF NOT EXISTS {0} ({1})"
                            .format(table, ','.join('\"' + str(column) +
                                                    '\"' for column in
                                                    columns)))

    def insert(self, table, values):
        self.cursor.execute("INSERT INTO {0} VALUES ({1})"
                            .format(table, ','.join('\"' + str(x) + '\"'
                                                    for x in values)))
        self.connection.commit()

    def insert_unique(self, table, values):
        if not self.row_exists(table, values):
            self.insert(table, values)
            return True
        else:
            return False

    def delete_rows(self, table, columns, values):
        wheres = [str(x) + "=\'" + str(y) + "\'" for x, y
                  in zip(columns, values)]
        self.cursor.execute("DELETE FROM {0} WHERE {1}"
                            .format(table, " AND ".join(wheres)))
        self.connection.commit()

    def update(self, table, update_columns, update_values, where_columns,
               where_values):
        updates = [str(x) + "=\'" + str(y) + "\'" for x, y
                   in zip(update_columns, update_values)]
        wheres = [str(x) + "=\'" + str(y) + "\'" for x, y
                  in zip(where_columns, where_values)]
        self.cursor.execute("UPDATE {0} SET {1} WHERE {2}".format(
            table, ", ".join(updates), "AND ".join(wheres)))
        self.connection.commit()

    def sort(self, table, column, order=SortingOrder.ascending):
        self.cursor.execute("SELECT * FROM {0} ORDER BY {1} {2}"
                            .format(table, column, order))
        self.connection.commit()
