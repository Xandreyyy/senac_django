from django.shortcuts import render

def home(request):
    context = {
        "title": "HOME",
        "text": "Estamos na Home"
    }
    return render(request, "home/index.html", context)
