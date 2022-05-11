from django.apps import AppConfig


class RedSocialConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'red_social'

    def ready(self):
        import red_social.signals