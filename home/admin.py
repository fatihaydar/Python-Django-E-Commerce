from django.contrib import admin

# Register your models here.
from home.models import Contact, Comment




class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','product','message','rating','status','create_at')
    list_filter = ('status','create_at')
    readonly_fields = ('user','product','message','rating','create_at','subject','email','name')
    list_display_links = ('product',)
    list_editable = ('status',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('mail','konu','status','create_at')
    list_filter = ('status','create_at')
    readonly_fields = ('mail','konu','create_at','mesaj','ad')

admin.site.register(Comment,CommentAdmin)
admin.site.register(Contact,ContactAdmin)
