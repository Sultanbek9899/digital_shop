from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework.response import  Response
from rest_framework.status import HTTP_404_NOT_FOUND

from backend.apps.service.models import Product


class ResponseCheckMiddleware(MiddlewareMixin):

    def is_exists(self, request, pk):
        if request.method in ["POST", "PATCH", "PUT"]:
            try:
                Product.objects.get(id=pk)
                return True
            except Product.DoesNotExist:
                return False
        return False

    def process_request(self, request, *args, **kwargs):
        if kwargs.get("pk", None):
            if not self.is_exists(request, kwargs.get("pk")):
                return HttpResponse("Product Not Found", status=404)