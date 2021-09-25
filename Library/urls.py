"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from Book.views import *
from subscribe.views import *
# from Book.views.first_views import func1              #dono ka kam views folder me kar sakte he
# from Book.views.second_views import func2
from Book import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('homepage/',views.homepage,name="home"),
    path('show-books/',views.get_books,name="show_book"),
    path("delete-book/<int:id>/",views.delete_book,name="delete_book"),
    path("update-book/<int:id>/",views.update_book,name="update_book"),
    path("soft-delete-book/<int:id>/",views.soft_delete,name="soft_delete"),
    path("active-books/",views.active_books,name="active_books"),
    path("in-active-books/",views.in_active_books,name="in_active_books"),
    path("rrr-book/<int:id>/", views.rrr_books, name="rrr_books"),
    path("subscribe_email/", subscribe_email, name="subscribe_email"),

    path("func1/",views.func1 ,name="func1"),
    path("func2/",views.func2 ,name="func2"),
]
