from django.shortcuts import render

def blog(request):
    print("[BLOG] Executando outras ações...")
    return render(request, "blog/index.html")

def exemplo(request):
    return render(request, "blog/exemplo.html")