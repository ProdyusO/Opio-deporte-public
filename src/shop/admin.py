"""Administration's model module."""
from django.contrib import admin
from .models import CartProduct, Category, Customer, Product, Error  # pylint: disable=E0402
from django import forms
from ckeditor.widgets import CKEditorWidget


class ProductCartAdmin(admin.ModelAdmin):
    """Item's controller."""

    list_display = (
        "customer",
        "product",
        "price",
        "quantity",
        "total",
        "in_order",
        "done",
        "created",
    )


class CustomerAdmin(admin.ModelAdmin):
    """Customer's controller."""

    list_display = (
        "name",
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "comment",
        "created",
    )


class ProductAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Product
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(CartProduct, ProductCartAdmin)
admin.site.register(Error)
