from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton
from app.configuration.ConfigurationCONF import ConfigurationCONF
from app.configuration.ConfigurationENV import ConfigurationENV
from app.connection.ConnectionSQLite import ConnectionSQLite
from app.repository.RepositoryMusic import RepositoryMusic
from app.service.ServiceMusic import ServiceMusic
from app.service.ServiceSecurity import ServiceSecurity
from app.serialize.SerializeFactory import SerializeFactory
from app.log.LogLocal import LogLocal


class DependencyContainer(DeclarativeContainer):

    config_conf = Singleton(ConfigurationCONF)

    config_env = Singleton(ConfigurationENV)

    log_local = Singleton(LogLocal, config_env)

    connection = Singleton(ConnectionSQLite, config_conf, "CONNECTION_SQLITE")

    music_repository = Singleton(RepositoryMusic, connection)

    serialize_factory = Singleton(SerializeFactory)

    # Frontend services
    service_music = Singleton(ServiceMusic, config_conf, music_repository)

    # Backend services
    service_security = Singleton(ServiceSecurity, log_local)




