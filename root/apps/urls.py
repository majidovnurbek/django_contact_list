from django.urls import path
from apps.views import index,HomeDeleteView
from django.urls import path

urlpatterns = [
    path('', index, name='contact_list'),
    path('delete/<int:pk>', HomeDeleteView.as_view(), name='delete'),]


