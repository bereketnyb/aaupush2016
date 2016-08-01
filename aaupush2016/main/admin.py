from django.contrib import admin
from .models import *

# Register your models here.
models = [Section, Lecturer, Material, Announcement, Course, Department]

for model in models:
	admin.site.register(model)