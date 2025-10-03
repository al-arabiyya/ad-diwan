"""URL Configuration for ad_diwan.api"""

from django.urls import path
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.contrib.redirects.api import RedirectsAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet
from wagtail.images.api.v2.views import ImagesAPIViewSet

# Wagtail Built-in APIs
router = WagtailAPIRouter("wagtail-api")
router.register_endpoint("pages", PagesAPIViewSet)
router.register_endpoint("images", ImagesAPIViewSet)
router.register_endpoint("documents", DocumentsAPIViewSet)
router.register_endpoint("redirects", RedirectsAPIViewSet)

urlpatterns = [
    path("", router.urls),
]
