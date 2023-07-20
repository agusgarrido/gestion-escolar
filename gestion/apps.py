from django.apps import AppConfig


class GestionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gestion'

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gestion'

    def ready(self):
        from django.contrib.auth.models import User
        import os

        superuser_username = os.getenv('DJANGO_SUPERUSER_USERNAME')
        superuser_password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

        if superuser_username and superuser_password:
            user, _ = User.objects.get_or_create(username=superuser_username)
            user.set_password(superuser_password)
            user.is_superuser = True
            user.is_staff = True
            user.save()