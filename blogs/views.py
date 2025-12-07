from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.urls import reverse
import logging
from .models import post,Aboutus
from django.core.paginator import Paginator
from .form import ContactForm
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
    all_posts=post.objects.all()

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
    try:
    #   Fetching the post item from the database
        post_item=post.objects.get(slug=slug)
        related_Post=post.objects.filter(category=post_item.category).exclude(pk=post_item.id)[:3]

    except post.DoesNotExist:
        return HttpResponse("Post not found, try with proper post id", status=404)
    
    return (render(request, 'blogs/detail.html',{'post_item':post_item,'related_posts':related_Post}))


def name(request, name):
    return HttpResponse(f"Welcome to the Blog Details Page, your name is {name}")

def old_url_redirect(request):
    return redirect(reverse("main:new_url_page"))

def new_url_view(request):
    return HttpResponse(" this is new url redirected from old url")

def contact(request):
    if request.method=="POST":

                
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')

        form=ContactForm(request.POST)
        logger=logging.getLogger("Testing")


        if form.is_valid():

            logger.debug(f"form data received: {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}")
            Success= "Thank you for contacting us. We have received your message."
            return render(request,'blogs/contact.html',{'form':form ,'Success':Success})
        else:   
            logger.debug("Form is not valid")


        # FORM FIELD IS SENT TO THE TEMPLATE TO RENDER ERRORS IF ANY
        return render(request,'blogs/contact.html',{'form':form ,'name':name,'email':email,'message':message})
    

    return render(request,'blogs/contact.html')


def about_us(request):
    content=Aboutus.objects.first().contents
    return render(request,'blogs/about.html',{'content':content})