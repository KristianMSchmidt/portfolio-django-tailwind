from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.urls import reverse
from django.http import Http404

from .context import context as ctx
from .forms import ContactForm
from .models import Mail


def home_view(request):

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
            try:
                send_mail(subject, full_message, sender,
                          recipients, fail_silently=False)
                context['email_status'] = 'success'
                return redirect(reverse('home'), context)
            except:
                context['email_status'] = 'failure'
    else:
        form = ContactForm()

    context['form'] = form

    return render(request, 'portfolio/home.html', context)


def project_detail_view(request, projectname):
    try:
        context = ctx['projects'][projectname]
    except:
        raise Http404("No project with this name")
    return render(request, 'portfolio/project_details.html', context)
