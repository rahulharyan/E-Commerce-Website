from django.shortcuts import render,redirect
from base.models import Products,cartModel
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def home(request):
    trend=False
    offer=False
    # count_=cartModel.objects.filter(host=request.user).count()
    # print(count_)
    all_data=Products.objects.all()

    if 'q' in request.GET:
        q=request.GET['q']
        all_data=Products.objects.filter(Q(name__icontains=q)|Q(desc__icontains=q)|Q(category__icontains=q))

    if 't' in request.GET:
        trend=True
        all_data=Products.objects.filter(p_trending=1)

    if'offer' in request.GET:
        offer=True
        all_data=Products.objects.filter(p_offer=1)

    cat = Products.objects.values_list('category', flat=True).distinct()


    if 'cat_form' in request.GET:
        cat_form=request.GET['cat_form']
        print(cat_form.lower())
        all_data=Products.objects.filter(category__iexact=cat_form)


    return render(request , 'home.html', {'all_data': all_data ,'trend':trend,'offer':offer,'cat':cat,})

@login_required(login_url='login_')
def cart(request):
    cart_data=cartModel.objects.filter(host=request.user)
    Totalpay=0
    for i in cart_data:
        Totalpay+=i.totalamount

    

    cart_nav=True
    return render(request,'cart.html',{'cart_nav':cart_nav,'cart_data':cart_data,'Totalpay':Totalpay})

def details(request,pk):
    all_data=Products.objects.filter(id=pk)
    return render(request,'details.html',{'all_data':all_data})

@login_required(login_url='login_')
def addtocart(request,pk):
    product=Products.objects.get(id=pk)

    try:
        cart_item=cartModel.objects.get(name=product.name, host=request.user)
        cart_item.p_quantity+=1
        cart_item.totalamount+=product.price
        cart_item.save()
        return redirect('cart')
    
    except:
        cartModel.objects.create(
            category=product.category,
            name=product.name,
            desc=product.desc,
            price=product.price,
            totalamount=product.price,
            host=request.user
    )

    return redirect('cart')


@login_required(login_url='login_')
def remove(request,pk):
    try:
        cart_product=cartModel.objects.get(id=pk)
        if cart_product.p_quantity > 1:
            cart_product.p_quantity -= 1
            cart_product.save()
        else:
            cart_product.delete()
    except:
        cartModel.DoesNotExist
    return redirect('cart')


def support(request):
    return render(request ,'support.html')




