from django.contrib.auth.models import Group, Permission

def create_groups_permissions(*args, **kwargs):
    try:
        # Creating groups properly
        author_group, _ = Group.objects.get_or_create(name='Author')
        reader_group, _ = Group.objects.get_or_create(name='Reader')
        editor_group, _ = Group.objects.get_or_create(name='Editor')

        # Creating permissions
        reader_permissions = [
            Permission.objects.get(codename='view_post'),
        ]

        author_permissions = [
            Permission.objects.get(codename='add_post'),
            Permission.objects.get(codename='view_post'),
            Permission.objects.get(codename='change_post'),
            Permission.objects.get(codename='delete_post'),
        ]

        # For custom permission, use get_or_create correctly
        can_publish_perm, _ = Permission.objects.get_or_create(
            codename='can_publish',
            content_type_id=7,   #  replace with correct content_type_id for your Post model
            name='Can Publish Post'
        )

        editor_permissions = [
            can_publish_perm,
            Permission.objects.get(codename='view_post'),
            Permission.objects.get(codename='change_post'),
            Permission.objects.get(codename='delete_post'),
            Permission.objects.get(codename='view_post'),
        ]

        # Assigning permissions to groups
        reader_group.permissions.set(reader_permissions)
        author_group.permissions.set(author_permissions)
        editor_group.permissions.set(editor_permissions)

        print("Groups and Permissions created successfully")

    except Exception as e:
        print("Error in creating groups and permissions:", e)