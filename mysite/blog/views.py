from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

def home(request):
	return render(request, 'blog/home.html',{})

def upload(request):
	return render(request, 'blog/upload.html', {})


def index(request):
	return render(request, 'blog/index.html', {})

def home(request):
    return render(request,"blog/home.html")

def events(request):
    return render(request,"blog/events.html")
def hala(request):
    return render(request,"blog/hala.html")


def enter(request):
    return render(request,"blog/enter.html")

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('events')

	else:
		form = UserCreationForm()
		args={'form': form}
		return render(request, 'blog/register.html',args)
