from django.urls import path
from apps.views import index
from django.urls import path


urlpatterns = [
    path('', index, name='contact_list'),
]


