from rest_framework.generics import CreateAPIView,ListAPIView
from .serializers import SignUpSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpAPIView(CreateAPIView):
	queryset = User.objects.all()
	serializer_class = SignUpSerializer





