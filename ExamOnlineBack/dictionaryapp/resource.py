from import_export import resources
from dictionaryapp.models import Example, Grammar, JaVi, Kanji, ViJa

class ExampleResource(resources.ModelResource):
    class Meta:
        model = Example
        fields = ('id', 'ref_id', 'mean', 'trans', 'content')

class GrammarResource(resources.ModelResource):
    class Meta:
        model = Grammar
        fields = ('id', 'mean', 'category', 'define', 'level', 'summary', 'favorite', 'remember', 'note')


class JaViResource(resources.ModelResource):
    class Meta:
        model = JaVi
        fields = ('id', 'mean', 'opposite', 'phonetic', 'pronunciation', 'related', 'seq', 'synsets', 'word', 'favorite')
        
        
class KanjiResource(resources.ModelResource):
    class Meta:
        model = Kanji
        fields = ['id', 'kanji', 'mean', 'level', 'on', 'kun', 'svg', 'detail', 'short', 'frequenty', 'components', 'stroke_count', 'components_detail', 'examples', 'favorite', 'remember']

class ViJaResource(resources.ModelResource):
    model = ViJa
    fields = ['id', 'word', 'kind', 'mean', 'favorite']