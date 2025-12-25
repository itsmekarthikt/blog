from django.contrib.auth.models import Group
from django.contrib.auth.models import Group, Permission
from django.shortcuts import get_object_or_404
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.urls import reverse
import logging
from .models import Category, post,Aboutus
from django.core.paginator import Paginator
from .form import ContactForm, Forgot_passwordForm,RegistrationForm,LoginForm,Reset_passwordForm, postForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail

from django.contrib.auth.decorators import login_required,permission_required
# Create your views here.
# Static data for blog posts now moved to database via management command
"""post=[  

        {"id":1,'title':'My first post 1','content':'This is my first blog post content'},
        {"id":2,'title':'My first post 2','content':'This is my second blog post content'},
        {"id":3,'title':'My first post 3','content':'This is my third blog post content'},
        {"id":4,'title':'My first post 4','content':'This is my fourth blog post content'},
        {"id":5,'title':'My first post 5','content':'This is my fifth blog post content'},
        {"id":6,'title':'My first post 6','content':'This is my six blog post content'},
        {"id":7,'title':'My first post 7','content':'This is my seven blog post content'},
        {"id":8,'title':'My first post 8','content':'This is my eight blog post content'},]"""


def home(request):
    blog_title="Latest posts"
    # getting all posts from database
    all_posts=post.objects.filter(is_published=True)

    #pagination styles
    paginater=Paginator(all_posts,5)
    page_number=request.GET.get('page')
    pagination=paginater.get_page(page_number)

    return (render(request, 'blogs/home.html',{'blog_title':blog_title,'paginated_posts':pagination}))

def details(request, slug):
#    to get data from static list now moved to database
#    post_item=next((item for item in post if item["id"] == post_id), None)

#    Logging the retrieved post item for debugging
#    logger=logging.getLogger("Testing")s
#    logger.debug(f"Post item retrieved: {post_item}")

    if not request.user.has_perm('blogs.view_post'):
        messages.error(request, "You do not have permission to view this post, Need to rgister as a User.")
        return redirect('main:home')
    
    try:
            #   Fetching the post item from the database
            post_item=post.objects.get(slug=slug)
            related_Post=post.objects.filter(category=post_item.category).exclude(pk=post_item.id)[:3]


    except post.DoesNotExist:
            return HttpResponse("Post not found, try with proper post id", status=404)
        
    return (render(request, 'blogs/detail.html',{'post_item':post_item,'related_posts':related_Post}))
        
    






def contact(request):
    if request.method=="POST":

                
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')

        form=ContactForm(request.POST)
        logger=logging.getLogger("Testing")


        if form.is_valid():
            form.save()


            logger.debug(f"form data received: {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}")
            Success= "Thank you for contacting us. We have received your message."
            return render(request,'blogs/contact.html',{'form':form ,'Success':Success})
        else:   
            logger.debug("Form is not valid")


        # FORM FIELD IS SENT TO THE TEMPLATE TO RENDER ERRORS IF ANY
        return render(request,'blogs/contact.html',{'form':form })
    

    return render(request,'blogs/contact.html')


def about_us(request):
    content=Aboutus.objects.first()

    if content is None or content.contents is None:
        content="About us content is not available at the moment. Please check back later."

    else:
        content=content.contents


    return render(request,'blogs/about.html',{'content':content})



def register(request):

    form=RegistrationForm()
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            User=form.save(commit=False)
            password=form.cleaned_data['password']
            User.set_password(password)
            User.save()
            # create a group for new registered users
            user_group, _ = Group.objects.get_or_create(name='reader')
            user_group.user_set.add(User)

            success=messages.success(request, "Registration successful. You can now log in.")
            return redirect('main:login')
            
            
        else:
            print("Form is not valid")
 
        
    return render(request,'blogs/register.html',{'form':form})



    

def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('main:dashboard')
            else:
                # Authentication failed
                messages.error(request, "Invalid username or password.")


        # Always return form on POST
        
        return render(request, 'blogs/login.html', {'form': form})

    # GET request
    return render(request, 'blogs/login.html', {'form': form})

@login_required

def dashboard_view(request):
    blog_title="My Posts"
    form = LoginForm(request.POST)
    user_posts=post.objects.filter(user=request.user)
    user=request.user
    
    #pagination styles
    paginater=Paginator(user_posts,5)
    page_number=request.GET.get('page')
    pagination=paginater.get_page(page_number)

    return render(request, 'blogs/dashboard.html',{'form':form,'title':blog_title,'paginated_posts':pagination,})

@login_required
def logout_view(request):
    logout(request)
    return redirect('main:home')


def forgot_password(request):
    form=Forgot_passwordForm()
    if request.method == "POST":

        form = Forgot_passwordForm(request.POST)



        if form.is_valid():

            email = form.cleaned_data['email']
            user_exists = User.objects.filter(email=email).first()


            #before sent email need to create token and link
            if user_exists:
                token=default_token_generator.make_token(user_exists)
                uid= urlsafe_base64_encode(force_bytes(user_exists.pk))
                get_current_site=request.get_host()
                reset_link=f"http://{get_current_site}/reset_password/{uid}/{token}/"
                subject="Password Reset Request"
                message=(f"Hi,\n\nYou requested a password reset. Click the link below to reset your password:\n{reset_link}\n\nIf you did not request this, please ignore this email.\n\nThanks.")
                
                send_mail(
                    subject=subject,
                    message=message,
                    from_email="noreply@gmail.com",
                    recipient_list=[user_exists.email])
                






                    
                # Here you would typically initiate the password reset process
                messages.success(request, " A password reset link has been sent to your mail Adress.")
                return redirect('main:login')
        else:
            return render(request, 'blogs/forgot_password.html', {'form': form})
    return render(request, 'blogs/forgot_password.html')



def reset_password(request, uidb64, token):

    form=Reset_passwordForm()

    if request.method == "POST":
        form = Reset_passwordForm(request.POST)

        if form.is_valid():
            try:
                uid = urlsafe_base64_decode(uidb64).decode()
                user = User.objects.get(pk=uid)

            except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                user = None

            if user is not None and default_token_generator.check_token(user, token):
                new_password = form.cleaned_data['new_password']
                user.set_password(new_password)
                user.save()
                messages.success(request, "Your password has been reset successfully. You can now log in with your new password.")
                return redirect('main:login')
            else:
                messages.error(request, "The reset link is invalid or has expired.")
                return redirect('main:forgot_password')
        else:
            return render(request, 'blogs/reset_password.html', {'form': form})
    return render(request, 'blogs/reset_password.html')

@login_required
@permission_required('blogs.add_post')
def newpost(request):
    categories = Category.objects.all()

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        category = request.POST.get("category")

      

        # save using ModelForm
        form = postForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, "Post created successfully.")
            return redirect('main:dashboard')  # redirect back to dashboard after saving

         
            

        return render(request, "blogs/newpost.html", {
            "form": form,
            "categories": categories
        })

    # GET request
    form = postForm()
    return render(request, "blogs/newpost.html", {
        "form": form,
        "categories": categories
    })



@login_required
@permission_required('blogs.change_post')
def editpost(request, post_id):
    # fetch the post object
    post_obj = get_object_or_404(post, pk=post_id)
    categories = Category.objects.all()

    if request.method == "POST":
        form = postForm(request.POST, request.FILES, instance=post_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully.")
            return redirect('main:dashboard')  # redirect back to dashboard after saving
    else:
        form = postForm(instance=post_obj)

    return render(request, 'blogs/editpost.html', {
        'form': form,
        'post': post_obj,
        'categories': categories
    })


@login_required
@permission_required('blogs.delete_post')
def deletepost(request, post_id):
    post_obj = get_object_or_404(post, pk=post_id)
    if post_obj:
        post_obj.delete()
        messages.success(request, "Post deleted successfully.")
        return redirect('main:dashboard')
    return render(request, 'blogs/dashboard.html', {'post': post_obj})


@login_required
def publish_post(request, post_id):
    post_obj = get_object_or_404(post, pk=post_id)
    if post_obj:
        post_obj.is_published = True
        post_obj.save()
        messages.success(request, "Post published successfully.")
        return redirect('main:dashboard')
    return render(request, 'blogs/dashboard.html', {'post': post_obj})

    
