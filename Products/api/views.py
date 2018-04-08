from rest_framework.generics import ListAPIView
from Products.models import Category, Subcategory, Products
from .serializers import CategorySerializer, SubcategorySerializer,ProductCategorySerializer
from rest_framework.filters import SearchFilter
from rest_framework import filters
from django.db.models import Q
import django_filters


#4
class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#5
class SubcategoryFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(name="category__main_category")

    class Meta:
        model = Subcategory
        fields = ['category']

class SubcategoryListAPIView(ListAPIView):

    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    filter_class = SubcategoryFilter


#6
class ProductCategoryFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(name="category__main_category")

    class Meta:
        model = Products
        fields = ['category']

class ProductCategoryListAPIView(ListAPIView):

    queryset = Products.objects.all()
    serializer_class = ProductCategorySerializer
    filter_class = ProductCategoryFilter
