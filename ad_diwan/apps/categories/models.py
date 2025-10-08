"""Category model"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.search import index

from ad_diwan.apps.mixins import ChildrenPaginatorMixin
from ad_diwan.cms.blocks import AllBlocks


# Create your models here.
class Category(ChildrenPaginatorMixin, Page):
    """Categories"""

    description = models.CharField(
        max_length=256,
        verbose_name=_("description"),
        help_text=_("Category description"),
    )
    content = StreamField(
        AllBlocks(),
        verbose_name=_("content"),
        help_text=_("Category content"),
    )

    context_object_name = "category"
    template = "ad_diwan/category.html"
    subpage_types = ["ad_diwan_poets.Poet"]
    parent_page_types = ["ad_diwan_indexes.Index"]
    api_fields = [APIField("description"), APIField("content")]
    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("content"),
    ]
    search_fields = Page.search_fields + [
        index.SearchField("description"),
        index.SearchField("content"),
    ]
