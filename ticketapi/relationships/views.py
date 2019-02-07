from django.views.generic import ListView, CreateView, UpdateView ## new
from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, generics
from ticketapi.serializers import UserSerializer,StudentSerializer, RelationshipSerializer, CommonStudentSerializer,NotificationSerializer
from django.contrib.auth import get_user_model
from relationships.models import Student, Relationship
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated ## for authentication purposes
import re
User = get_user_model()

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RelationshipViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer

class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



class CommonStudentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    # queryset = Ticket.objects.all()
    serializer_class = CommonStudentSerializer
    def get_queryset(self):
        queryset = Relationship.objects.all()
        temp = self.request.query_params.get('teacher_email',None)
        if temp is not None:
            queryset = queryset.filter(teacher_user__email = temp)
            # print(queryset.exclude(students__email__isnull = True))
            student_email_dct = {'students__email':[]}
            for student_email in queryset.exclude(students__email__isnull = True).values_list("students__email"):
                if student_email[0] not in student_email_dct['students__email']:
                    student_email_dct['students__email'].append(student_email[0])
            email_1 = student_email_dct
            # print(email_1)
            email = list(queryset.exclude(students__email__isnull = True).values("students__email"))
            # print(email)
            ################## for now the view for the students do not match the user requirement #######################
            results = CommonStudentSerializer([email_1],many = True).data
        return results
        # return queryset


class NotificationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Relationship.objects.all()
    serializer_class = NotificationSerializer

    def create(self, request,*args,**kwargs):
        ## Extracting all Ticket instance in the database
        queryset_ticket = Relationship.objects.all()
        ## Extracting all Student instance in the database
        queryset_student = Student.objects.all()
        ## Filtering the students out if they are suspended and storing it into a set
        all_enrolled_students_set = set(queryset_student.values_list("email",flat=True).distinct())
        queryset_student_not_suspended = queryset_student.filter(suspended = False)
        student_not_suspended_set = set(queryset_student_not_suspended.values_list("email",flat=True).distinct())

        ## Getting the post data - Teacher email and notification and checking if valid : meaning it fulfils the field it is supposed to be
        write_serializer = NotificationSerializer(data=request.data)
        write_serializer.is_valid(raise_exception = True)

        ## Extracting out the notification in string
        notification_str = write_serializer.validated_data.get('notification')

        ## extracting the emails
        student_emails_in_notification_set = set(re.findall(r'@([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)',notification_str))
        ## Check if these students exist in the database
        is_valid_student = True
        not_valid_student_lst = []
        for student_email_object in list(student_emails_in_notification_set ):
            if student_email_object not in all_enrolled_students_set:
                is_valid_student = False
                not_valid_student_lst.append(student_email_object)
        if not is_valid_student:
            error_message = "no such student(s): " + str(not_valid_student_lst)
            return JsonResponse({'errorMessage':error_message})

        ## all valid students and now to check if the students are suspended or not
        student_emails_in_notification_set_not_suspended = student_emails_in_notification_set & student_not_suspended_set

        ## Extracting out the entered teacher email
        teacher_email_temp = write_serializer.validated_data.get('teacher_email')
        if teacher_email_temp is not None:
            ## filter by the teacher's email first
            queryset_ticket_1 = queryset_ticket.filter(teacher_user__email = teacher_email_temp)
            ## Check if this teacher is valid
            if len(set(queryset_ticket_1.values_list('teacher_user__email',flat = True).distinct())) == 0:
                return JsonResponse({'errorMessage':'no such teacher'})
            ## Removing those empty student email field in this ticket object through the linking between the dbs
            teacher_students_set = set(queryset_ticket_1.exclude(students__email__isnull = True).values_list("students__email",flat = True).distinct())

            ## Extractng the students under this teacher and not suspended
            intersected_students = teacher_students_set & student_not_suspended_set

            ## union of the students under this teacher and not suspended AND students mentioned in the notification
            final_students_union = intersected_students | student_emails_in_notification_set_not_suspended

            ## storing it into dict class for now
            final_answer = {"recipients":list(final_students_union)}

            read_serializer = NotificationSerializer([final_answer],many = True).data
            return Response(read_serializer)
        else:
            ## to capture the other case of teacher not validated ( usually it would have been caught earlier on)
            return JsonResponse({'errorMessage':'Teacher field is none'})

    def get_queryset(self):
        queryset = Student.objects.all()
        print(self.request.data)
        queryset = queryset.filter(suspended = False)
        recipient_email_dct = {'recipients':[]}
        for student_email in queryset.values_list("email"):
            if student_email[0] not in recipient_email_dct['recipients']:
                recipient_email_dct['recipients'].append(student_email[0])
        print(recipient_email_dct)
        return NotificationSerializer([recipient_email_dct],many = True).data
