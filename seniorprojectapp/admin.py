from django.contrib import admin

# Register your models here.

from .models import User, Survey

admin.site.register(User)
#admin.site.register(Register)
admin.site.register(Survey)