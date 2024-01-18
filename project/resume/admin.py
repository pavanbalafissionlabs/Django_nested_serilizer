from django.contrib import admin

# from resume.models import Singer,Song

# Register your models here.

from .models import *
admin.site.register(Resume)
admin.site.register(Projects)
admin.site.register(Location)
