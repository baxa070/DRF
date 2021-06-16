from contextlib import closing
from django.db import connection
from collections import OrderedDict


def get_university(university_id):
    with closing(connection.cursor())as cursor:
        cursor.execute("""select * from univer_university where id = %s""", [university_id])
        university = dictfetchone(cursor)
        return university


def get_universities():
    with closing(connection.cursor())as cursor:
        cursor.execute("""select * from univer_university""")
        universities = dictfetchall(cursor)
        return universities


def get_faculty(faculties_id):
    with closing(connection.cursor())as cursor:
        cursor.execute("""select * from univer_faculties where id = %s""", [faculties_id])
        faculty = dictfetchone(cursor)
        return faculty


def get_faculties():
    with closing(connection.cursor())as cursor:
        cursor.execute("""select * from univer_faculties""")
        faculties = dictfetchall(cursor)
        return faculties


def get_student(students_id):
    with closing(connection.cursor())as cursor:
        cursor.execute(
            """select univer_students.*, univer_university.id as university_id, univer_university.name as university_name, 
            univer_faculties.id as faculties_id, univer_faculties.name as faculties_name from univer_students left join univer_faculties on univer_students.university_id = univer_university.id
            left join univer_faculties on univer_students.faculties_id = univer_faculties.id 
            where univer_students.id = %s""", [students_id])
        student = dictfetchone(cursor)
        return OrderedDict([
            ('id', student['id']),
            ('full_name', student['full_name']),
            ('age', student['age']),
            ('gender', student['gender']),
            ('university', OrderedDict(
                [
                    ('id', student['university_id']),
                    ('name', student['university_name'])
                ]
            )),
            ('faculties', OrderedDict(
                [
                    ('id', student['faculties_id']),
                    ('name', student['faculties_name'])
                ]
            )),

        ]
        )


def get_students():
    with closing(connection.cursor())as cursor:
        cursor.execute(
            """ select univer_students.*, univer_university.id as university_id, univer_university.name as university_name, 
            univer_faculties.id as faculties_id, univer_faculties.name as faculties_name from univer_students left join univer_university on univer_students.university_id = univer_university.id
            left join univer_faculties on univer_students.faculties_id = univer_faculties.id """)
        students = dictfetchall(cursor)
        return [OrderedDict([
            ('id', student['id']),
            ('name', student['full_name']),
            ('age', student['age']),
            ('gender', student['gender']),
            ('university', OrderedDict(
                [
                    ('id', student['university_id']),
                    ('name', student['university_name'])
                ]
            )),
            ('faculties', OrderedDict(
                [
                    ('id', student['faculties_id']),
                    ('name', student['faculties_name'])
                ]
            )),

        ]
        ) for student in students]



def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))