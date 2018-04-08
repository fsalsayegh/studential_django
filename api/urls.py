from django.urls import path
from .views import *

app_name='api'

urlpatterns = [
path('signup/', SignUpAPIView.as_view(), name='signup'),
path('majorlist/', MajorAPIView.as_view(), name='majorlist'),
path('courselist/', CourseAPIView.as_view(), name='courselist'),
path('profiledetail/', Profile_DetailAPIView.as_view(), name='profile_detail')  
]
