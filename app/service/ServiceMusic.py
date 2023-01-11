from pathlib import Path
import os
from app.repository.RepositoryAbstract import RepositoryAbstract
from app.configuration.ConfigurationAbstract import ConfigurationAbstract
from app.domain.Artist import Artist
from app.domain.Album import Album

BASE_DIR = Path(__file__).resolve().parent.parent.parent


def __create_query__(file_query, parameter_id):

    with open(file_query, 'r') as query:
        sql_script = query.read() + (str(parameter_id))
    return sql_script


class ServiceMusic:

    def __init__(self, config: ConfigurationAbstract, repository: RepositoryAbstract):
        self.repository = repository
        self.static_folder = config.get("STATIC", "path")

    def get_artist_by_id(self, artist_id: int):
        file_path = "select_artist_by_id.sql"
        file_query = os.path.join(BASE_DIR, self.static_folder, file_path)

        query = __create_query__(file_query, artist_id)

        result = self.repository.read(query)

        artist = Artist(name=result.fetchone())
        return artist

    def get_album_by_id(self, album_id: int):
        file_path = "select_album_by_id.sql"
        file_query = os.path.join(BASE_DIR, self.static_folder, file_path)

        query = __create_query__(file_query, album_id)

        result = self.repository.read(query)

        album = Album(title=result.fetchone())
        return album
