from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
# Create your views here.

from .models import Post

def index(request):
    return render(request, 'app/index.html')

def contact(request):
    return render(request, 'app/contact.html')

class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post
