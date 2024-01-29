from django.shortcuts import render
from django.http import Http404
from blog.data import posts

def blog(request):
    print('Blog 4!')
    
    return render(
        request, 
        'blog/index.html',
        {
            # 'text': 'Estamos no Blog',
            'title': ' Blog',
            'posts':posts
        }
    )

def post(request, post_id):
    found_post = None
    
    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break
        
    if found_post is None:
        raise Http404('Post não encontrado!')
        
    context = {
        # 'title': found_post['title'] + ' - ',
        'title': 'Post ' + str(post_id),
        'post': found_post
    }
    
    return render(
        request, 
        'blog/post.html',
        context
    )

def exemplo(request):
    print('Exemplo 4!')
    
    return render(
        request, 
        'blog/exemplo.html',
        {
            'text': 'Estamos no Exemplo',
            'title': ' Exemplo'
        }
    )
