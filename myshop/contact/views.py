from django.shortcuts import render
from .forms import ContactForm, PlantillasForm
from django.core.mail import send_mail, EmailMessage
from django.conf import settings


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print('the form is valid')
            name = request.POST['name']
            email = request.POST['email']
            content = request.POST['content']

            email_message = EmailMessage(
                subject=f'Contact Form from {name}',
                body=content,
                from_email=email,
                to=[settings.EMAIL_HOST_USER],
                reply_to=[email],)
            email_message.send(fail_silently=False),

            print(email)
            return render(request, 'contact/contact_valid.html')
    else:
        form = ContactForm()

    context = {'form': form, }
    return render(request, 'contact/contact.html', context)


def contact_valid(request):
    return render(request, 'contact/contact_valid.html')


def contact_invalid(request):
    return render(request, 'contact/contact_invalid.html')


def info_plantillas(request):
    if request.method == 'POST':
        form = PlantillasForm(request.POST)
        if form.is_valid():

            email = form.cleaned_data['email']
            email_message = EmailMessage(
                subject='Contacto Form de InfoPlantillas',
                body='Quiero informacion sobre plantillas ortopedicas!',
                from_email=settings.EMAIL_HOST_USER,
                to=[settings.EMAIL_HOST_USER],
                reply_to=[email],)

            email_message.send(fail_silently=False)

            confirmation_message = EmailMessage(
                subject='Gracias por contactarnos',
                body='Hola \n\n Gracias por contactarte con Almafuerte ortopedias \n Para poder asistirte de la mejor manera posible, me gustaría hacerte un par de preguntas: \n\n ¿Qué número de calzado usas? \n ¿En qué horario te vendría bien acercarte para realizar las plantillas? \n\n Nuestro horario de atención es de 9: 00 a 18: 00 hs.\n Quedo a la espera de tu respuesta para coordinar la cita.\n Saludos cordiales, Juan de Almafuerte Ortopedias ',
                from_email=settings.EMAIL_HOST_USER,
                to=[email],)
            confirmation_message.send(fail_silently=False)

            return render(request, 'contact/contact_valid.html')
        else:
            print('the form is not valid')
            print(form.errors)
            return render(request, 'contact/contact_invalid.html', {'form': form})
    else:
        form = PlantillasForm()

    context = {'form': form}
    return render(request, 'contact/info_plantillas.html', context)
