from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import Student, Clazz
from user.serializers import StudentSerializer, UserDetailSerializer, ClazzSerializer


# Create your views here.
class CustomBackend(ModelBackend):
    """
    Custom user verification
    """

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


def jwt_response_payload_handler(token, user=None, request=None):
    """
    After setting jwt login, return token and user information
    """
    student = Student.objects.get(user=user)
    return {
        'token': token,
        'user': UserDetailSerializer(user, context={'request': request}).data,
        'student': StudentSerializer(student, context={'request': request}).data
    }


class RegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    User registration
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    def create(self, request, *args, **kwargs):
        user = User.objects.filter(username=request.data['username'])
        if user:
            return Response({'msg': 'Username already exists'}, status=status.HTTP_201_CREATED)
        user_detail = UserDetailSerializer(data=request.data)
        if user_detail.is_valid():
            user_detail.save()
        user = User.objects.get(username=request.data['username'])
        # Code convert to ciphertext storage
        user.password = make_password(user.password)
        user.save()
        student = Student(user=user, name=request.data['name'])
        if student:
            student.save()
        return Response(user_detail.errors)


class UpdatePwdApi(APIView):
    """
    Modify the user password
    """

    def patch(self, request):
        # Get parameters
        old_pwd = request.data['oldpwd']
        new_pwd = request.data['newpwd']
        user_id = request.data['userid']
        # Obtain a request user
        user = User.objects.get(id=user_id)
        # Check whether the original password is correct
        if user.check_password(old_pwd):
            user.set_password(new_pwd)
            user.save()
        else:
            return Response(data={'msg': 'fail'}, status=status.HTTP_200_OK)
        # Return data
        return Response(data={'msg': 'success'}, status=status.HTTP_200_OK)


class StudentViewSet(viewsets.ModelViewSet):
    """
    student information
    """
    # Query set
    queryset = Student.objects.all().order_by('id')
    # Serialization
    serializer_class = StudentSerializer


class ClazzListViewSet(viewsets.ModelViewSet):
    """
    Class information
    """
    # Query set
    queryset = Clazz.objects.all().order_by('id')
    # Serialization
    serializer_class = ClazzSerializer
