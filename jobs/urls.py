from django.urls import path
from . import views

urlpatterns  = [
    path('', views.job_list, name='job_list'),
    path('post_job/', views.post_job, name='post_job'),
    path('apply/<int:job_id>/', views.apply_for_job, name='apply_for_job'),
]