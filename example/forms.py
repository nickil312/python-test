import re
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
class EmailForm(forms.Form):
    subject = forms.CharField(
        label='Заголовок письма',
        max_length=40,
        strip=True,
        widget=forms.TextInput(
            attrs={
                "class":"form-control p-2 m-2"
            }
        )

    )

    content = forms.CharField(
        label="Тело письма",
        strip=True,
        widget=forms.Textarea(
            attrs={
                "class": "form-control p-2 m-2"
            }
        )
    )
class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        # fields = "__all__"
        fields = ["name","telephone","address"]
        widgets={
            "name":forms.TextInput(
                attrs={
                    "class":"form-control"
                }
            ),
            "telephone": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "address": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            )
        }
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name","description","products"]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class ProductDeleteForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['is_deleted']
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
class OrderProductForm(forms.ModelForm):
    class Meta:
        model = OrderProduct
        fields = "__all__"
class RegisForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()


class SupplierKBForm(forms.ModelForm):
    class Meta:
        model = SupplierKB
        fields = '__all__'

    def clean_representative_phone(self):
        phone = self.cleaned_data.get('representative_phone')
        # Проверка телефона по маске +7(___)-___-__-__
        if not re.match(r'^\+7\(\d{3}\)-\d{3}-\d{2}-\d{2}$', phone):
            raise forms.ValidationError("Введите номер телефона в формате +7(***)-***-**-**")
        return phone