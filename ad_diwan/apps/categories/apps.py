"""AppConf for ad_diwan.apps.categories"""

from django.apps import AppConfig


# Create your AppConf here.
class CategoriesConfig(AppConfig):
    """App Configuration for ad_diwan.apps.categories"""

    label = "ad_diwan_categories"
    name = "ad_diwan.apps.categories"
    default_auto_field = "django.db.models.BigAutoField"
