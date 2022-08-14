from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.urls import reverse
from django.http import Http404

from .context import context as ctx
from .forms import ContactForm
from .models import Mail
from django.contrib import messages


def home_view(request, nav_id=""):

    context = ctx
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            sender = form.cleaned_data['sender']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipients = ['kmollerschmidt@gmail.com', 'krms@kvuc.dk']
            full_message = f"Portfolio message from {name} with email {sender}: {message}"
            Mail.objects.create(name=name, sender=sender,
                                subject=subject, message=message)
            # try:
            #     send_mail(subject, full_message, sender,
            #               recipients, fail_silently=False)
            #     messages.success(
            #         request, "Your message was send. I'll reply as soon as possible.")
            #     return redirect(reverse('home'))
            # except:
            #     messages.error(
            #         request, 'Your message was not send. Try again or send a regular email to the address shown below.')
            messages.error(
                request, 'There was an error. Please send your message to kmollerschmidt@gmail.com.')
    else:
        form = ContactForm()

    context['form'] = form
    context['nav_id'] = nav_id
    return render(request, 'portfolio/home.html', context)
