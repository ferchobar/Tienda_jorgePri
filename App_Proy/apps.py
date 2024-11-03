from django.apps import AppConfig


class AppProyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'App_Proy'
    def ready(self):
        import App_Proy.signals  # Importa el archivo signals.py
       # import App_Proy.validators