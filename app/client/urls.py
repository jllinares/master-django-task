from django.urls import(
    path,
    include
)

from rest_framework.routers import DefaultRouter
from client import views

router = DefaultRouter()

#Verbos Rest
#/client
router.register('client', views.ClientViewSet)

app_name = 'client'

urlpatterns = [
    path('', include(router.urls))
]
