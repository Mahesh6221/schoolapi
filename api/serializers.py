from rest_framework import serializers
from api.models import School, Student

# create serializers here

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = "__all__"  #means i want to include all the fields of School model

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"  