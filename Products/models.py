from django.db import models

# Create your models here.
class Category(models.Model):
    main_category = models.CharField(max_length=200, default = '')

    def __str__(self):
        return '%s' % (self.main_category)

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=200, default = '')

    def __str__(self):
        return '%s' % (self.sub_category)

class Products(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200, default = '')

    def __str__(self):
        return '%s' % (self.product_name)
