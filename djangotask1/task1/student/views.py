from django.http import HttpResponse


def index(request):
    return HttpResponse("Students at Saylani are very Genius & Intelligent.")