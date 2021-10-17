from django_elasticsearch_dsl import Document, Index
from .models import Video
videos =Index('videos')

@videos.doc_type
class VideoDocument(Document):
    class Meta:
        model = Video
        fields = [
            'id',
            'title',
            'description',
            'thumbnail',
            'video_url',
            'created_at',
            'updated_at',
        ]