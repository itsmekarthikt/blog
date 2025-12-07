from django.contrib import admin
from .models import post,Category,Aboutus

# Register your models here.

class postAdmin(admin.ModelAdmin):
    list_display=('title','content')
    search_fields=['title','content']
    list_filter=('category','created_at')


class aboutAdmin(admin.ModelAdmin):
    list_display=('contents',)
    

admin.site.register(post,postAdmin)
admin.site.register(Aboutus,aboutAdmin)
admin.site.register(Category)
