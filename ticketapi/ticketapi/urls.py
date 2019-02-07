from django.contrib import admin
from django.urls import path, include

# from django.contrib.auth.models import User
from relationships.models import Relationship
from rest_framework import routers

from relationships.views import RelationshipViewSet,CommonStudentViewSet, StudentViewSet, NotificationViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

router.register(r'api/register', RelationshipViewSet, base_name = "Relationship")
router.register(r'api/commonstudents',CommonStudentViewSet, base_name = 'commonstudents')
router.register(r'api/suspend', StudentViewSet, base_name = 'Student')
router.register(r'api/retrievefornotifications', NotificationViewSet, base_name = 'notification')


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework'))
]
