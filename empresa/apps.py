from django.apps import AppConfig


class EmpresaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "empresa"


class SeuAppConfig(AppConfig):
    name = 'empresa'

    def ready(self):
        import empresa.models  # Importa seus sinais