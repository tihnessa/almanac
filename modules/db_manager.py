import sqlite3


class DBManager():
    def __init__(self, file):
        self.database = file

    def execute_sql(self, query, parameters):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            query_result = cursor.execute(query, parameters).fetchall()
        return query_result

    def create_database(self, sql_file):
        pass

    def select_data(self, table, columns):
        sql_query = 'SELECT '
        for column in columns:
            sql_query += f'{column}, '
        sql_query = sql_query[:-2] + f' FROM {table};'
        return self.execute_sql(sql_query, [])
