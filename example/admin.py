from django.contrib import admin

# Register your models here.
from .models import Toy, Supplier, Order, Doc_toy, Pos_order_toy, Supply_toys,Product,ProductTag,OrderProduct,OrderItem,Category,Tag, CategoryKB, TagKB, ProductKB, ProductCharacteristic, SupplierKB, DeliveryKB, OrderKB, OrderItemKB, DeliveryItemKB



class ToyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'exist')
    list_display_links = ('name',)
    list_editable = ('price', 'exist')
    list_filter = ('exist',)
admin.site.register(Toy,ToyAdmin)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'telephone', 'address')
    list_display_links = ('name',)
    list_editable = ('telephone', 'address')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator_name', 'price','is_deleted')
    list_display_links = ('name',)
    list_editable = ('creator_name', 'price','is_deleted')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name',)

@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ('product', 'tag')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity', 'discount')
    list_display_links = ('product',)
    list_editable = ('quantity', 'discount')

@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('order_number','is_deleted','created_at', 'delivery_address', 'client_phone','client_name')
    list_display_links = ('created_at','client_phone')
    list_editable = ('delivery_address','is_deleted','client_name')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(Doc_toy)
class Doc_toyAdmin(admin.ModelAdmin):
    pass

@admin.register(Pos_order_toy)
class Pos_order_toyAdmin(admin.ModelAdmin):
    pass

@admin.register(Supply_toys)
class Supply_toysAdmin(admin.ModelAdmin):
    pass

@admin.register(CategoryKB)
class CategoryKBAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ('name', 'description')
    list_editable = ()
    ordering = ('name',)

# Регистрация модели Тегов в административной панели
@admin.register(TagKB)
class TagKBAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ('name', 'description')
    list_editable = ()
    ordering = ('name',)

# Регистрация модели Товара в административной панели
@admin.register(ProductKB)
class ProductKBAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'created_date', 'updated_date', 'is_deleted')
    list_display_links = ('name',)
    list_filter = ('category', 'is_deleted')
    search_fields = ('name', 'category__name', 'price')
    list_editable = ('price', 'is_deleted')
    ordering = ('name',)
# Регистрация модели Характеристик товара в административной панели
@admin.register(ProductCharacteristic)
class ProductCharacteristicAdmin(admin.ModelAdmin):
    list_display = ('product', 'characteristic', 'value')
    list_display_links = ('product',)
    list_filter = ('product', 'characteristic')
    search_fields = ('product__name', 'characteristic', 'value')
    list_editable = ()
    ordering = ('product',)
# Регистрация модели Поставщика в административной панели
@admin.register(SupplierKB)
class SupplierKBAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'full_name', 'representative_phone', 'address', 'is_deleted')
    list_display_links = ('company_name',)
    list_filter = ('company_name', 'is_deleted')
    search_fields = ('company_name', 'representative_name', 'representative_phone', 'address')
    list_editable = ('is_deleted',)
    ordering = ('company_name',)

    def full_name(self, obj):
        return f'{obj.representative_name}'

    full_name.short_description = 'ФИО представителя'
# Регистрация модели Поставки в административной панели
@admin.register(DeliveryKB)
class DeliveryKBAdmin(admin.ModelAdmin):
    list_display = ('delivery_number', 'delivery_date', 'supplier')
    list_display_links = ('delivery_number',)
    list_filter = ('delivery_number', 'delivery_date', 'supplier')
    search_fields = ('delivery_number', 'supplier__company_name')
    list_editable = ()
    ordering = ('delivery_number',)
# Регистрация модели Заказа в административной панели
@admin.register(OrderKB)
class OrderKBAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'customer_name', 'delivery_address', 'delivery_method', 'created_date', 'completion_date')
    list_display_links = ('order_number',)
    list_filter = ('order_number', 'delivery_method', 'completion_date')
    search_fields = ('order_number', 'customer_name', 'delivery_address', 'delivery_method')
    list_editable = ()
    ordering = ('order_number',)
# Регистрация модели Позиции заказа в административной панели
@admin.register(OrderItemKB)
class OrderItemKBAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'discount')
    list_display_links = ('order',)
    list_filter = ('order', 'product')
    search_fields = ('order__order_number', 'product__name')
    list_editable = ('quantity', 'discount')
    ordering = ('order',)
# Регистрация модели Позиции поставки в административной панели
@admin.register(DeliveryItemKB)
class DeliveryItemKBAdmin(admin.ModelAdmin):
    list_display = ('delivery', 'product', 'quantity')
    list_display_links = ('delivery',)
    list_filter = ('delivery', 'product')
    search_fields = ('delivery__delivery_number', 'product__name')
    list_editable = ('quantity',)
    ordering = ('delivery',)