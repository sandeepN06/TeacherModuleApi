# from django.conf.urls import url
from django.urls import path, include
from .views import (
    UserModelApiView,
)

urlpatterns = [
    path('api', UserModelApiView.as_view()),
]