from django.shortcuts import render
from .models import blog , tag , category , comments
from .forms import CommentForm
from django.core.paginator import Paginator

# Create your views here.

def blog_list(request):
    Blogs = blog.objects.all()
    paginator = Paginator(Blogs,3)
    page_number = request.GET.get('page')
    Blog_list = paginator.get_page(page_number)
    context = {
        "Blog_list" : Blog_list
    }

    return render(request,"blog/blog_list.html",context)
def blog_detail(request, id):
    Blog = blog.objects.get(id=id)
    Tags = tag.objects.all().filter(blogs=Blog)
    Recent = blog.objects.all().order_by("created_at")[:5]
    Category = category.objects.all()
    Comments = comments.objects.all().filter(Blog=Blog)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            new_email = form.cleaned_data["email"]
            new_message = form.cleaned_data["message"]

            new_comment = comments(Blog=Blog,name=new_name,email=new_email,message=new_message)
            new_comment.save()
    context = {
        "Blog" : Blog,
        "Tags" : Tags,
        "Recent" : Recent,
        "Category" : Category,
        "Comments" : Comments,
    }
    return render(request,"blog/blog_detail.html",context)

def blog_tag(request,tag):
    Blogs = blog.objects.filter(tags__slug=tag)
    context = {
        "Blogs" : Blogs
    }

    return render(request,"blog/blog_list.html",context)

def blog_category(request,category):
    Blogs = blog.objects.filter(Category__slug=category)
    context = {
        "Blogs" : Blogs
    }

    return render(request,"blog/blog_list.html",context)

def search(request):
    if request.method == "GET":
        q = request.GET.get("search")
    Blog_list = blog.objects.filter(title__icontains=q)
    return render(request,"blog/blog_list.html",{"Blog_list":Blog_list})
