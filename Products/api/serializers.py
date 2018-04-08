from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from Products.models import Category, Subcategory, Products


#4 To get all categories
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = [
        'id',
        'main_category',
        ]


#5
# to get all sub_category of a category , just run a
# ''?'' query in url like "?category=main category 1"
class SubcategorySerializer(ModelSerializer):

    category_name = serializers.CharField(source='category.main_category')
    class Meta:
        model = Subcategory
        fields = [
        'category_name',
        'sub_category',
        ]


class ProductCategorySerializer(ModelSerializer):

    #category_name = serializers.CharField(source='category.main_category')
    category_name = CategorySerializer(source='category_set')
    class Meta:
        model = Products
        fields = [
        'category_name',
        'product_name',
        ]


#7
# to get all sub_category of a category , just run a
# ''?'' query in url like "?subcategory=sub category 2"
class ProductSubcategorySerializer(ModelSerializer):

    sub_category_name = serializers.CharField(source='subcategory.sub_category')

    class Meta:
        model = Products
        fields = [
        'sub_category_name',
        'product_name',
        ]
