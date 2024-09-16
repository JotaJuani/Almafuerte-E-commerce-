from django.shortcuts import render, get_object_or_404
from shop.models import Category,   Product
from cart.forms import CartAddProductForm, CartAddProductSizeForm
from .serializers import ProductSerializer
from django.http import JsonResponse


def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    related_products = Product.objects.filter(
        category__in=product.category.all()).exclude(id=product.id)

    context = {
        'product': product,
        'related_products': related_products}

    print('Productos Relacionados', related_products)

    return render(request, 'shop/product/detail.html', context)


def home(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).order_by('?')
    categories_side = Category.objects.all()
    categories = Category.objects.order_by('?')
    show_all = request.GET.get('show_all', False) == 'True'

    if show_all:
        categories = categories_side
    else:
        categories = categories[:6]
        products = products[:6]

    return render(request, 'shop/product/home.html',
                  {'categories': categories,
                   'products': products,
                   'show_all': show_all,
                   'categories_side': categories_side})


def category_list(request):
    categories = Category.objects.order_by('?')
    show_all = request.GET.get('show_all', False) == 'True'

    if not show_all:
        categories = categories[:6]

    print(categories)

    return render(request, 'shop/product/category_list.html',
                  {'categories': categories,
                   'show_all': show_all})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).order_by('?')

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    show_all = request.GET.get('show_all', False)

    if not show_all:
        products = products[:6]

    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'show_all': show_all})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    size_product_form = CartAddProductSizeForm()
    related_products = Product.objects.filter(
        category__in=product.category.all()
    ).exclude(id=product.id)

    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'size_product_form': size_product_form,
                   'related_products': related_products})


def search_products(request):
    search_term = ""
    if 'search' in request.GET:
        search_term = request.GET['search']
        products = Product.objects.filter(name__icontains=search_term)
    else:
        products = Product.objects.all()
    product_data = ProductSerializer(products, many=True).data

    return render(request,
                  'shop/product/searched.html',
                  {'products': products,
                   'search_term': search_term})


def about(request):
    return render(request, 'shop/product/about.html')
