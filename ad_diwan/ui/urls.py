"""URLConf for ad_diwan.ui"""

from django.urls import path

from ad_diwan.ui import views

# Create your URLConf here.
app_name = "ad_diwan"

urlpatterns = [
    path("search/", views.SearchView.as_view(), name="search"),
]
