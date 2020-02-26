from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, request
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from order.models import ShopCartForm, ShopCart, Order, OrderDetail

@login_required(login_url='/login')
def index(request):
    current_user = request.user
    orders = Order.objects.all().filter(user_id=current_user.id)

    context= {
        'page':'orders',
        'orders':orders,
    }
    return render(request,'order_list.html',context)

@login_required(login_url='/login')
def profil(request):
    current_user = request.user

    return render(request,'profil.html')

@login_required(login_url='/login')
def shop_cart_add(request, proid):
    url = request.META.get('HTTP_REFERER')


    if request.method == 'POST':

            current_user = request.user
            quantity = request.POST['quantity']

            try:
                q1 = ShopCart.objects.get(user_id=current_user.id, product_id=proid)
            except ShopCart.DoesNotExist:
                q1 = None
            if q1 != None:
                q1.quantity = q1.quantity + int(quantity)
                q1.save()
            else:
                data = ShopCart(user_id=current_user.id, product_id=proid, quantity=quantity)
                data.save()
            request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
            messages.success(request, "Ürün sepete eklendi...")
            return HttpResponseRedirect(url)

    return HttpResponseRedirect(reverse('product', args=[proid]))


@login_required(login_url='/login')
def shop_cart_delete(request,id):
    url = request.META.get('HTTP_REFERER')
    ShopCart.objects.filter(id=id).delete()
    messages.success(request,"Ürün silme başarılı...")
    return HttpResponseRedirect(url)

@login_required(login_url='/login')
def shop_cart_list(request):
    current_user = request.user
    shopcart = ShopCart.objects.all().filter(user_id=current_user.id)
    carttotal=0
    for rs in shopcart:
        carttotal+=rs.quantity * rs.product.price

    context= {
        'page': 'cart',
        'shopcart': shopcart,
        'carttotal': carttotal,
    }
    return render(request,'shop_cart_list.html',context)


@login_required(login_url='/login')
def shop_cart_checkout(request):
    current_user=request.user
    shopcart= ShopCart.objects.all().filter(user_id=current_user.id)
    carttotal=0
    for rs in shopcart:
        carttotal+=rs.quantity * rs.product.price

    if request.method=='POST':
        data = Order()
        data.name= request.POST['name']
        data.surname= request.POST['surname']
        data.address=request.POST['address']
        data.city=request.POST['city']
        data.phone = request.POST['phone']
        data.user_id = current_user.id
        data.total = carttotal
        data.save()


        for rs in shopcart:
            detail = OrderDetail()
            detail.order_id= data.id
            detail.product_id = rs.product_id
            detail.user_id = current_user.id
            detail.quantity = rs.quantity
            detail.price = rs.product.price
            detail.total =rs.amount
            detail.save()

        ShopCart.objects.filter(user_id=current_user.id).delete()
        request.session['cart_items']=0
        return HttpResponseRedirect("/order")

    context = {'page':'checkout',
               'shopcart':shopcart,
               'carttotal': carttotal,
    }
    return render(request,'shop_cart_checkout.html',context)

@login_required(login_url='/login')
def order_detail(request,id):
    order = Order.objects.get(pk=id)
    items = OrderDetail.objects.all().filter(order=id)

    context = {
        'page' : 'detail',
        'order': order,
        'items': items,

    }
    return render(request, 'order_detail.html',context)