from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Settings(models.Model):
    title="Settings"
    hakkimizda      = RichTextUploadingField()
    hakkimizdaimage = models.ImageField(upload_to='images',blank=True)
    iletisim        = RichTextUploadingField()
    iletisimimage   = models.ImageField(upload_to='images',blank=True)
    smtpserver      = models.CharField(max_length=255,blank=True)
    smtpport        = models.CharField(max_length=255,blank=True)
    smtpmail        = models.CharField(max_length=255,blank=True)
    smtppass        = models.CharField(max_length=255,blank=True)
    facebook        = models.CharField(max_length=255,blank=True)
    twitter         = models.CharField(max_length=255,blank=True)
    instagram       = models.CharField(max_length=255,blank=True)
    pinterest       = models.CharField(max_length=255,blank=True)
    gplus           = models.CharField(max_length=255,blank=True)
    youtube         = models.CharField(max_length=255,blank=True)
    tumblr          = models.CharField(max_length=255,blank=True)
    kisailetisim    = models.TextField(blank=True)
    kisahakkimizda  = models.TextField(blank=True)
    adres           = models.CharField(max_length=255,blank=True)
    sehir           = models.CharField(max_length=255,blank=True)
    fax             = models.CharField(max_length=255,blank=True)
    tel             = models.CharField(max_length=255,blank=True)
    email           = models.CharField(max_length=255,blank=True)
    def __str__(self):
        return self.title

