from app.repository.RepositoryAbstract import RepositoryAbstract
from app.connection.ConnectionAbstract import ConnectionAbstract


class RepositoryBreaze(RepositoryAbstract):

    def __init__(self, connection: ConnectionAbstract):
        self.sql = connection

    def create(self, query: str):
        try:
            with self.sql.get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute(query)
        except Exception as ex:
            raise Exception(f'Error on creating table or inserting values with this query: ') + query

    def read_with_headers(self, query: str):
        with self.sql.get_connection() as connection:
            cursor = connection.cursor()
            result = cursor.execute(query).fetchall()
            headers = list(map(lambda attr: attr[0], cursor.description))
            results = [{header: row[i] for i, header in enumerate(headers)} for row in result]

        return results

    def read(self, query: str):
        with self.sql.get_connection() as connection:
            cursor = connection.cursor()
            return cursor.execute(query)

    def update(self):
        pass

    def delete(self):
        pass

