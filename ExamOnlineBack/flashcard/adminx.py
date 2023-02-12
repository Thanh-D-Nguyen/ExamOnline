import xadmin
from xadmin.views import CommAdminView, BaseAdminView
from flashcard.models import Card, Desk
from flashcard.resource import CardResource

class CardAdmin(object):
    list_display = ['id', 'front', 'back', 'description', 'image', 'video_link']
    list_per_page = 10
    import_export_args = {'import_resource_class': CardResource}


class DeskAdmin(object):
    list_display = ['id', 'name', 'image', 'description', 'cards']
    list_per_page = 10
    style_fields = {'cards': 'm2m_transfer'}

xadmin.site.register(Card, CardAdmin)
xadmin.site.register(Desk, DeskAdmin)