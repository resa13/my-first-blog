from django.shortcuts import render
from .models import Post
from django.utils import timezone


# Create your views here.
def post_list(request):
    #this was the basic form
    #return render(request, 'blog/post_list.html', {})
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
