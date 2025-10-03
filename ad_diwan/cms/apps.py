"""AppConf for ad_diwan.cms"""

from django.apps import AppConfig


# Create your config here.
class CMSConfig(AppConfig):
    """App configuration for ad_diwan.cms"""

    name = "ad_diwan.cms"
    label = "ad_diwan_cms"
    default_auto_field = "django.db.models.BigAutoField"
