from django.urls import path, re_path

from example.views import *

urlpatterns = [
    path('api/', api_start),
    path('api/ces', api_product),

    path('', ProductList.as_view(), name='catalog_main'),
    path('help/', help, name='helpPage'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='categoryPage'),
    path('catalog-view/', ToyList.as_view(), name='catalog_View_main'),
    path('supplier/create', add_supplier, name='supplier_create_page'),
    path('supplier-view/', SupplierList.as_view(), name='supplier_list_view'),
    path('supplier-view/create', SuppierCreate.as_view(), name='supplier_create_view'),
    path('supplier-view/delete/<int:pk>/', SuppierDelete.as_view(), name='supplier_delete_view'),
    path('supplier-view/view/<int:id_supp>/', SupplierDetail.as_view(), name='supplier_detail_view'),
    path('supplier-view/update/<int:pk>/', SuppierUpdate.as_view(), name='supplier_update_view'),
    path('category/addPage', addPage, name='addPage'),
    path('toy-detail/<int:pk>/', ToyDetail.as_view(), name='toy-detail'),
    path('productPage/<int:pk>/', ProductDetail.as_view(), name='productPage'),
    path('productPage/changePage/<int:pk>/', ProductUpdate.as_view(), name='changePage'),
    path('productPage/delete/<int:pk>/', ProductDelete.as_view(), name='product_delete_view'),
    path('productPage/createPage', ProductCreate.as_view(), name='createPage'),
    path('category/tagPage/', TagList.as_view(), name='tagsPage'),
    path('category/tagPage/<int:pk>', TagDetail.as_view(), name='tagsPageDetail'),
    path('category/tagPage/createTag/', TagCreate.as_view(), name='tagsPageCreate'),
    path('category/createCategory', createCategory, name='createCategory'),
    path('zakaz/', OrderProdList.as_view(), name='zakaz_view'),
    path('zakaz/create', OrderProductCreate.as_view(), name='zakaz_create_view'),
    path('zakaz/update/<int:pk>', OrderProductUpdate.as_view(), name='zakaz_update_view'),
    path('zakaz/delete/<int:pk>', OrderProductDelete.as_view(), name='zakaz_delete_view'),
    path('zakaz/detail/<int:pk>', OrderProductDetail.as_view(), name='zakaz_detail_view'),
    # path('plus/<int:a>/<int:b>/', calc),
    # path('plus_get/', calc_get),
    # path('plus/<str:a>/<str:b>/', calc),
    # re_path('^index/..', ban)
    # ^ -  начало адреса
    # $ -  конец адреса
    # t+ - символ t будет встречаться 1 и более раз
    # t? - символ t будет встречаться 0 или 1 раз
    # ? - символ t будет встречаться 0 или 1 раз
    # . - любой символ
    # t{n} - символ t встречается ровно n раз
    # t{m,n} - символ t встречается от n  до m раз
    # \d{n} \d+ - любая цифра
    # \D{n} \D+ - любая символ
    # \w{n} \w+ - любая буквенный символ



# URL для списка товаров
    path('KB/products/', ProductKBListView.as_view(), name='product_list_info'),

    # URL для подробной информации о товаре
    path('KB/products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

    # URL для списка поставщиков
    path('KB/suppliers/', SupplierListView.as_view(), name='supplier_list'),

    # URL для подробной информации о поставщике
    path('KB/suppliers/<int:pk>/', SupplierDetailView.as_view(), name='supplier_detail'),

    # URL для добавления поставщика
    path('KB/add_supplier/', SupplierCreateView.as_view(), name='add_supplier'),







]
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r"api/products", ProductViewSet, basename="Products")
urlpatterns += router.urls