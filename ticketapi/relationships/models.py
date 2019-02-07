from django.db import models
import uuid
from django.contrib.auth import get_user_model
User = get_user_model()

class Relationship(models.Model):
    ## teacher and student Relationship
    # student_email = models.ManyToManyField(Student, related_name = "students_all", on_delete = models.CASCADE) ## student unique identifier: Foreign Key
    # teacher_email = models.ForeignKey(Teacher, on_delete = models.CASCADE)  ## teacher unique identifier: Foreign key
    teacher_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):

        super(Relationship, self).save(*args, **kwargs) # Call the real   save() method

    class Meta:
        ordering = ["-created"]


class Student(models.Model):
    email = models.EmailField(max_length = 254, unique = True)
    created = models.DateTimeField(auto_now=True)
    ticket = models.ManyToManyField(Relationship,related_name = "students")
    suspended = models.BooleanField(default = False)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.email
