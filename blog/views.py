from django.shortcuts import render, render_to_response, get_object_or_404
from blog.models import Blog, Category


def index(request):
    return render(request, 'index.html', {
        'post': Blog.objects.all()[:5]
    })


def views_post(request, slug):
    return render(request, 'view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'view_category.html', {
        'posts': Blog.objects.filter(category=category)[:5]
    })
# Create your views here.
