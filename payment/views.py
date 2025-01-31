from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from orders.models import Order
from django.urls import reverse
from orders.tasks import order_created
from cart.cart import Cart
import mercadopago


class PaymentProcessor:
    def __init__(self, order):
        self.order = order

    def checkout(self, request):
        sdk = mercadopago.SDK(settings.MERCADO_PAGO_ACCESS_TOKEN)

        total_cost = self.order.get_total_cost()
        if not isinstance(total_cost, float):

            total_cost = float(total_cost)
        preference_data = {
            "items": [
                {
                    "title": f"Orden {self.order.id}",
                    "quantity": 1,
                    "unit_price": float(total_cost),
                }
            ],
            "back_urls": {
                "success": request.build_absolute_uri(reverse('payment:completed')),
                "failure": request.build_absolute_uri(reverse('payment:canceled')),
                "pending": request.build_absolute_uri(reverse('payment:pending')),
            },
            "auto_return": "approved",
        }
        preference_response = sdk.preference().create(preference_data)
        preference = preference_response["response"]

        request.session['order_id'] = self.order.id

        return redirect(preference['init_point'])


def payment_completed(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)

    order_created.delay(order.id)
    order.paid = True
    order.save()
    cart = Cart(request)
    cart.clear()

    return render(request, 'payment/completed.html', {'order': order})


def payment_canceled(request):
    return render(request, 'payment/canceled.html')


def payment_pending(request):
    return render(request, 'payment_pending.html')
