#from rest_framework import stauts
from rest_framework.response import Response
#from rest_framework.decorators import api_view
from rest_framework import viewsets

from classroom.models import User
from classroom.models import ClassNotice, ClassAssignment
from classroom.api.serializers import ClassNoticeSerializer, ClassAssignmentSerializer


class ClassNoticeViewSet(viewsets.ModelViewSet):
    queryset = ClassNotice.objects.all()
    serializer_class = ClassNoticeSerializer


class ClassAssignmentViewSet(viewsets.ModelViewSet):
    queryset = ClassAssignment.objects.all()
    serializer_class = ClassAssignmentSerializer