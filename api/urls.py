from django.urls import path
from .views import *

app_name='api'

urlpatterns = [
path('signup/', SignUpAPIView.as_view(), name='signup') 
]
