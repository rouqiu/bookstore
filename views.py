# bookstore views
from django.http import HttpResponse
from django.utils.html import escape, linebreaks
from django.shortcuts import render_to_response, get_object_or_404

from bookstore.models import Genre, Person

def storefront(request):
    return render_to_response("bookstore/storefront.html")
    
def readme(request):
    from os import path
    with open(path.join(path.dirname(path.realpath(__file__)), "README.md"), "rU") as f:
        text = f.read().decode("utf-8")

    try: import markdown
    except ImportError: html = linebreaks(escape(text))
    else: html = markdown.markdown(text)

    return render_to_response("bookstore/markdown.html", dict(content=html))

def author_list(request):
    return HttpResponse("TODO: not yet...")
    
def author_detail(request, author_link):
    author = get_object_or_404(Person, link=author_link)
    return render_to_response("bookstore/author_detail.html", dict(author=author, link=request.build_absolute_uri()))
    
def genre_list(request):
    return HttpResponse("TODO: not yet...")
    
def genre_detail(request, genre_link):
    genre = get_object_or_404(Genre, link=genre_link)
    return render_to_response("bookstore/genre_detail.html", dict(genre=genre, link=request.build_absolute_uri()))
