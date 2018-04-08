from rest_framework.generics import ListAPIView, CreateAPIView
from Products.models import Category, Subcategory, Products
from .serializers import (
    CategorySerializer, SubcategorySerializer,
    ProductCategorySerializer, ProductSubcategorySerializer,
    ProductCreateSerializer)
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

#6 NO django filter use in this
class ProductCategoryListAPIView(ListAPIView):

    serializer_class = ProductCategorySerializer

    def get_queryset(self):
        queryset = Products.objects.all()
        category = self.request.query_params.get("category", None)
        if category is not None:
            queryset = queryset.filter(subcategory__category__main_category__icontains=category)
        return queryset


#7
class ProductSubcategoryFilter(django_filters.FilterSet):
    subcategory = django_filters.CharFilter(name="subcategory__sub_category")

    class Meta:
        model = Products
        fields = ['subcategory']

class ProductSubcategoryListAPIView(ListAPIView):

    queryset = Products.objects.all()
    serializer_class = ProductSubcategorySerializer
    filter_class = ProductSubcategoryFilter


#8
class ProductCreateAPIView(CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = ProductCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
