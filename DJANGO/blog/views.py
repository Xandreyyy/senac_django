from django.shortcuts import render
from blog.data import posts

def blog(request):
    print("[BLOG] Executando outras ações...")
    return render(request,
                  "blog/index.html",
                 {
                  "title": "Blog",
                  "posts": posts   
                 }
    )

def post(request, id):
    print("[POST] Executando outras ações...")
    return render(request,
                  "blog/index.html",
                 {
                  "title": "Post",
                  "posts": posts   
                 }
    )

def exemplo(request):
    context = {
        "title": "EXEMPLO",
        "text": "Estamos no EXEMPLO"
    }
    return render(request, "blog/exemplo.html", context)