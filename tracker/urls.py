from django.urls import path
from . import views

urlpatterns = [
    path('tracker_page', views.tracker_page, name = 'tracker_page'),
    path('tracker_page/<int:task_id>/', views.tracker_page, name = 'edit_tracker'),
    path('trackers', views.trackers, name = 'trackers'),
    path('',views.main_page, name = 'main_page'),
    path('delete/<int:task_id>',views.delete_task, name = 'delete_task')
]