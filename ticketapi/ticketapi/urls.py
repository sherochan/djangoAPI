"""ticketapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from django.contrib.auth.models import User
from relationships.models import Relationship
from rest_framework import routers

from relationships.views import RelationshipViewSet,UserViewSet,CommonStudentViewSet, StudentViewSet, NotificationViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'api/users', UserViewSet)

router.register(r'api/register', RelationshipViewSet, base_name = "Relationship")
router.register(r'api/commonstudents',CommonStudentViewSet, base_name = 'commonstudents')
router.register(r'api/suspend', StudentViewSet, base_name = 'Student')
router.register(r'api/retrievefornotifications', NotificationViewSet, base_name = 'notification')


# router.register()

# router.register(r'api/category', CategoryViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework'))
]
