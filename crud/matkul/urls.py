from django.contrib import admin  
from django.urls import path  
from matkul import views  
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('create', views.create),  
    path('read',views.read),  
    path('update/<int:id>', views.update),  
    path('update_matkul/<int:id>', views.update_matkul),  
    path('delete/<int:id>', views.delete),  
]  