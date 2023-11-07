from django.apps import AppConfig


class AdsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ads"

    def ready(self) -> None:
        import ads.signals  # noqa: F401

        return super().ready()
