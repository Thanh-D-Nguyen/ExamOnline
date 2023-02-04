import subprocess

from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from question.models import Choice, Fill, Judge, Program
from question.serializers import ChoiceSerializer, FillSerializer, JudgeSerializer, ProgramSerializer


# Create your views here.


class ChoiceListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """Selection question list page"""
    # It is necessary to define a default sort here, otherwise an error will be reported
    queryset = Choice.objects.all().order_by('id')[:0]
    # Serialization
    serializer_class = ChoiceSerializer

    # 重写queryset
    def get_queryset(self):
        # Quantity
        choice_number = int(self.request.query_params.get("choice_number"))
        level = int(self.request.query_params.get("level", 1))

        if choice_number:
            self.queryset = Choice.objects.all().filter(level=level).order_by('?')[:choice_number]
        return self.queryset


class FillListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """Fill in the blank question list"""
    # It is necessary to define a default sort here, otherwise an error will be reported
    queryset = Fill.objects.all().order_by('id')[:0]
    # Serialization
    serializer_class = FillSerializer

    # Rewrite queryset
    def get_queryset(self):
        # Quantity
        fill_number = int(self.request.query_params.get("fill_number"))
        level = int(self.request.query_params.get("level", 1))

        if fill_number:
            self.queryset = Fill.objects.all().filter(level=level).order_by('?')[:fill_number]
        return self.queryset


class JudgeListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """Judgment question list page"""
    # It is necessary to define a default sort here, otherwise an error will be reported
    queryset = Judge.objects.all().order_by('?')[:0]
    # Serialization
    serializer_class = JudgeSerializer

    # Rewrite queryset
    def get_queryset(self):
        # Quantity
        judge_number = int(self.request.query_params.get("judge_number"))
        level = int(self.request.query_params.get("level", 1))

        if judge_number:
            self.queryset = Judge.objects.all().filter(level=level).order_by('?')[:judge_number]
        return self.queryset


class ProgramListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """Programming Question Table Page"""
    # Here is a default sort, otherwise an error will be reported
    queryset = Program.objects.all().order_by('?')[:0]
    # Serialization
    serializer_class = ProgramSerializer

    #Rewrite queryset
    def get_queryset(self):
        # Quantity
        program_number = int(self.request.query_params.get("program_number"))
        level = int(self.request.query_params.get("level", 1))

        if program_number:
            self.queryset = Program.objects.all().filter(level=level).order_by('?')[:program_number]
        return self.queryset


class CheckProgramApi(APIView):
    """Test preparation questions"""

    def post(self, request):
        # Get the dictionary data submitted by POST
        json_body = request.data

        # The ANSWER to be executed is written into the python file
        with open(r'.\question\Solution.py', 'w') as f:
            if json_body['answer']:
                f.write(json_body['answer'])
            else:
                f.write('')
            f.flush()
        # initialization subprocess
        obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               universal_newlines=True)
        try:
            obj.stdin.write(json_body['program']['test_case'])
            obj.stdin.close()

            cmd_out = obj.stdout.read()
            obj.stdout.close()
            cmd_error = obj.stderr.read()
            obj.stderr.close()
            # print(cmd_out)
            # print(cmd_error)  # There is no abnormality in the program, only the output empty line
        except Exception as e:
            return Response({'message': 'Program run errors'})
        finally:
            if 'OK' in cmd_error:
                return Response({'message': 'pass'})
            return Response({'message': cmd_error})
