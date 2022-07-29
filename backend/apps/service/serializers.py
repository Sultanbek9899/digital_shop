from rest_framework import serializers

from backend.apps.service.models import Product
from backend.apps.service.validators import negative_number


class ProductSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(validators=[negative_number])

    class Meta:
        model = Product
        fields = (
            "name",
            "description",
            "price",
            "quantity",
        )


class ProductQuantitySerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(required=True, validators=[negative_number])

    class Meta:
        model = Product
        fields = (
            "quantity",
        )