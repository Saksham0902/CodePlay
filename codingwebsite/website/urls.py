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
    path('problems/ThreeNumberSum.html',views.ThreeNumberSum,name="ThreeNumberSum"),
    path('problems/ProductSum.html',views.ProductSum,name="ProductSum"),
    path('problems/RemoveKthElementFromTheEnd.html',views.RemoveKthElementFromTheEnd,name="RemoveKthElementFromTheEnd"),
    path('problems/ValidateBST.html',views.ValidateBST,name="ValidateBST"),
    path('problems/MoveElementToEnd.html',views.MoveElementToEnd,name="MoveElementToEnd"),
    path('problems/NumberOfWaysToMakeChange.html',views.NumberOfWaysToMakeChange,name="NumberOfWaysToMakeChange"),
    path('problems/SingleCycleCheck.html',views.SingleCycleCheck,name="SingleCycleCheck"),
]
