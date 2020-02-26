from django.urls import path

from . import views
app_name='home'
urlpatterns = [
    path('',views.index,name='index'),
    path('urunler/',views.products,name='index'),
    path('hakkimizda/',views.hakkimizda,name='index'),
    path('iletisim/',views.iletisim,name='index'),
    path('category/<int:id>',views.catproducts,name='index'),
    path('urunler/category/<int:id>',views.catproducts,name='index'),
    path('login',views.login_form),
    path('join',views.join_form),
    path('logout',views.login_out),
    path('<int:product_id>/',views.prodetail,name='index'),
    path('addcomment/<int:proid>', views.comment_add, name='addcomment'),
    path('deletecomment/<int:id>', views.comment_delete, name='deletecomment'),
    path('comments/', views.comment_list, name='comments'),

]