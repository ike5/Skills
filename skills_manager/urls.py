from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('categories/<slug:category_slug>/', views.category_detail, name='category_detail'),
    path('skills/create/', views.create_skills_collection, name='create_skills_collection'),
    path('skills/<int:collection_id>/', views.skills_collection_detail, name='skills_collection_detail'),
    path('skills/<int:collection_id>/download/', views.download_skills_file, name='download_skills_file'),
]