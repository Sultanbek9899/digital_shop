from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST

from backend.apps.service.serializers import ProductSerializer, ProductQuantitySerializer
from backend.apps.service.models import Product
from backend.apps.service.tasks import send_email_with_report

class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductUpdateAPIView(UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductQuantityAddView(APIView):

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductQuantitySerializer(data=request.POST)
        if serializer.is_valid():
            if request.GET.get("q") == "update":
                product.quantity = serializer.data["quantity"]
            else:
                product.quantity += serializer.data["quantity"]
            send_email_with_report()
            product.save(update_fields=["quantity"])
            return Response(status=HTTP_200_OK)
        return Response({"message":"Invalid data", "errors":serializer.errors}, status=HTTP_400_BAD_REQUEST)
# Create your views here.
