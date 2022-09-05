from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "date")

admin.site.register(Note)

# Register your models here.
