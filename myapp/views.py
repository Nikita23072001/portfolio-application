from django.shortcuts import render
from django.utils import timezone
from .models import Post, AboutMe

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

def home(request):
    about_me = AboutMe.objects.get(pk=1)  # Assuming you have only one AboutMe object
    context = {'about_me': about_me}
    return render(request, 'aboutme.html', context)