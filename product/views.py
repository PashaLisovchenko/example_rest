from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from product.models import Product, Category
from .serializer import ProductSerializer, CategorySerializer


class ProductList(ListAPIView, CreateAPIView):
    serializer_class = ProductSerializer
    # model = Product
    queryset = Product.objects.all()


class ProductDetail(UpdateAPIView, DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CategoryList(ListAPIView, CreateAPIView):
    serializer_class = CategorySerializer
    # model = Category
    queryset = Category.objects.all()


class CategoryDetail(UpdateAPIView, DestroyAPIView):
    serializer_class = CategorySerializer
    # model = Category
    queryset = Category.objects.all()
