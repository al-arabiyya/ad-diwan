"""Poet model"""

from django_countries.fields import CountryField
from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.search import index
from wagtail.images import get_image_model

from ad_diwan.apps.mixins import ChildrenPaginatorMixin
from ad_diwan.cms.blocks import AllBlocks


Image = get_image_model()


# Create your models here.
class Poet(ChildrenPaginatorMixin, Page):
    """Poets"""

    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name=_("birth date"),
        help_text=_("Poet birth date"),
    )
    death_date = models.DateField(
        null=True,
        blank=True,
        verbose_name=_("death date"),
        help_text=_("Poet death date"),
    )
    image = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
        verbose_name=_("image"),
        help_text=_("Poet image"),
    )
    country = CountryField(
        null=True,
        blank=True,
        verbose_name=_("country"),
        help_text=_("Poet country"),
    )
    description = models.CharField(
        max_length=256,
        verbose_name=_("description"),
        help_text=_("Poet description"),
    )
    details = StreamField(
        AllBlocks(),
        verbose_name=_("details"),
        help_text=_("Poet details"),
    )

    context_object_name = "poet"
    template = "ad_diwan/poet.html"
    subpage_types = ["ad_diwan_poems.Poem"]
    parent_page_types = ["ad_diwan_categories.Category"]
    api_fields = [
        APIField("birth_date"),
        APIField("death_date"),
        APIField("image"),
        APIField("country"),
        APIField("description"),
        APIField("details"),
    ]
    search_fields = Page.search_fields + [
        index.FilterField("birth_date"),
        index.FilterField("death_date"),
        index.FilterField("country"),
        index.SearchField("description"),
        index.SearchField("details"),
    ]
    content_panels = Page.content_panels + [
        FieldPanel("birth_date"),
        FieldPanel("death_date"),
        FieldPanel("image"),
        FieldPanel("country"),
        FieldPanel("description"),
        FieldPanel("details"),
    ]
