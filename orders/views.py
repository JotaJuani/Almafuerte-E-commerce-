from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.shortcuts import render, get_object_or_404
from payment.views import PaymentProcessor
from .serializers import OrderSerializer
from django.http import JsonResponse


def order_detail_view(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return JsonResponse({'error': 'Order not found'}, status=404)

    order_data = OrderSerializer(order).data
    for item in order_data.get('items', []):
        item['price'] = str(item['price'])
    return JsonResponse(order_data)


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=str(item['price']),
                                         quantity=item['quantity'],
                                         size = request.POST.get('size', ''))

            request.session['order_id'] = int(order.id)
            cart_serialized = {
                key: {
                    'quantity': value['quantity'],
                    'price': str(value['price']),
                    'product': str(value['product']),
                    'size': str(value['size']),
                    'total_price': str(value['total_price'])}
                for key, value in cart.cart.items()
            }
            request.session['cart'] = cart_serialized
            print("Session data:", request.session.items())
            payment_processor = PaymentProcessor(order)

            return payment_processor.checkout(request)

    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart,
                   'form': form})


def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/detail.html',
                  {'order': order})
