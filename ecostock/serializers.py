from rest_framework import serializers
from ecostock.models import Product, Warehouse



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "quantity", "description", "warehouse", "status"]

    def validate(self, data):
        if data["name"].length > 30:
            raise serializers.ValidationError("The name must contain 30 characters.")
        
        if data["description"].length > 50 :
            raise serializers.ValidationError("The description must contain 50 characters")
        return data
        
        



class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields =  ["id", "title", "location", "capacity"]

    def validate(self, data):
        if Warehouse.objects.filter(title = data["title"]).exists():
            raise serializers.ValidationError("The warehouse already exists ")
        return data

