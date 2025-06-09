# blog/views.py
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category


def index(request):
    """Главная страница с лентой записей"""
    post_list = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    ).select_related('author', 'category', 'location').order_by('-pub_date')[:5]
    
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    """Детальная страница поста"""
    post = get_object_or_404(
        Post.objects.select_related('author', 'category', 'location'),
        id=post_id,
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )
    
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    """Страница с постами конкретной категории"""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    
    post_list = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    ).select_related('author', 'location').order_by('-pub_date')
    
    return render(request, 'blog/category.html', {
        'category': category,
        'post_list': post_list
    })
