from django.contrib import admin

# Register your models here.
from order.models import Order, OrderDetail


class OrderAdmin(admin.ModelAdmin):
    list_display = ('status','name','city','phone','create_at')
    list_filter = ('status','create_at')

class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('user','order','total','create_at')
    list_filter = ('order','user')




admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail,OrderDetailAdmin)