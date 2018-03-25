from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Major , Course

User = get_user_model()


# class MajorSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Major
# 		fields = ['name']

# class CourseSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Course
# 		fields = ['name']


class SignUpSerializer(serializers.ModelSerializer):
	password = serializers.CharField(style={"input_type":"password"}, write_only=True)
	# major = serializers.SerializerMethodField()
	# course = serializers.SerializerMethodField()
	# course = serializers.MultipleChoiceField(choices=['Operating System', 'Nano', 'physics'])
	# course = serializers.SlugRelatedField(slug_field='course', read_only=True, many=True)
	# major = serializers.SlugRelatedField(read_only=True, slug_field='major')

	class Meta:
		model = User
		fields = ['username' , 'password' ,'email','major','course' ]
		
	# def get_major(self , obj):
	# 	return obj.name

	# def get_course(self , obj):
	# 	return obj.name			

	def create(self, validated_data):
		username = validated_data['username']
		password = validated_data['password']
		email = validated_data['email']
		major = validated_data['major']
		course = validated_data['course']
		new_user = User(username=username ,email=email , major=major) #take the name in the input field and add it to the database username field 
		new_user.set_password(password)
		new_user.save()
		new_user.course.set(course)
		new_user.save()
		return validated_data




		