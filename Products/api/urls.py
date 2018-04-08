from django.contrib import admin
from django.urls import path, include
from Products.api.views import CategoryListAPIView, SubcategoryListAPIView, ProductCategoryListAPIView,ProductSubcategoryListAPIView

urlpatterns = [
    path('allcategories/', CategoryListAPIView.as_view(), name = 'Categorylist'),
    path('allsubcategories/', SubcategoryListAPIView.as_view(), name = 'Subcategorylist'),
    path('productcategories/', ProductCategoryListAPIView.as_view(), name = 'ProductCategorylist'),
    path('productsubcategories/', ProductSubcategoryListAPIView.as_view(), name = 'ProductSubcategorylist'),
]
