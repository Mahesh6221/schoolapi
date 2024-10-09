from django.shortcuts import render
from rest_framework import viewsets
from api.models import School, Student
from api.serializers import SchoolSerializer, StudentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    @action(detail=True,methods=['get'])
    def students(self,request,pk=None):
        try:
            school = School.objects.get(pk=pk)
            studs = Student.objects.filter(school=school)
            stud_serializer = StudentSerializer(studs,many=True,context={'request':request})
            return Response(stud_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'student not found'
            })

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer