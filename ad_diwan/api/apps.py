"""AppConf for ad_diwan.api"""

from django.apps import AppConfig


# Create your AppConf here.
class APIConfig(AppConfig):
    """App Configuration for ad_diwan.api"""

    name = "ad_diwan.api"
    label = "ad_diwan_api"
    default_auto_field = "django.db.models.BigAutoField"
