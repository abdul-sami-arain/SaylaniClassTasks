from django.http import HttpResponse


def index(request):
    return HttpResponse("Teachers at Saylani are very Genius & Intelligent.")