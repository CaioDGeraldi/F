from django.shortcuts import render

def index(request):
    return render(request, 'launcher/launcher_index.html')