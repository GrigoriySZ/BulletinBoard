from django.apps import AppConfig


class UserprofileConfig(AppConfig):
    name = 'profiles'
    verbose_name = 'Профили пользователей'

    def ready(self):
        import profiles.signals
