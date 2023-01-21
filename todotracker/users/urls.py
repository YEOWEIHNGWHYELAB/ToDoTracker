from django.urls import include, path


# Using djoser to help with login/logout
urlpatterns = [
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken'))
]
