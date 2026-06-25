from django.shortcuts import render

def index(request):
    return render(request, 'whatsapp/whatsapp_index.html')