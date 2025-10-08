"""Index model"""

from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.search import index

from ad_diwan.cms.blocks import AllBlocks


# Create your models here.
class Index(Page):
    """Index page"""

    content = StreamField(
        AllBlocks(),
        verbose_name=_("content"),
        help_text=_("Page content"),
    )

    context_object_name = "index"
    template = "ad_diwan/index.html"
    parent_page_types = ["home.Home"]
    api_fields = [APIField("content")]
    subpage_types = ["ad_diwan_categories.Category"]
    content_panels = Page.content_panels + [FieldPanel("content")]
    search_fields = Page.search_fields + [index.SearchField("content")]
