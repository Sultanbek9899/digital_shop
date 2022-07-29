from django.urls import path, include

from rest_framework.routers import DefaultRouter

from backend.apps.service.views import ProductCreateAPIView, ProductUpdateAPIView, ProductQuantityAddView

urlpatterns = [
    path("create/product/", ProductCreateAPIView.as_view()),
    path("update/product/<int:pk>/", ProductUpdateAPIView.as_view()),
    path("update/quantity/<int:pk>/", ProductQuantityAddView.as_view(), name="quantity_update")
]