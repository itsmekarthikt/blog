from django.apps import AppConfig
from django.db.models.signals import post_migrate



class BlogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogs'

    def ready(self):
        from .signal import create_groups_permissions
        post_migrate.connect(create_groups_permissions, sender=self)