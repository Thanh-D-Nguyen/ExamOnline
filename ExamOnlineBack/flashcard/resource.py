from import_export import resources
from flashcard.models import Card

class CardResource(resources.ModelResource):
    class Meta:
        model = Card
        fields = ('id', 'front', 'back', 'description', 'image', 'video_link')