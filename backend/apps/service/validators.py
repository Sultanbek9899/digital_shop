from rest_framework.serializers import ValidationError


def negative_number(value):
    print(type(value))
    print(value)
    if value < 0:
        raise ValidationError("Product Quantity must be positive number")