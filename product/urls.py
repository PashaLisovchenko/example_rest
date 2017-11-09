from django.conf.urls import url
from .views import ProductList, ProductDetail, CategoryDetail, CategoryList


urlpatterns = [
    url(r'^list_product/', ProductList.as_view(), name='product_list'),
    url(r'^detail_product/(?P<pk>\d+)/', ProductDetail.as_view(), name='product_detail'),

    url(r'^list_category/', CategoryList.as_view(), name='category_list'),
    url(r'^detail_category/(?P<pk>\d+)/', CategoryDetail.as_view(), name='category_detail'),
]
