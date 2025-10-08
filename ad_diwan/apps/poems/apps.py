"""AppConf for ad_diwan.apps.poems"""

from django.apps import AppConfig


# Create your AppConf here.
class PoemsConfig(AppConfig):
    """App Configuration for ad_diwan.apps.poems"""

    label = "ad_diwan_poems"
    name = "ad_diwan.apps.poems"
    default_auto_field = "django.db.models.BigAutoField"
