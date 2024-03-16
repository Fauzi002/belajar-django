from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'nama' : 'Atur data ASN dengan mudah',
    }
    return render(request, 'index.html', context)
