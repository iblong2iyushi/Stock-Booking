from django.urls import path, include
from rest_framework import routers
from .views import CustomersViewSet, StocksViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'customer', CustomersViewSet)
router.register(r'stock', StocksViewSet)

urlpatterns = [
   path('',include(router.urls)), 
]

