import sqlite3 as sql


class Database:

    def __init__(self, name):
        self.name = name
        self.connect()

    def __del__(self):
        self.close()

    def connect(self):
        self.connection = sql.connect(self.name + ".db")
        self.connection.row_factory = sql.Row
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def createTable(self, table, columns):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS {0} ({1})"
                            .format(table, ','.join('\"'+ str(x) + '\"' for x in columns)))

    def insert(self, table, values):
        self.cursor.execute("INSERT INTO {0} VALUES ({1})"
                            .format(table, ','.join('\"' + str(x) + '\"'
                                                    for x in values)))
        self.connection.commit()

    def delete(self, table, columns, values):
        wheres = [str(x) + "=\'" + str(y) + "\'" for x, y
                  in zip(columns, values)]
        self.cursor.execute("DELETE FROM {0} WHERE {1}"
                            .format(table, " AND ".join(wheres)))
        self.connection.commit()

    def allFromTable(self, table):
        self.cursor.execute("SELECT * FROM {0}".format(table))

    def next(self):
        return self.cursor.fetchone()

    def nextFromTable(self, table):
        self.allFromTable(table)
        return self.cursor.fetchone()

    def update(self, table, updateColumns, updateValues, whereColumns,
               whereValues):
        updates = [str(x) + "=\'" + str(y) + "\'" for x, y
                   in zip(updateColumns, updateValues)]
        wheres = [str(x) + "=\'" + str(y) + "\'" for x, y
                  in zip(whereColumns, whereValues)]
        self.cursor.execute("UPDATE {0} SET {1} WHERE {2}".format(
            table, ", ".join(updates), "AND ".join(wheres)))
        self.connection.commit()

    def sort(self, table, column):
        self.cursor.execute("SELECT * FROM {0} ORDER BY {1}".format(table,
                                                                    column))
        self.connection.commit()

    def numRows(self, table):
        self.cursor.execute("SELECT COUNT(*) AS value FROM {0}".format(table))
        return self.next()['value']
