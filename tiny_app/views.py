from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse

from .forms import ContactForm, SignUpForm
from .models import SignUp


def home(request):
    title = 'Sign Up Now'
    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form
    }
    if form.is_valid():
        instance = form.save(commit=False)

        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name
        if not instance.full_name:
            instance.full_name = "Justin"
        instance.save()
        context = {
            "title": "Thank you"
        }

    if request.user.is_authenticated() and request.user.is_staff:

        queryset = SignUp.objects.all().order_by('-timestamp')  # .filter(full_name__iexact="Justin")
        # print(SignUp.objects.all().order_by('-timestamp').filter(full_name__iexact="Justin").count())
        context = {
            "queryset": queryset
        }

    return render(request, "home.html", context)


def contact(request):
    title = 'Contact Us'
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        subject = 'Tiny Spot contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email]  # Add more emails as a string if needed
        contact_message = "%s: %s via %s" % ( 
                form_full_name,
                form_message,
                form_email)
        send_mail(subject,
                contact_message,
                from_email,
                to_email,
                fail_silently=False)

    context = {
        "form": form,
        "title": title,
    }
    return render(request, "forms.html", context)


def form(request):
    return render(request, "form.html", {})


def upload(request):  # for loop used to loop over the upload function..allows for multiple uploads.
    for count, x in enumerate(request.FILES.getlist("files")):
        def process(f):
            with open('/static/img/file_' + str(count), 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
        process(x)
    return HttpResponse("File(s) uploaded!")
