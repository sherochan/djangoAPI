from rest_framework import serializers

from django.contrib.auth import get_user_model
from relationships.models import Student, Relationship
User = get_user_model()

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email')

# Serializers define the API representation.

class StudentSerializer(serializers.ModelSerializer):
    # tickets = serializers.StringRelatedField(many = True)
    # def __init__(self, *args, **kwargs):
    #     many = kwargs.pop('many', True)
    #     super(StudentSerializer, self).__init__(many=many, *args, **kwargs)
    email = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(),write_only = True)
    student_email = serializers.CharField(source = "email",read_only = True)
    # email = serializers.SlugRelatedField(queryset= Student.objects.all(),slug_field = 'email')
    class Meta:
        model = Student
        fields = ('email','student_email','suspended')
        extra_kwargs = {
            'suspended': {'write_only':True}
        }
        # read_only_fields = ('email')

    def create(self, validated_data):
        # print(validated_data)
        # print(validated_data.get('email',None))
        # one_entry = Student.objects.get(pk =pk)
        # print(one_entry)
        answer,created = Student.objects.update_or_create(
            email = validated_data.get('email',None),

            defaults = {'suspended': validated_data.get('suspended',None)}

        )
        return answer

class RelationshipSerializer(serializers.ModelSerializer):
    teacher_email = serializers.CharField(source = "teacher_user.email", read_only = True)
    # students_all = serializers.SlugRelatedField(queryset = Student.objects.all() ,slug_field = "email",many = True)
    # # students_all = StudentSerializer(many = True)
    # teacher_email = serializers.SlugRelatedField(queryset=Teacher.objects.all(),slug_field = "email")
    # # students_all = StudentSerializer(many=True,read_only = True)
    students = serializers.SlugRelatedField(many = True, slug_field="email", queryset = Student.objects.all())
    # def __init__(self, *args, **kwargs):
    #     many = kwargs.pop('many', True)
    #     super(TicketSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = Relationship
        # fields = ('teacher_email','students')
        fields = ('teacher_email','teacher_user','students')

        extra_kwargs = {
            'teacher_user': {'write_only':True}
        }

class CommonStudentSerializer(serializers.Serializer):
    # teacher_email = serializers.CharField(source = "teacher_user.email", read_only = True)
    # students_all = serializers.SlugRelatedField(queryset = Student.objects.all() ,slug_field = "email",many = True)
    # # students_all = StudentSerializer(many = True)
    # teacher_email = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field = "email")
    # # students_all = StudentSerializer(many=True,read_only = True)
    # students = serializers.SlugRelatedField(many = True, slug_field="students__email", read_only = True)
    # def __init__(self, *args, **kwargs):
    #     many = kwargs.pop('many', True)
    #     super(TicketSerializer, self).__init__(many=many, *args, **kwargs)
    students__email = serializers.EmailField(read_only = True)
    # class Meta:
    #     model = Student
    #     fields = ('students',)
    #     # read_only_fields = ('teacher_email','students')

    # # students = serializers.SlugRelatedField(many = True, slug_field="email", queryset = Student.objects.all())
    # students = serializers.SlugRelatedField(many = True, slug_field="email", queryset = Student.objects.all())
    # class Meta:
    #     model = Ticket
    #     fields = ('students')

class NotificationSerializer(serializers.Serializer):
    recipients = serializers.EmailField(read_only = True)
    teacher_email = serializers.EmailField(write_only = True)
    notification = serializers.CharField(write_only = True)
