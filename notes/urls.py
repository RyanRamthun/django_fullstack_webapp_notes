from django.urls import path
from . import views
from .views import NoteListView, NoteDetailView, NoteCreateView, NoteUpdateView, NoteDeleteView

urlpatterns = [
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='notes-detail'),
    path('notes/<int:pk>/update', NoteUpdateView.as_view(), name='notes-update'),
    path('notes/<int:pk>/delete', NoteDeleteView.as_view(), name='notes-delete'),
    path('notes/new/', NoteCreateView.as_view(), name='notes-create'),
    path('about/', views.about, name='notes-about'),
    path('', NoteListView.as_view(), name='notes-home'),
]
