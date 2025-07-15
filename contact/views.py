from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            content = contact_form.cleaned_data['content']
            
            # Configurar y enviar el email
            try:
                email_obj = EmailMessage(
                    "La Cafetería: Nuevo mensaje de contacto",
                    "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                    "no-contestar@inbox.mailtrap.io",
                    [settings.EMAIL_HOST_USER],
                    reply_to=[email]
                )
                email_obj.send()
                # Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact') + '?ok')
            except Exception as e:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact') + '?fail')
    
    return render(request, 'contact/contact.html', {'form': contact_form})
