from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Orden nº{order.id}'
    message = f'Señor/a {order.first_name},\n\n' \
    f'Su orden se ha  realizado correctamente.' \
    f'Su numero de orden es : {order.id}'
    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [order.email])
    return mail_sent

