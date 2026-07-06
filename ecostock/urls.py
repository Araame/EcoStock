from django.urls import path, include
from rest_framework import routers
from ecostock.views import ProductViewSet, WarehouseViewSet

router_product = routers.SimpleRouter()
router_product.register("products", ProductViewSet, basename="product" )


router_warehouse= routers.SimpleRouter()
router_warehouse.register("warehouses", WarehouseViewSet, basename="warehouse")



urlpatterns = [
    path("", include(router_product.urls)),
    path("", include(router_warehouse.urls))     
    
    
]
