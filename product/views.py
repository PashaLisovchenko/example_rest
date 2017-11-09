from rest_framework.viewsets import ModelViewSet
from product.models import Product, Category
from .serializer import ProductSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
