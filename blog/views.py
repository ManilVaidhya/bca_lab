from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    return render(request, 'blog/index.html')


def contact(request):
    return render(request, 'blog/contact.html')

def blog(request):
    context={
        'post': Post.objects.all()
    }
    return render(request, 'blog/blog.html',context)
