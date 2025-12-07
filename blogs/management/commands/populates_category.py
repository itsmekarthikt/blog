from blogs.models import Category
from django.core.management.base import BaseCommand





class Command(BaseCommand):
    help = 'Populates the database with sample blog posts'

    def handle(self, *args, **kwargs):

        # Clear existing data
        Category.objects.all().delete()  

        categories=['Technology', 'Health', 'Lifestyle', 'Travel', 'Food', 'Education', 'Finance', 'Entertainment', 'Sports', 'Science']
        
        for category_name in categories:
           Category.objects.create(name=category_name)

        return self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample blog posts'))