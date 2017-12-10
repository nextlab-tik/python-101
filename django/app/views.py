from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
# Create your views here.

from .models import Post


# function based view
def index(request):
    return render(request, 'app/index.html')


def contact(request):
    return render(request, 'app/contact.html')


# class based view for model listing
class PostList(ListView):
    model = Post


# class based view for post detail
class PostDetail(DetailView):
    model = Post
