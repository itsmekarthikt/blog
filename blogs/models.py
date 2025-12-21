from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User



# categories model 

class Category(models.Model):
    name=models.CharField(max_length=50)


    def __str__(self):
        return self.name
    


# Create your models here.
class post(models.Model):


    title=models.CharField(max_length=100)
    content=models.TextField()
    img_url=models.ImageField( null=True,upload_to='posts/images')
    created_at=models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    is_published=models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    @property
    def formated_img(self):
         
       url= self.img_url if self .img_url.__str__().startswith(("http://","https://")) else self.img_url.url
       return url
            
    
class Aboutus(models.Model):
    contents=models.TextField()

class contactus(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()


    
    
   
    

