from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Note

class NotesHomeView(ListView):
    template_name = 'notes/note_list.html'
    model = Note
