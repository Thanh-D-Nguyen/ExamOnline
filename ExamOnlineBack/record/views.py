from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets

from question.models import Program
from record.models import ChoiceRecord, FillRecord, JudgeRecord, ProgramRecord
from record.serializers import ChoiceRecordSerializer, FillRecordSerializer, JudgeRecordSerializer, \
    ProgramRecordSerializer


class ChoiceRecordListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Selected questions practice record"""
    # data set
    queryset = ChoiceRecord.objects.all()
    # Serialization
    serializer_class = ChoiceRecordSerializer

    def get_queryset(self):
        # Simulation exercise ID
        practice_id = self.request.query_params.get('practice_id')
        if practice_id:
            self.queryset = ChoiceRecord.objects.filter(practice_id=practice_id)
        return self.queryset


class FillRecordListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Fill in the blank questions practice record"""
    # data set
    queryset = FillRecord.objects.all()
    # Serialization
    serializer_class = FillRecordSerializer

    def get_queryset(self):
        # Simulation exercise ID
        practice_id = self.request.query_params.get('practice_id')
        if practice_id:
            self.queryset = FillRecord.objects.filter(practice_id=practice_id)
        return self.queryset


class JudgeRecordListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Selected questions practice record"""
    # data set
    queryset = JudgeRecord.objects.all()
    # Serialization
    serializer_class = JudgeRecordSerializer

    def get_queryset(self):
        # Simulation exercise ID
        practice_id = self.request.query_params.get('practice_id')
        if practice_id:
            self.queryset = JudgeRecord.objects.filter(practice_id=practice_id)
        return self.queryset


class ProgramRecordListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Programming questions practice record"""
    # data set
    queryset = ProgramRecord.objects.all()
    # Serialization
    serializer_class = ProgramRecordSerializer

    def get_queryset(self):
        # Simulation exercise ID
        practice_id = self.request.query_params.get('practice_id')
        if practice_id:
            self.queryset = ProgramRecord.objects.filter(practice_id=practice_id)
        return self.queryset
