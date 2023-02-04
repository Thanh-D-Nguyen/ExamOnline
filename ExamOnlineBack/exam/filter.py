import django_filters

from exam.models import Exam


class ExamFilter(django_filters.rest_framework.FilterSet):
    """Class of test filtering"""
    # Two parameters, field_name is a field to be filtered, lookup is an execution behavior
    exam_date_min = django_filters.DateFilter(field_name='exam_date', lookup_expr='gte')
    exam_date_max = django_filters.DateFilter(field_name="exam_date", lookup_expr='lte')

    class Meta:
        model = Exam
        fields = ['exam_date_min', 'exam_date_max']
