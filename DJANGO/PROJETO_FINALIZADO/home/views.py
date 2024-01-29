from django.shortcuts import render

# from django.http import HttpResponse

# Create your views here.

def home(request):
    print('Home!')
    
    context = {
        'text': 'Estamos na Home',
        'title': ' Home'
    }
    
    return render(
        request, 
        'home/index.html',
        context,
    )