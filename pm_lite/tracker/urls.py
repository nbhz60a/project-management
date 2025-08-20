from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
]
