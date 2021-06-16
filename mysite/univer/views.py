from .models import University, Faculties, Students
from .serializers import UniversitySerializer, FacultiesSerializers, StudentsSerializers
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from .service import get_university, get_universities, get_faculty,  get_faculties, get_student, get_students
from rest_framework.exceptions import NotFound


class UniversityView(GenericAPIView):

    serializer_class = UniversitySerializer
    queryset = University.objects.all()

    def get_object(self, *args, **kwargs):
        try:
            university = University.objects.get(pk=kwargs['pk'])
        except Exception as e:
            raise NotFound
        return university

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, pk=None):
        if pk:
            author = get_university(university_id=pk)
            if not author:
                raise NotFound("Author not found")
            return Response(author, status=status.HTTP_200_OK)
        else:
            universities = get_universities()
            return Response(universities, status=status.HTTP_200_OK)


class FacultiesView(GenericAPIView):

    serializer_class = FacultiesSerializers
    queryset = Faculties.objects.all()

    def get_object(self, *args, **kwargs):
        try:
            faculty = Faculties.objects.get(pk=kwargs['pk'])
        except Exception as e:
            raise NotFound
        return faculty

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, pk=None):
        if pk:
            faculty = get_faculty(faculties_id=pk)
            if not faculty:
                raise NotFound("Author not found")
            return Response(faculty, status=status.HTTP_200_OK)
        else:
            faculties = get_faculties()
            return Response(faculties, status=status.HTTP_200_OK)


class StudentsView(GenericAPIView):

    serializer_class = StudentsSerializers
    queryset = Students.objects.all()

    def get_object(self, *args, **kwargs):
        try:
            student = Students.objects.get(pk=kwargs['pk'])
        except Exception as e:
            raise NotFound
        return student

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, pk=None):
        if pk:
            book = get_student(students_id=pk)
            if not book:
                raise NotFound("book not found")
            return Response(book, status=status.HTTP_200_OK)
        else:
            students = get_students()
            return Response(students, status=status.HTTP_200_OK)



