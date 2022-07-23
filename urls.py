"""quartermaster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from .views import Categories, SingleCategory, Things, SingleThing

urlpatterns = [
    path('api/categories/', Categories.as_view(), name='categories'),
    path('api/category/<int:cid>', SingleCategory.as_view(), name='category'),
    path('api/things/', Things.as_view(), name='things'),
    path('api/things/<int:tid>', SingleThing.as_view(), name='thing'),
]
