from django.urls import path
from Device import views 
 
urlpatterns = [ 
      
             
    path('manage_building_master/', views.user_list),
    path('manage_building_master/<int:pk>', views.user),
    
    path('manage_bms_floor/', views.floor_list),
    path('manage_bms_floor/<int:pk>', views.floor_details),
    
    path('manage_bms_department/', views.department_list),
    path('manage_bms_department/<int:pk>', views.department),

    path('manage_bms_area/', views.bms_area_list),
    path('manage_bms_area/<int:pk>', views.bms_area_list_1),

    path('manage_bms_subarea/', views.Bms_sub_area_list),
    path('manage_bms_subarea/<int:pk>', views.Bms_sub_area),
    
    path('manage_bms_locker/', views.Bms_locker_list),
    path('manage_bms_locker/<int:pk>', views.Bms_locker_list_details),

    path('manage_bms_devices/', views.Device_list),
    path('manage_bms_devices/<int:pk>', views.Device_list_details),

    
    path('manage_user_area_card_list/', views.bms_user_area_card_list),
    path('manage_user_area_card_list/<int:pk>', views.bms_user_area_card_list_details),

    path('get_bms_all_list/', views.bms_building_floor_area_subarea_device_Serializer_list),
]

