from rest_framework.viewsets import ModelViewSet
from ecostock.serializers import ProductSerializer, WarehouseSerializer
from ecostock.models import Product, Warehouse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from rest_framework import status


# Create your views here.
class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.all()
    

   
    @action(detail=True, methods=['post'])
    @transaction.atomic
    def transfer(self, request, pk=None):
       
        product = self.get_object()
        
        if product.status == 'perime':
            return Response({"detail": "Expired product","current_status": product.status}, status=status.HTTP_403_FORBIDDEN)

        warehouse_id = request.data.get('warehouse_id')

        if not warehouse_id:
            return Response({"error": "Warehouse id not found"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            dest_warehouse = Warehouse.objects.get(id=warehouse_id)
        except Warehouse.DoesNotExist:
            return Response({"error": "Warehouse not found"}, status=status.HTTP_404_NOT_FOUND)


        product.warehouse = dest_warehouse
        product.save()

        return Response({"detail": "Transfer done","destination_warehouse": {"product": product.id, "warehouse": dest_warehouse.title}}, status=status.HTTP_200_OK)

 
    
   


class WarehouseViewSet(ModelViewSet):
    serializer_class = WarehouseSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return Warehouse.objects.all()
   
    @action(detail=False, methods=['get'])
    def audit(self, request, pk=None):
        warehouse_id = request.query_params.get('warehouse_id')
        
        if not warehouse_id:
            return Response({"error": "Warehouse id not ound in the url"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            warehouse = Warehouse.objects.get(id=warehouse_id)
        except Warehouse.DoesNotExist:
            return Response({"error": "Warehouse not found"}, status=status.HTTP_404_NOT_FOUND)

        

        return Response({
            "warehouse": {"id": warehouse.id},
            "total_items": Product.objects.filter(warehouse=warehouse).count(),
        }, status=status.HTTP_200_OK)

  

    