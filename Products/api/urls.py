from django.contrib import admin
from django.urls import path, include
from Products.api.views import CategoryListAPIView, SubcategoryListAPIView, ProductCategoryListAPIView

urlpatterns = [
    path('allcategories/', CategoryListAPIView.as_view(), name = 'Categorylist'),
    path('allsubcategories/', SubcategoryListAPIView.as_view(), name = 'Subcategorylist'),
    path('productcategories/', ProductCategoryListAPIView.as_view(), name = 'ProductCategorylist'),
    #path('productcategories/', ProductCategoryListAPIView.as_view(), name = 'ProductCategorylist'),
]
