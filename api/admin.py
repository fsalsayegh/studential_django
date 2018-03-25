from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Course, Major


# class CustomUserAdmin(UserAdmin):
# 	list_display = ['username','course', 'major']
# 	class Meta:
# 		model = Users

class MyUserAdmin(UserAdmin):

	    model = User

	    fieldsets = UserAdmin.fieldsets + (
	            (None, {'fields': ('course','major')}),
	    )


admin.site.register(User, MyUserAdmin)
admin.site.register(Course)
admin.site.register(Major)

