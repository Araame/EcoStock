from rest_framework.viewsets import ModelViewSet
from ecostock.serializers import ProductSerializer, WarehouseSerializer
from ecostock.models import Product, Warehouse
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.all()
    

class WarehouseViewSet(ModelViewSet):
    serializer_class = WarehouseSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return Warehouse.objects.all()