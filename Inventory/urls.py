from django.urls import path
from Inventory import views

urlpatterns = [
    path('addviewcategory/', views.Bms_InventoryListView),
    path('deleteupdatecategory/<int:pk>', views.Bms_InventoryDetailView),
    
    path('addviewitems/', views.Bms_ItemListView),
    path('deleteupdateitems/<int:pk>', views.Bms_ItemDetailView),
    
    path('addviewmanagestock/', views.Bms_manage_inventoryListView),
    path('deleteupdatemanagestock/<int:pk>', views.Bms_manage_inventoryDetailView),
    
]