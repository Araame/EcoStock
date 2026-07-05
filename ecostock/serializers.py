from rest_framework import serializers
from ecostock.models import Product, Warehouse



class ProductSerializer(serializers.ModelSerializer):
    model = Product
    fields = ["id", "name", "quantity", "description", "warehouse", "status"]

    def validate_product(self, data):
        if data["name"].length > 30:
            return serializers.ValidationError("The name must contain 30 characters.")
        
        if data["description"].length > 50 :
            return serializers.ValidationError("The description must contain 50 characters")
        
    


