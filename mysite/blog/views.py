from django.shortcuts import render

# Create your views here.

def blog(request):
    context = {
        'nama' : 'Blog kami',
    }
    return render(request, 'blog/blog.html', context)
