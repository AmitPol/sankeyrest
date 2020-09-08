from rest_framework import serializers
from .models import Emp


class HR_Serial(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = '__all__'
        read_only_fields = ['id', 'created_date']


class Emp_Serial(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = ['id', 'name', 'email', 'username', 'role', 'password']

# class IdeaListSerializer(serializers.ListSerializer):
#     def create(self, validated_data):
#         ideas = [Emp(**item) for item in validated_data]
#         return Emp.objects.bulk_create(ideas)
