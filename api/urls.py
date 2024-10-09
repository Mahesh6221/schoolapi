from django.urls import include, path
from api.views import SchoolViewSet, StudentViewSet
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'schools',SchoolViewSet)
router.register(r'students',StudentViewSet)


urlpatterns = [
    path('',include(router.urls))
]

