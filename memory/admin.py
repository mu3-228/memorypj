# memory/admin.py
from django.contrib import admin
from .models import Folder, Memory

admin.site.register(Folder)
admin.site.register(Memory)
# Register your models here.
