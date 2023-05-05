from django.urls import path
from .views import *

urlpatterns = [
    path('get-resturants/', getResturantsData.as_view(), name='get_resturants'),
    path('get-resturants-list/', getResturantsDataByIds.as_view(), name='get_resturants_by_ids'),
    path('get-list-items/', getListItems.as_view(), name='List_items'),
    path('create-list/', createListItems.as_view(), name='create_list'),
    path('update-item/<int:pk>', UpdateItemAPIView.as_view(), name='update_Item'),
    path('delete-list/', DeleteItemAPIView.as_view(), name='delete_item')
]
