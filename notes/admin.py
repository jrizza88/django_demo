from django.contrib import admin

from .models import Note, Folders
# Register your models here.
admin.site.register(Note)

admin.site.register(Folders)