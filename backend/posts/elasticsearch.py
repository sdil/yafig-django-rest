from django.conf import settings
from django_elasticsearch_dsl import Document, Index, fields
from elasticsearch_dsl import analyzer
from .models import Post

# Name of the Elasticsearch index
INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])

# See Elasticsearch Indices API reference for available settings
INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)

@INDEX.doc_type
class PostDocument(Document):
    """Post Elasticsearch document."""

    id = fields.IntegerField(attr='id')

    caption = fields.StringField(
        fields={
            'raw': fields.StringField(analyzer='keyword'),
        }
    )

    tag = fields.StringField(
        attr='tags_indexing',
        analyzer=html_strip,
        fields={
            'raw': fields.StringField(analyzer='keyword', multi=True),
            'suggest': fields.CompletionField(multi=True),
        },
        multi=True
    )

    class Django(object):
        """Inner nested class Django."""

        model = Post  # The model associate with this Document
