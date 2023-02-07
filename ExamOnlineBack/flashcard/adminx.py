import xadmin
from xadmin.views import CommAdminView, BaseAdminView
from flashcard.models import Card, Desk

class CardAdmin(object):
    list_display = ['id', 'front', 'back', 'image', 'video_link']
    list_per_page = 10

class DeskAdmin(object):
    list_display = ['id', 'name', 'image', 'descriotion', 'cards']
    list_per_page = 10
    style_fields = {'cards': 'm2m_transfer'}

xadmin.site.register(Card, CardAdmin)
xadmin.site.register(Desk, DeskAdmin)