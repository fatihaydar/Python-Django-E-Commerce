from django.contrib import admin
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
# Register your models here.
from product.models import Category, Product, ProductImage

class ImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product','image','create_at')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','category','status')
    list_filter = ('category','status','price')
    inlines = [ImageInline]
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','status')
class ModelClass:

    detail = RichTextUploadingField()

class PostForm(forms.ModelForm):
    detail = forms.CharField(widget=CKEditorUploadingWidget())


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage,ProductImageAdmin)