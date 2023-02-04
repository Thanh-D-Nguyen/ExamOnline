from django.contrib.auth.models import User
from rest_framework import serializers

from user.models import Student, Clazz


class ClazzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clazz
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    # Cover the outer key field and read only
    # user = UserDetailSerializer()
    # clazz = ClazzSerializer(read_only=True)

    # Only written fields for creation
    clazz_id = serializers.PrimaryKeyRelatedField(queryset=Clazz.objects.all(), source='clazz', write_only=True)

    class Meta:
        model = Student
        fields = '__all__'
