"""AppConf for ad_diwan.ui"""

from django.apps import AppConfig


# Create your config here.
class UIConfig(AppConfig):
    """App configuration for ad_diwan.ui"""

    name = "ad_diwan.ui"
    label = "ad_diwan_ui"
    default_auto_field = "django.db.models.BigAutoField"
