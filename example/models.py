from django.db import models
import uuid
# Create your models here.
from django.urls import reverse, reverse_lazy


class Toy(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='цена')
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    exist = models.BooleanField(default=True)

    photo = models.ImageField(upload_to='image/%Y/%m/%d', blank=True, null=True)

    supplier = models.ForeignKey('Supplier', on_delete=models.PROTECT, null=True)

    # oto = models.OneToOneField('Supplier', on_delete=models.PROTECT)
    # MtM_with_table = models.ManyToManyField('Supplier',through='check_toy')

    def __str__(self):
        return f'{self.name} - {self.price}'

    class Meta():
        verbose_name = 'Играшка'
        verbose_name_plural = 'Игрушки'
        ordering = ['name', '-price']


class Supplier(models.Model):
    name = models.CharField(verbose_name='Название поставщика')
    telephone = models.CharField(verbose_name="Телефон")
    address = models.CharField(verbose_name="Адресс")

    def get_absolute_url(self):
        return reverse('supplier_detail_view', kwargs={'id_supp': self.pk})

    def __str__(self):
        return f'{self.name} - {self.telephone}'


# связь 1 к 1
class Doc_toy(models.Model):
    number = models.CharField()
    date_confirm = models.DateField()
    data_expire = models.DateField()
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)

    toy = models.OneToOneField(Toy, on_delete=models.PROTECT)


class Supply_toys(models.Model):
    name = models.CharField()
    date_outload = models.DateTimeField(auto_now_add=True)

    toy = models.ManyToManyField(Toy)


class Order(models.Model):
    name = models.CharField()
    date_create = models.DateTimeField(auto_now_add=True)
    address = models.CharField(blank=True)

    toy = models.ManyToManyField(Toy, through='Pos_order_toy')


class Pos_order_toy(models.Model):
    toy = models.ForeignKey(Toy, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)

    count_toys = models.IntegerField()
    discount = models.DecimalField(max_digits=3, decimal_places=2)


class Product(models.Model):
    name = models.CharField(max_length=100)
    creator_name = models.CharField(max_length=100, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='image/%Y/%m/%d', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    exist = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.price}'

    class Meta():
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'
        ordering = ['name', '-price', 'creator_name']


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    products = models.ManyToManyField(Product, related_name='categories')

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Катерогия'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    products = models.ManyToManyField(Product, through='ProductTag')

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class ProductTag(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} - {self.tag.name}"

    class Meta():
        verbose_name = 'Тег продукта'
        verbose_name_plural = 'Теги продуктов'


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey('OrderProduct', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    discount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} - {self.order.order_number}"

    class Meta():
        verbose_name = 'Заказанный продукт'
        verbose_name_plural = 'Заказанные продукты'


class OrderProduct(models.Model):
    order_number = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    delivery_address = models.TextField()
    client_phone = models.CharField(max_length=20)
    client_name = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, through='OrderItem')
    is_deleted = models.BooleanField(default=False,null=True)

    def __str__(self):
        return f"Order {self.order_number} - {self.delivery_address} - {self.client_name} - {self.client_phone}"

    class Meta():
        verbose_name = 'Заказ фотографии'
        verbose_name_plural = 'Заказы фотографий'



class CategoryKB(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория_'
        verbose_name_plural = 'Категории_'

# Модель Тегов
class TagKB(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег_'
        verbose_name_plural = 'Теги_'

# Модель Характеристик товара
class ProductCharacteristic(models.Model):
    product = models.ForeignKey('ProductKB', on_delete=models.CASCADE, verbose_name='Товар')
    characteristic = models.CharField(max_length=255, verbose_name='Характеристика')
    value = models.CharField(max_length=255, verbose_name='Значение')

    def __str__(self):
        return f'{self.product} - {self.characteristic}: {self.value}'

    class Meta:
        verbose_name = 'Характеристика товара_'
        verbose_name_plural = 'Характеристики товара_'

# Модель Товара
class ProductKB(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    category = models.ForeignKey(CategoryKB, on_delete=models.CASCADE, verbose_name='Категория')
    description = models.ManyToManyField(TagKB, verbose_name='Описание', related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    image = models.ImageField(upload_to='product_images/', verbose_name='Картинка')
    is_deleted = models.BooleanField(default=False, verbose_name='Логическое удаление')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар_'
        verbose_name_plural = 'Товары_'

# Модель Поставщика
class SupplierKB(models.Model):
    company_name = models.CharField(max_length=255, verbose_name='Название компании')
    representative_name = models.CharField(max_length=255, verbose_name='ФИО представителя')
    representative_phone = models.CharField(max_length=255, verbose_name='Телефон представителя')
    address = models.TextField(verbose_name='Адрес')
    is_deleted = models.BooleanField(default=False, verbose_name='Логическое удаление')

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Поставщик_'
        verbose_name_plural = 'Поставщики_'

# Модель Поставки
class DeliveryKB(models.Model):
    delivery_number = models.CharField(max_length=255, verbose_name='Номер поставки')
    delivery_date = models.DateTimeField(verbose_name='Дата поставки')
    supplier = models.ForeignKey(SupplierKB, on_delete=models.CASCADE, verbose_name='Поставщик', related_name='deliveries')

    def __str__(self):
        return self.delivery_number

    class Meta:
        verbose_name = 'Поставка_'
        verbose_name_plural = 'Поставки_'

# Модель Заказа
class OrderKB(models.Model):
    order_number = models.CharField(max_length=255, verbose_name='Номер заказа')
    customer_name = models.CharField(max_length=255, verbose_name='ФИО покупателя')
    comment = models.TextField(verbose_name='Комментарий')
    delivery_address = models.TextField(verbose_name='Адрес доставки')
    delivery_method = models.CharField(max_length=255, verbose_name='Способ доставки')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    completion_date = models.DateTimeField(verbose_name='Дата завершения')

    def __str__(self):
        return self.order_number

    class Meta:
        verbose_name = 'Заказ_'
        verbose_name_plural = 'Заказы_'

# Модель Позиции заказа
class OrderItemKB(models.Model):
    order = models.ForeignKey(OrderKB, on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(ProductKB, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    discount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Скидка')

    def __str__(self):
        return f'{self.order} - {self.product}'

    class Meta:
        verbose_name = 'Позиция заказа_'
        verbose_name_plural = 'Позиции заказа_'

# Модель Позиции поставки
class DeliveryItemKB(models.Model):
    product = models.ForeignKey(ProductKB, on_delete=models.CASCADE, verbose_name='Товар')
    delivery = models.ForeignKey(DeliveryKB, on_delete=models.CASCADE, verbose_name='Поставка')
    quantity = models.PositiveIntegerField(verbose_name='Количество товара')

    def __str__(self):
        return f'{self.delivery} - {self.product}'

    class Meta:
        verbose_name = 'Позиция поставки_'
        verbose_name_plural = 'Позиции поставки_'
