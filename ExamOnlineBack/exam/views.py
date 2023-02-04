from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets, filters
from rest_framework.pagination import PageNumberPagination

from exam.filter import ExamFilter
from exam.models import Exam, Grade, Practice
from exam.serializers import ExamSerializer, GradeSerializer, PracticeSerializer
# Create your views here.
from user.models import Student


class CommonPagination(PageNumberPagination):
    """Test list of test lists"""
    # The number of displayed per page by default
    page_size = 10
    # You can dynamically change the number displayed per page
    page_size_query_param = 'page_size'
    # Page parameter
    page_query_param = 'page'
    # How many pages can be displayed at most
    max_page_size = 10


class ExamListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """Test list page"""
    # Here we must define a default sort, otherwise an error will be reported
    queryset = Exam.objects.all().order_by('id')
    # Serialization
    serializer_class = ExamSerializer
    # Pagination
    pagination_class = CommonPagination
    # Open filter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # Set the class class to customize the class
    filter_class = ExamFilter
    # Search, = name means precise search, or you can use various regular expressions
    search_fields = ('name', 'major')
    # Sort
    ordering_fields = ('id', 'exam_date')

    # Rewritequeryset
    def get_queryset(self):
        # Student ID
        student_id = self.request.query_params.get("student_id")
        student = Student.objects.get(id=student_id)

        if student:
            self.queryset = Exam.objects.filter(clazzs__student=student)
        return self.queryset


class GradeListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Score list"""
    # Here we must define a default sort, otherwise an error will be reported
    queryset = Grade.objects.all().order_by('-create_time')
    #Serialization
    serializer_class = GradeSerializer
    # Pagination
    pagination_class = CommonPagination

    # Rewritequeryset
    def get_queryset(self):
        # studentID
        student_id = self.request.query_params.get("student_id")

        if student_id:
            self.queryset = Grade.objects.filter(student_id=student_id)
        return self.queryset


class PracticeListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Practice list"""
    # data set
    queryset = Practice.objects.all()
    # Serialization
    serializer_class = PracticeSerializer
    # Pagination
    pagination_class = CommonPagination

    def get_queryset(self):
        # Student ID
        student_id = self.request.query_params.get('student_id')
        if student_id:
            self.queryset = Practice.objects.filter(student_id=student_id)
        return self.queryset
