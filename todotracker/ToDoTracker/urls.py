"""ToDoTracker URL Configuration

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
from django.contrib import admin
from django.urls import path, re_path
from django.urls.conf import include
from users.urls import urlpatterns as users_urlpatterns
from frontend import views as frontend_views


urlpatterns = [
    path('admin/', admin.site.urls),

    # When we enter localhost:3000/ -> It has frontend_view's index.js and also include
    # tasks.urls which have been registered in the tasks.urls python file
    path('', frontend_views.index),
    path('', include('tasks.urls')),
]
urlpatterns += users_urlpatterns
urlpatterns += [re_path(r'^.*', frontend_views.index)]
