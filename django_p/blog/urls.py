# from django.urls import path
# from . import views
# urlpatterns = [
#     path('', views.home , name='blog-home '),
#    # path('about/',views.about , name="about_page"),
# ]



from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('blog/', views.index, name='index'),
    path('add/', views.add_task, name='add_task'),
    path('toggle/<int:task_id>/', views.toggle_complete, name='toggle_complete'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]

