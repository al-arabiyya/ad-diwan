"""AppConf for ad_diwan.apps.poets"""

from django.apps import AppConfig


# Create your AppConf here.
class PoetsConfig(AppConfig):
    """App Configuration for ad_diwan.apps.poets"""

    label = "ad_diwan_poets"
    name = "ad_diwan.apps.poets"
    default_auto_field = "django.db.models.BigAutoField"
