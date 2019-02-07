from rest_framework import serializers

from django.contrib.auth import get_user_model
from relationships.models import Student, Relationship
User = get_user_model()

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email')

class StudentSerializer(serializers.ModelSerializer):
    email = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(),write_only = True)
    student_email = serializers.CharField(source = "email",read_only = True)
    # email = serializers.SlugRelatedField(queryset= Student.objects.all(),slug_field = 'email')
    class Meta:
        model = Student
        fields = ('email','student_email','suspended')
        extra_kwargs = {
            'suspended': {'write_only':True}
        }

    def create(self, validated_data):
        answer,created = Student.objects.update_or_create(
            email = validated_data.get('email',None),
            defaults = {'suspended': validated_data.get('suspended',None)}
        )
        return answer

class RelationshipSerializer(serializers.ModelSerializer):
    ## for the view on ../api/register
    teacher_email = serializers.CharField(source = "teacher_user.email", read_only = True)
    students = serializers.SlugRelatedField(many = True, slug_field="email", queryset = Student.objects.all())

    class Meta:
        model = Relationship
        fields = ('teacher_email','teacher_user','students')

        extra_kwargs = {
            'teacher_user': {'write_only':True}
        }

class CommonStudentSerializer(serializers.Serializer):
    students__email = serializers.EmailField(read_only = True)


class NotificationSerializer(serializers.Serializer):
    recipients = serializers.EmailField(read_only = True)
    teacher_email = serializers.EmailField(write_only = True)
    notification = serializers.CharField(write_only = True)
