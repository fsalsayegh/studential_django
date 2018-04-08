from rest_framework.generics import CreateAPIView,ListAPIView
from .serializers import SignUpSerializer , MajorSerializer,CourseSerializer ,Profile_Detail
from django.contrib.auth import get_user_model
from .models import *
from django.http import JsonResponse
from django.core import serializers

User = get_user_model()

class SignUpAPIView(CreateAPIView):
	queryset = User.objects.all()
	serializer_class = SignUpSerializer


class MajorAPIView(ListAPIView):
	queryset = Major.objects.all()
	serializer_class = MajorSerializer 

class CourseAPIView(ListAPIView):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer

class Profile_DetailAPIView(ListAPIView):
	queryset = User.objects.all()
	serializer_class = Profile_Detail



	

