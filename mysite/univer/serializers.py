from rest_framework import serializers
from .models import University, Faculties, Students


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = "__all__"


class FacultiesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Faculties
        fields = "__all__"


class StudentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"