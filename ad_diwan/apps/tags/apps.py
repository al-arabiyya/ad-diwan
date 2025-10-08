"""AppConf for ad_diwan.apps.tags"""

from django.apps import AppConfig


# Create your config here.
class TagsConfig(AppConfig):
    """App configuration for ad_diwan.apps.tags"""

    label = "ad_diwan_tags"
    name = "ad_diwan.apps.tags"
    default_auto_field = "django.db.models.BigAutoField"
