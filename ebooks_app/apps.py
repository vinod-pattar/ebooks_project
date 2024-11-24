from django.apps import AppConfig


class EbooksAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ebooks_app'

    def ready(self):
        import ebooks_app.signals 
