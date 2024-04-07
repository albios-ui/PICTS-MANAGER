"""pixman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from pixman import crud_photos, crud_albums

urlpatterns = [
    path('admin/', admin.site.urls),
    path('photos', crud_photos.photo_list),
    path('fileimage', crud_photos.save_file),
    path('albums', crud_albums.album_list),
    path('album/<str:name>', crud_albums.get_album),
]
