from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('addtask/', views.add_task, name='addtask'),
    path('completed/', views.completed, name='completed'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path("edit/<int:task_id>/", views.edit_task, name="edit_task"),
    path("delete/<int:task_id>/", views.delete_task, name="delete_task"),
    path("complete/<int:id>/",views.complete_task,name="complete_task"),
    path("undo/<int:id>/",views.undo_complete,name="undo_complete"),
    path("edit-profile/",views.edit_profile,name="edit_profile"),
    path("change-password/",views.change_password,name="change_password"),
]