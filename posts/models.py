import uuid
from django_cassandra_engine.models import DjangoCassandraModel
from cassandra.cqlengine.models import Model as PythonCassandraModel
from cassandra.cqlengine import columns

# Create your models here.

class Post(DjangoCassandraModel, PythonCassandraModel):
    __keyspace__ = 'example'
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    title = columns.Text()
    body = columns.Text()
    created_at = columns.DateTime()
    updated_at = columns.DateTime()