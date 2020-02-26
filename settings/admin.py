from django.contrib import admin
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.
from django import forms

from settings.models import Settings



class ModelClass:

    hakkimizda = RichTextUploadingField()
    iletisim = RichTextUploadingField()

class PostForm(forms.ModelForm):
    hakimizda = forms.CharField(widget=CKEditorUploadingWidget())
    iletisim = forms.CharField(widget=CKEditorUploadingWidget())



admin.site.register(Settings)
