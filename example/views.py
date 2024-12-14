from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .serializable import *
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required, permission_required
from .models import ProductKB
from example.models import *
from .forms import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse

# @login_requested(login_url=reverse_lazy('catalog_main'))

# def info(request):
# return HttpResponse (' <h3>Информация</h3>')
# # example. toy_add
# # example. toy_view
# # example. toy_change
# # example. toy_delete
# @permission_required('example.toy_a
# [def calc(request, a, b):
# return HttoResponse(f'ch2>{at + {bt = {a + b7</h2>')





# Create your views here.
def main(request):
    # toyList = Toy.objects.filter(exist=True)
    toyList = Product.objects.filter(is_deleted=False)
    categoryList = Category.objects.all()


    # a = 71
    # b = 54
    #
    # result = a*b

    context = {'list_toys':toyList,
               'categoryList':categoryList,
               'title':"Каталог фотографий"}

    return render(request,'example/index.html',context=context)

def help(request):
    return render(request,'example/help.html')

def category(request,category):
    category_obj = get_object_or_404(Category, name=category)
    toyList = Product.objects.filter(is_deleted=False, categories=category_obj)

    context = {
        'product': toyList,
        'category': category_obj,
        'title': f"Каталог фотографий - {category_obj.name}"
    }

    return render(request, 'example/category.html', context=context)

def addPage(request):
    return render(request,'example/addPage.html')

def productPage(request,id):
    product = get_object_or_404(Product, id=id)
    # categories = product.categories.all()
    categories = product.tag_set.all()
    # category_obj = get_object_or_404(Category, name=product.categories)

    item = product.id
    context = {
        'product': product,
        'item':item,
        'category':categories
    }
    return render(request,'example/productPage.html', context=context)
def tagsPage(request):
    categories = Tag.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'example/tagPage.html', context=context)
def tagsPageDetail(request,tag):

    cat = get_object_or_404(Tag, name=tag)
    # productmain = get_object_or_404(Product, categories=cat)
    # productmain = cat.products.all()

    product = Product.objects.filter(tag=cat)
    categories = Category.objects.filter(name=tag)
    context = {
        'categories': categories,
        'cat': cat,
        'product':product,

    }
    return render(request, 'example/tagPageDetail.html', context=context)
def changePage(request,id):

    return render(request,'example/changePage.html',{'item_change':id})
def createCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()  # Сохранение новой категории
            return redirect('catalog_main')  # Перенаправление после успешного создания
    else:
        form = CategoryForm()

    context = {'form': form}
    return render(request, 'example/create_category.html', context)

def add_supplier(request):
    form_em = EmailForm()
    form_supp = SupplierForm()
    if request.method == 'GET':
        print('Открытие страницы')
    if request.method == 'POST':
        # Обработка формы
        # # print(request.POST.get('subject'))
        # # print(request.POST.get('content'))
        # form_em = EmailForm(request.POST)
        # print(form_em.data)
        #
        # form_em.is_valid()
        # print(form_em.cleaned_data)

    #     Обработка формы supplier
        form_supp = SupplierForm(request.POST)
        if form_supp.is_valid():
            print(form_supp.cleaned_data)
            # new_sup = Supplier(
            #     name=form_supp.cleaned_data.get('name'),
            #     telephone=form_supp.cleaned_data.get('telephone'),
            #     address=form_supp.cleaned_data.get('address'),
            # )
            new_sup = Supplier(**form_supp.cleaned_data)
            new_sup.save()
    context = {
        'form_email':form_em,
        'form_supplier':form_supp

    }
    return render(request,'example/supplier_create.html',context)

class ToyList(ListView):
    model = Toy
    template_name = 'example/index.html'
    context_object_name = 'list_toys'
    extra_context = {'title': 'класс игрушек'}
    paginate_by = 1


    def get_queryset(self):
        return Toy.objects.filter(exist=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        a = 71
        b = 54

        result = a * b

        context["result"] = result

        return context
class ProductList(ListView):
    model = Product.objects.filter(is_deleted=False)
    template_name = 'example/index.html'
    context_object_name = 'list_toys'
    paginate_by = 2

    def get_queryset(self):
        return Product.objects.filter(is_deleted=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        categoryList = Category.objects.all()

        LastCategory = Category.objects.last()



        context["categoryList"] = categoryList
        context["LastCategory"] = LastCategory

        return context

class ProductDetail(DetailView):
    model = Product
    template_name = 'example/productPage.html'
    context_object_name = 'product'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получаем связанные теги для текущего продукта через промежуточную модель ProductTag
        product_tags = ProductTag.objects.filter(product=self.object)
        categories = [product_tag.tag for product_tag in product_tags]
        context["category"] = categories

        return context

class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog_main')

class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog_main')
    template_name = 'example/product_confirm_delete.html'  # Укажите ваш шаблон для формы
    form_class = ProductForm  # Замените на свой класс формы
    context_object_name = 'product'
    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.is_deleted = True  # Логическое удаление: установка is_deleted в True
        obj.save()
        return obj

class TagList(ListView):
    model = Tag
    template_name = 'example/tagPage.html'
    context_object_name = 'categories'
    paginate_by = 2
class TagDetail(DetailView):
    model = Tag
    template_name = 'example/tagPageDetail.html'
    context_object_name = 'cat'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получаем связанные теги для текущего продукта через промежуточную модель ProductTag
        product_tags = ProductTag.objects.filter(tag=self.object)
        products = [product_tag.product for product_tag in product_tags]
        context["product"] = products

        return context

class TagCreate(CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy('tagsPage')

class OrderProdList(ListView):
    model = OrderProduct
    template_name = 'example/order.html'
    context_object_name = 'order'
    paginate_by = 2

class OrderProductDetail(DetailView):
    model = OrderProduct
    template_name = 'example/order_detail_view.html'
    context_object_name = 'order'

class OrderProductCreate(CreateView):
    model = OrderProduct
    form_class = OrderProductForm
    success_url = reverse_lazy('zakaz_view')

class OrderProductUpdate(UpdateView):
    model = OrderProduct
    form_class = OrderProductForm
    success_url = reverse_lazy('zakaz_view')

class OrderProductDelete(DeleteView):
    model = OrderProduct
    success_url = reverse_lazy('zakaz_view')
    template_name = 'example/orderproduct_confirm_delete.html'  # Укажите ваш шаблон для формы
    form_class = OrderProductForm  # Замените на свой класс формы
    context_object_name = 'orderproduct'
    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.is_deleted = True  # Логическое удаление: установка is_deleted в True
        obj.save()
        return obj

class CategoryDetail(DetailView):
    model = Category
    template_name = 'example/category.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получаем связанные теги для текущего продукта через промежуточную модель ProductTag
        products = Product.objects.filter(categories=self.object)
        context["product"] = products

        return context

class ToyDetail(DetailView):
    model = Toy
    template_name = 'example/index.html'
    context_object_name = 'list_toys'
    paginate_by = 2


class SupplierDetail(DetailView):
    model = Supplier
    pk_url_kwarg = 'id_supp'

class SupplierList(ListView):
    model = Supplier

class SuppierCreate(CreateView):
    model = Supplier
    form_class = SupplierForm
    success_url = reverse_lazy('supplier_list_view')


class SuppierUpdate(UpdateView):
    model = Supplier
    form_class = SupplierForm

class SuppierDelete(DeleteView):
    model = Supplier

    success_url = reverse_lazy('supplier_list_view')




# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

class ProductKBListView(ListView):
    model = ProductKB
    template_name = 'example/KB/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return ProductKB.objects.all()
class ProductDetailView(DetailView):
    model = ProductKB
    template_name = 'example/KB/product_detail.html'
    context_object_name = 'product'

class SupplierListView(ListView):
    model = SupplierKB
    template_name = 'example/KB/supplier/supplier_list.html'
    context_object_name = 'suppliers'

class SupplierDetailView(DetailView):
    model = SupplierKB
    template_name = 'example/KB/supplier/supplier_detail.html'
    context_object_name = 'supplier'

class SupplierCreateView(CreateView):
    model = SupplierKB
    template_name = 'example/KB/supplier/supplier_form.html'
    form_class = SupplierKBForm
    success_url = reverse_lazy('supplier_list')

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<













def api_start(request):
    return JsonResponse({"message": "Hello API Django"})

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

@api_view(['GET', 'POST', 'PUT','DELETE'])
def api_product(request):
    products = Product.objects.all()
    ser_products = ProductSerializer(products, many=True)

    if request.method == "POST":
        print(request.POST)
    if request.method == "GET":
        ProductViewSet(instance=ser_products)


    return Response({"products": ser_products.data})


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProductListView(ListView):
    pass
