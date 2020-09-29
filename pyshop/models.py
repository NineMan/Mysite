from django.db import models
from django.core import serializers
from django.http import HttpResponse


class Category(models.Model):
    name = models.CharField(u'категория', max_length=50)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    categories = models.ManyToManyField(Category,
                                        related_name='products',
                                        blank=True, verbose_name=u"категории")
    related_products = models.ManyToManyField('Product',
                                              blank=True,
                                              verbose_name="связанные продукты")

    sku = models.CharField(u'артикул', max_length=128, unique=True)

    price = models.DecimalField(u'цена', max_digits=12, decimal_places=4)

    slug = models.SlugField(u'slug', max_length=80, db_index=True, unique=True)

    name = models.CharField(u'название', max_length=128)
    title = models.CharField(u'заголовок страницы (<title>)', max_length=256, blank=True)
    description = models.TextField(u'описание', blank=True)

    def __str__(self):
        return self.name


@classmethod
def live_search(request, template_name="pyshop/livesearch_results.html"):
    q = request.GET.get("q", "")
    sku = Product.objects.filter(sku__contains=q)
    name = Product.objects.filter(name__contains=q)
    description = Product.objects.filter(description__contains=q)
    answer = sku.union(name)
    answer = answer.union(description)
    data = serializers.serialize('json', answer)
    return HttpResponse(data, content_type='application/json')
