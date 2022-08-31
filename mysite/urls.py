from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('foods/', include('foods.urls')),
    path('api/v1/foods/', include('foods.urls')),
    path('admin/', admin.site.urls),
]
