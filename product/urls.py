from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet


router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = [
    url(r'api/', include(router.urls)),
]
