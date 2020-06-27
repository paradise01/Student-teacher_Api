from rest_framework import serializers

from classroom.models import ClassNotice, ClassAssignment



class ClassNoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassNotice
        fields = '__all__'


class ClassAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassAssignment
        fields = '__all__'

