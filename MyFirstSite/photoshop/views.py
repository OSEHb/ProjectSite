from django.shortcuts import render
from .models import Illustration


def illustrations(request):
    myillustrations = Illustration.objects.all()
    context = {}
    context['myillustrations'] = myillustrations

    return render(request, 'photoshop/ps.html', context)
