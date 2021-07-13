from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('contact.html',views.contact,name="contact"),
    path('courses.html',views.courses,name="courses"),
    path('blog.html',views.blog,name="blog"),
    path('video.html',views.video,name="video"),
    path('login.html',views.login,name="login"),
    path('register.html',views.register,name="register"),
    path('home.html',views.home,name="home"),
    path('logout.html',views.logoutUser,name="logout"),
    path('problem.html',views.problem,name="problem"),
]
