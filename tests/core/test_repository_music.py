import unittest
from app.connection.ConnectionSQLite import ConnectionSQLite
from app.DependencyContainer import DependencyContainer
from app.repository.RepositoryMusic import RepositoryMusic


class TestRepositorySqlite(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.app = DependencyContainer()
        self.config = self.app.config_conf()  # ConfigurationCONF
        self.sql_connection = ConnectionSQLite(self.config, "CONNECTION_SQLITE_TEST")
        self.music_repository = RepositoryMusic(self.sql_connection)

    def test_get_one_artist_music_repo(self):
        result = self.music_repository.read("select * from Album limit 1")
        album_id, title, artist_id = result.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(album_id, 1)
        self.assertEqual(title, "For Those About To Rock We Salute You")
        self.assertEqual(artist_id, 1)


if __name__ == '__main__':
    unittest.main()
