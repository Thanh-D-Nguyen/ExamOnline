import xadmin
from django.contrib.auth.models import User
from xadmin.plugins.auth import UserAdmin

from exam.models import Exam, Grade, Paper
from xadmin.views import CommAdminView, BaseAdminView


# Register your models here.

class GlobalSetting(object):
    # Global Setting
    site_title = 'Python online test management system'
    site_footer = 'Design by Pengshengfu'
    #Menu default contraction
    # menu_style = 'accordion'


class BaseSetting(object):
    # Start the theme manager
    enable_themes = True
    # Use theme
    use_bootswatch = True


class ExamAdmin(object):
    list_display = ['id', 'name', 'exam_date', 'total_time', 'paper', 'major', 'tips', 'clazzs']
    list_filter = ['major', 'exam_date']
    search_fields = ['id', 'name']
    list_display_links = ['name']
    list_per_page = 10
    # list_editable = ['name']
    model_icon = 'fa fa-book'
    relfield_style = 'fk-ajax'
    #Multi -to -the -style field support filtering
    filter_horizontal = ('clazzs',)
    #Modify the multi -shuttle frame style
    style_fields = {'clazzs': 'm2m_transfer'}


class PaperAdmin(object):
    list_display = ['id', 'name', 'score', 'choice_number', 'fill_number', 'judge_number', 'program_number', 'level']
    list_filter = ['level']
    search_fields = ['id', 'name']
    list_display_links = ['name']
    list_per_page = 10
    # list_editable = ['name']
    model_icon = 'fa fa-file-text'


class GradeAdmin(object):
    list_display = ['id', 'exam', 'student', 'score', 'create_time', 'update_time']
    list_filter = ['exam', 'student', 'create_time', 'update_time']
    search_fields = ['exam', 'student']
    list_display_links = ['score']
    list_per_page = 10
    # list_editable = ['id', 'score']
    model_icon = 'fa fa-bar-chart'

    data_charts = {
        'grade_charts1': {
            'title': 'Test score curve',
            'x-field': 'create_time',
            'y-field': ('score',),
            'order': ('id',)
        },
        'grade_charts2': {
            'title': 'Test results column -like diagram',
            'x-field': 'score',
            'y-field': ('score',),
            'order': ('id',),
            'option': {
                "series": {"bars": {"align": "center", "barWidth": 0.5, "show": True}},
                "xaxis": {"aggregate": "count", "mode": "score"}
            }
        }
    }


xadmin.site.register(CommAdminView, GlobalSetting)
xadmin.site.register(BaseAdminView, BaseSetting)
xadmin.site.register(Exam, ExamAdmin)
xadmin.site.register(Paper, PaperAdmin)
xadmin.site.register(Grade, GradeAdmin)

