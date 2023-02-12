import xadmin
from dictionaryapp.models import Example, Grammar, JaVi, Kanji, ViJa
from xadmin.views import CommAdminView, BaseAdminView


class ExampleAdmin(object):
    list_display = ['id', 'ref_id', 'content', 'mean', 'trans']
    list_per_page = 10
    
class GrammarAdmin(object):
    list_display = ['id', 'define', 'summary', 'mean', 'note', 'level', 'favorite', 'remember', 'category']
    list_per_page = 10

class JaViAdmin(object):
    list_display = ['id', 'word', 'phonetic', 'mean', 'seq', 'opposite', 'favorite', 'synsets', 'related', 'pronunciation']
    list_per_page = 10

class KanjiAdmin(object):
    list_display = ['id', 'kanji', 'mean', 'level', 'on', 'kun', 'svg', 'detail', 'short', 'frequenty', 'components', 'stroke_count', 'components_detail', 'examples', 'favorite', 'remember']
    list_per_page = 10

class ViJaAdmin(object):
    list_display = ['id', 'word', 'kind', 'mean', 'favorite']
    list_per_page = 10

xadmin.site.register(Example, ExampleAdmin)
xadmin.site.register(Grammar, GrammarAdmin)
xadmin.site.register(JaVi, JaViAdmin)
xadmin.site.register(Kanji, KanjiAdmin)
xadmin.site.register(ViJa, ViJaAdmin)