from django.shortcuts import render,redirect, get_object_or_404
from .models import Contact,Post
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .form import PostForm

# Create your views here.
def home(request):
    allPosts=Post.objects.all()
    context={'allPosts':allPosts}
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method =="POST":
        name=request.POST['name']
        email=request.POST['email']
        content=request.POST['content']
        contactus=Contact(name=name,email=email,content=content)
        contactus.save()
        messages.success(request,"query sent successfully")
    return render(request,'contact.html')


def loginuser(request):
    if request.method=="POST":
        loginUsername=request.POST['name']
        loginPassword=request.POST['password']
        user=authenticate(request,username=loginUsername,password=loginPassword)
        if user is not None:
            login(request,user)
            messages.success(request,"user logged in successfully")
            return redirect('home')
        
        else:
            messages.error(request,"username or password is wrong")
            return redirect('home')
    return render(request,'login.html')


def register(request):
    if request.method =="POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        password_repeat=request.POST['password_repeat']

        #check for error inputs

        #save user
        myuser=User.objects.create_user(username=name,email=email,password=password)
        myuser.save()
        return redirect('login')
    return render(request,'register.html')

def myblogs(request):
    author=request.user
    myPost=Post.objects.filter(author=author)
    context={'myPost':myPost}
    return render(request,'myblogs.html',context)



def logoutuser(request):
    messages.success(request,"user logged out successfully")
    logout(request)
    return redirect('home')

def createblogs(request):
    if request.method=="POST":
        author=request.POST['name']
        title=request.POST['title']
        content=request.POST['content']
        slug=title.replace(" ","-")
        blog=Post(author=author,title=title,content=content,slug=slug)
        blog.save()
        messages.success(request,"new blog created!")
    return render(request,'createblogs.html')

def blogpost(request,slug):
    blog=Post.objects.filter(slug=slug)
    context={'blog':blog}
    
    return render(request,'blogpost.html',context)

def delete_post(request, sno):
    post = get_object_or_404(Post, sno=sno)
    if request.method == "POST":
        post.delete()
        return redirect('/myblogs')
    return render(request, 'confirm_delete.html', {'post': post})


def edit_post(request, sno):
    post = get_object_or_404(Post, sno=sno)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/myblogs')
    else:
        form = PostForm(instance=post)

    return render(request, 'edit.html', {'form': form, 'post': post})



