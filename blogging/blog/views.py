from django.shortcuts import render
from blog.models import *
from .forms import CommentForm, ContactForm, BlogForm

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts':posts
    }
    return render(request, "index.html",context)

def blog_categories(request, category):
    posts = Post.objects.filter(
        categories__name__contains = category
    ).order_by('-created_on')
    context = {
        "category":category,
        "posts":posts
    }
    return render(request, "category.html", context)




def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                name=form.cleaned_data["name"],
                body=form.cleaned_data["body"],
                email=form.cleaned_data["email"],
                post=post,
            )
            comment.save()
    

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form":form,
    }

    return render(request, "single-standard.html", context)

def about(request):
    return render(request, "page-about.html")

def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact(
                name=form.cleaned_data["name"],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                message=form.cleaned_data['message']
            )
            contact.save()
    context = {
        "form":form
    }

    return render(request,"page-contact.html",context )

def blog(request):
    form = BlogForm()
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            post = Post(
                title=form.cleaned_data["name"],
                body=form.cleaned_data["body"],
                image=form.cleaned_data["image"],
                categories=form.cleaned_data["categories"]
            )
            post.save()
    context = {
        "form":form
    }
    return render(request,'blog.html', context)
