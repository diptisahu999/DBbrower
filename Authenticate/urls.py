
from django.urls import include, path,re_path
from Authenticate import views
from django.contrib import admin 
# from corsheaders.views import cors_exempt

from .views import LoginView

urlpatterns = [        
    path('manage_user_list/', views.user_list),
    path('manage_user_list/<int:pk>', views.user),
    
    path('manage_user_profile/', views.user_details_list),
    path('manage_user_profile/<int:pk>', views.user_detail),
     
    path('login/',LoginView.as_view(),name='login'),
    
    # path('login/',views.user),
    
    path('manage_role_list/', views.role_list),
    path('manage_role_list/<int:pk>', views.role_detail),
    
    
    path('manage_module_list/', views.module_list),
    path('manage_module_list/<int:pk>', views.module_detail),

    path('manage_role_device_information_list/', views.role_device_information_list),
    path('manage_role_device_information_list/<int:pk>', views.role_device_information_details),
    
    
]
