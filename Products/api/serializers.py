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

#6
class ProductCategorySerializer(ModelSerializer):

    main_category = serializers.CharField(source='subcategory.category')
    #sub_category_name = serializers.CharField(source='subcategory.sub_category')
    class Meta:
        model = Products
        fields = [
        'main_category',
        #'sub_category_name',
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

#8
class ProductCreateSerializer(ModelSerializer):

    #main_category = serializers.CharField(source='subcategory.category')
    #sub_category_name = serializers.CharField(source='subcategory.sub_category')
    sub_category = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Products
        fields = [
        #'main_category',
        #'sub_category_name',
        'id','product_name', 'sub_category'
        ]

    def create(self, validated_data):
        id_param = validated_data.pop('sub_category')
        subcategory = Subcategory.objects.get_or_create(id=id_param)[0]
        product = Menu.objtects.create(resturant_id=resturant.id)
        return product
