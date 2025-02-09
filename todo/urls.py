from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),  # Login page first
    path('signup/', views.signup, name='signup'),  # Signup page
    path('todopage/', views.todo, name='todo_page'),  # Todo page
    path('logout/', views.logout_view, name='logout'),  # Logout
    path('add_task/', views.add_task, name='add_task'),  # AJAX Task Addition
    path('complete_task/', views.complete_task, name='complete_task'),  # Mark Task as Completed
]
