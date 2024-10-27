from django.urls import reverse,path
from . import views

app_name = 'api_services'


urlpatterns = [
    path('shop/list/',views.ShopListView.as_view(),name="api_shop_list"),
    path('shop/create/',views.ShopCreateView.as_view(),name="api_shop_create"),
    path('shop/detail/<path:slug>',views.ShopRetrieveView.as_view(),name="api_shop_retrive"),
    path('shop/update/<int:pk>/',views.ShopUpdateView.as_view(),name="api_shop_update"),
    path('shop/delete/<int:pk>/',views.ShopDeleteView.as_view(),name="api_shop_Delete"),
]
