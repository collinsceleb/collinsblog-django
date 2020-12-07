from operator import attrgetter

from django.shortcuts import render
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger

# Create your views here.
from account.models import Account
from blog.models import BlogPost
from blog.views import get_blog_queryset

BLOG_POSTS_PER_PAGE = 10


def home_view(request):
    # list_of_values = ['One', 'Two', 'Three', 'Four', 'Five']
    # context = {
    #     'some_strings': "This is a context being passed.",
    #     'list_of_values': list_of_values
    # }
    # accounts = Account.objects.all()
    # context = {'accounts': accounts}
    context = {}

    query = ""
    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)
    # blog_posts = sorted(BlogPost.objects.all(), key=attrgetter('date_updated'), reverse=True)
    blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)
    # context['blog_posts'] = blog_posts

    # Pagination
    page = request.GET.get('page', 1)
    blog_posts_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)

    try:
        blog_posts = blog_posts_paginator.page(page)
    except PageNotAnInteger:
        blog_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
    except EmptyPage:
        blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

    context['blog_posts'] = blog_posts
    return render(request, 'home.html', context)
