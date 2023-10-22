from django.urls import path
from . import views

urlpatterns = [
    path('getTopicId/', views.GetTopicId.as_view())
]
