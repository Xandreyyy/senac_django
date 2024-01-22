from django.shortcuts import render
# from django.http import HttpResponse

def blog(request):
    print("[BLOG] Executando outras ações...")
    return HttpResponse("[BLOG] Funcionando!")

def exemplo(request):
    return HttpResponse("[BLOG -> EZEMPLO] Funcionando!")