from django.shortcuts import render

from django.http import HttpResponse


def Form(request):
    return render(request, "index/form.html", {})


def Upload(request):   # for loop used to loop over the upload function..allows for multiple uploads.
    for count, x in enumerate(request.FILES.getlist("files")):
        def process(f):
            with open('/Documents/Proje/static/img/file_' + str(count), 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
        process(x)
    return HttpResponse("File(s) uploaded!")