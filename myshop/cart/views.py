from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .cart import Cart
from .forms import CartAddProductForm
from .serializers import CartSerializer
from shop.models import Product


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    print(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        print(cd)
        size = cd.get('size')
        cart.add(product=product,
                 size=size,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])

        print(product_id, size)
        print(cart.cart)
        print("Cart contents after adding:", cart.cart)
    else:
        print("Form errors:", form.errors)
    next_url = request.POST.get('next', 'cart:cart_detail')
    return redirect(next_url)


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    print(cart.cart)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        serializer = CartSerializer(cart)
        return JsonResponse(serializer.data, safe=False)

    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'size': item['size'],
            'override': True
        })

    return render(request, 'cart/detail.html', {'cart': cart})
