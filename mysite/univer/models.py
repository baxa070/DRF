from django.db import models


class University(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Faculties(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Students(models.Model):

    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100, blank=False, null=False, choices=(("Male", "male"), ("Female", "female")))
    university = models.ForeignKey(University, blank=False, null=True, on_delete=models.SET_NULL)
    faculties = models.ForeignKey(Faculties, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.full_name

