import pathlib
from decouple import config
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.cqlengine.connection import register_connection, set_default_connection

ASTRA_DB_CLIENT_ID = config('ASTRA_DB_CLIENT_ID', cast=str)
ASTRA_DB_CLIENT_SECRET = config('ASTRA_DB_CLIENT_SECRET', cast=str)

IGNORED_DIR = pathlib.Path(__file__).parent.parent / 'ignored'

CONNECTION_BUNDLE = IGNORED_DIR / 'connect.zip'

cloud_config= {
    'secure_connect_bundle': str(CONNECTION_BUNDLE)
}

def get_cluster():
    auth_provider = PlainTextAuthProvider(
        ASTRA_DB_CLIENT_ID, ASTRA_DB_CLIENT_SECRET
    )
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    return cluster

def get_session():
    cluster = get_cluster()
    session = cluster.connect()
    register_connection(str(session), session=session)
    set_default_connection(str(session))
    return session