"""ToDo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from todo_app.views import todo_view,addtodo,deletetodo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/',todo_view,name="todo_list"),
    path('',todo_view,name="todo_list"),
    path('addtodo/',addtodo,name="todo_add"),
    path('deletetodo/<int:todo_id>/',deletetodo,name="todo_delete"),
]
