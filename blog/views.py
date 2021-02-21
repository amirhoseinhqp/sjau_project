from django.shortcuts import render
from .models import blog

# Create your views here.

def blog_list(request):
    Blogs = blog.objects.all()
    context = {
        "Blogs" : Blogs
    }

    return render(request,"blog/blog_list.html",context)
def blog_detail(request, id):
    Blog = blog.objects.get(id=id)
    context = {
        "Blog" : Blog
    }
    return render(request,"blog/blog_detail.html",context)
