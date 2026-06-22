from django.shortcuts import render

def index(request):
    return render(request, 'estoque/estoque_index.html')