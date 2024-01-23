from django.shortcuts import render

def blog(request):
    print("[BLOG] Executando outras ações...")
    context = {
        "title": "BLOG",
        "text": "Estamos no BLOG"
    }
    return render(request, "blog/index.html", context)

def exemplo(request):
    context = {
        "title": "EXEMPLO",
        "text": "Estamos no EXEMPLO"
    }
    return render(request, "blog/exemplo.html", context)