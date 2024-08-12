
from django.contrib import admin
from django.urls import path
from app.views import home,about,contact,loginuser,register,myblogs,logoutuser,createblogs,blogpost,delete_post,edit_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('about/',about,name='about'),

    path('contact/',contact,name='contact'),
    path('contact',contact,name='contact'),

    path('login/',loginuser,name='login'),
    path('login',loginuser,name='login'),

    path('register/',register,name='register'),
    path('register',register,name='register'),

    path('myblogs/',myblogs,name='myblogs'),
    path('myblogs',myblogs,name='myblogs'),

    path('logout/',logoutuser,name='logout'),
    
    path('createblogs/',createblogs,name='createblogs'),
    path('createblogs',createblogs,name='createblogs'),

    path('<str:slug>/',blogpost,name='blogpost'),
    path('post/<int:sno>/delete/', delete_post, name='delete_post'),

    path('post/<int:sno>/edit/', edit_post, name='edit_post'),
    
]

