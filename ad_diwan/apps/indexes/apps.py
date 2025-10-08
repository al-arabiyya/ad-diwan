"""AppConf for ad_diwan.apps.indexes"""

from django.apps import AppConfig


# Create your AppConf here.
class IndexConfig(AppConfig):
    """App Configuration for ad_diwan.apps.indexes"""

    label = "ad_diwan_indexes"
    name = "ad_diwan.apps.indexes"
    default_auto_field = "django.db.models.BigAutoField"
