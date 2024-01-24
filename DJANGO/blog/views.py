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

def post(request, post_id):
    found_post = None
    for post in posts:
        if post['id'] == post_id:
            found_post = post['id']
            break

    return render(request,
                  "blog/index.html",
                 {
                  "title": "Post",
                  "posts": found_post
                 }
    )

def exemplo(request):
    context = {
        "title": "EXEMPLO",
        "text": "Estamos no EXEMPLO"
    }
    return render(request, "blog/exemplo.html", context)