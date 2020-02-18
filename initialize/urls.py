from django.urls import path

from . import views

urlpatterns = [
    path('', views.display, name='display'),
    path(r'customer', views.list_customer, name='list'),
    path(r'customer/add/<str:name>', views.add_customer, name='add'),
    path(r'customer/delete/<str:name>', views.delete_customer, name='delete'),
    path(r'customer/update/<str:old_name>/<str:new_name>',views.update_customer, name='update'),
    path(r'stock/', views.list_stock, name='list'),
    path(r'stock/add/<str:name>', views.add_stock, name='add'),
    path(r'stock/delete/<str:name>', views.delete_stock, name='delete'),
    path(r'stock/update/<str:old_name>/<str:new_name>',views.update_stock, name='update'),
]
