from django.shortcuts import render


posts = [
    {
        'author': 'Tomek',
        'title': 'Post na blogu',
        'content': 'Pierwszy post',
        'date_posted': 'March 24, 2019'
    },
    {
        'author': 'Tomek 2',
        'title': 'Post na blogu 2',
        'content': 'Drugi post',
        'date_posted': 'March 25, 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
