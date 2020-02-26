from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from home import models
from home.models import Comment
from product.models import Category, Product, ProductImage
from settings.models import Settings
from order.models import ShopCart


def index(request):
    catlist=Category.objects.all()
    products=Product.objects.all()
    settings=Settings.objects.all()
    productlatest=Product.objects.all()[0:5]
    producttop = Product.objects.all()[2:10]
    productone = Product.objects.all()[3:4]
    current_user=request.user
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
    context = {
        'settings': settings,
        'catlist' : catlist,
        'products': products,
        'productlatest': productlatest,
        'producttop': producttop,
        'productone': productone,
    }
    return render(request,'index.html',context)

def prodetail(request,product_id):
    product = Product.objects.get(pk=product_id)
    productimage=ProductImage.objects.filter(product=product_id)
    settings = Settings.objects.all()
    comments = Comment.objects.filter(product_id=product_id, status=1).order_by('-id')
    context = {
        'settings': settings,
        'product': product,
        'productimage': productimage,
        'comments': comments,
    }
    return render(request, 'detail.html', context)

def catproducts(request,id):
    products = Product.objects.all().filter(category=id)
    settings = Settings.objects.all()
    category = Category.objects.all()
    context = {
        'settings': settings,
        'products': products,
        'category': category,
    }
    return render(request, 'katurunler.html', context)

def products(request):
    products = Product.objects.all()[0:20]
    settings = Settings.objects.all()
    category = Category.objects.all()
    context = {
        'settings': settings,
        'products': products,
        'category': category,
    }
    return render(request, 'productsbase.html', context)

def hakkimizda(request):
    settings = Settings.objects.all()
    context = {
        'settings': settings

    }
    return render(request, 'hakkimizda.html', context)

def iletisim(request):
    settings = Settings.objects.all()
    deger = 0
    if (request.method=='POST'):
        ad=request.POST['ad']
        email= request.POST['email']
        konu= request.POST['konu']
        mesaj= request.POST['mesaj']
        veri=models.Contact(ad=ad,mail=email,konu=konu,mesaj=mesaj)
        veri.save()
        deger = "İşleminiz başarıyla gerçekleşmiştir.."
    else:
         deger=""
    context = {
        'deger': deger,
        'settings': settings,

    }
    return render(request, 'iletisim.html', context,locals())


def login_form(request):
    if request.method=="POST":
        next_url=request.POST['next']
        username= request.POST['username']
        password= request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            if next_url:
                return  redirect(next_url)
            else:
                return redirect('/')

        else:
            context = {
                'hata': 'Username od password incorrect',
            }
            return render(request,"login.html",context)

    else:
        return render(request,"login.html")


def join_form():
    return None

def login_out(request):
    logout(request)
    return  redirect('/')

@login_required(login_url='/login')
def comment_add(request,proid):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':

        current_user = request.user
        data = Comment()
        data.product_id = proid
        data.user_id = current_user.id
        data.name = current_user.username
        data.email = current_user.email
        data.subject = request.POST['subject']
        data.message = request.POST['message']
        data.save()
        messages.success(request, "ur review has been sent.")
        return HttpResponseRedirect(url)

    else:
        return HttpResponseRedirect(url)



@login_required(login_url='/login')
def comment_delete(request,id):
    url = request.META.get("HTTP_REFERER")
    Comment.objects.filter(id = id).delete()
    messages.success(request, "ur review has been delete.")
    return HttpResponseRedirect(url)


@login_required(login_url='/login')
def comment_list(request):
    current_user = request.user
    comments = Comment.objects.filter(user=current_user.id).order_by('-id')
    context = {
        'page': 'comments',
        'comments': comments,
    }
    return render(request, "comment_list.html", context)


@login_required(login_url='/login')
def panel(request):
    current_user = request.user

    return render(request, "userpanel.html")