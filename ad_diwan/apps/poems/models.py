"""Poem model"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.contrib.taggit import ClusterTaggableManager
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import StreamField, RichTextField
from wagtail.models import Page
from wagtail.search import index

from ad_diwan.apps.poems import DIACRITICS, LETTERS
from ad_diwan.cms.blocks import AllBlocks


# Create your models here.
class Poem(Page):
    """Poems"""

    letter = models.CharField(
        max_length=1,
        choices=LETTERS,
        verbose_name=_("letter"),
        help_text=_("Poem letter"),
    )
    diacritic = models.CharField(
        max_length=2,
        choices=DIACRITICS,
        verbose_name=_("diacritic"),
        help_text=_("Poem diacritic"),
    )
    description = models.CharField(
        max_length=256,
        verbose_name=_("description"),
        help_text=_("Poem description"),
    )
    content = RichTextField(
        verbose_name=_("content"),
        help_text=_("Poem content"),
    )
    details = StreamField(
        AllBlocks(),
        verbose_name=_("details"),
        help_text=_("Poem details"),
    )
    tags = ClusterTaggableManager(
        blank=True,
        through="ad_diwan_tags.Tag",
        help_text=_("Tags"),
        verbose_name=_("tags"),
    )

    subpage_types = []
    context_object_name = "poem"
    template = "ad_diwan/poem.html"
    parent_page_types = ["ad_diwan_poets.Poet"]
    api_fields = [
        APIField("letter"),
        APIField("diacritic"),
        APIField("description"),
        APIField("content"),
        APIField("details"),
        APIField("tags"),
    ]
    content_panels = Page.content_panels + [
        FieldPanel("letter"),
        FieldPanel("diacritic"),
        FieldPanel("description"),
        FieldPanel("content"),
        FieldPanel("details"),
        FieldPanel("tags"),
    ]
    search_fields = Page.search_fields + [
        index.FilterField("letter"),
        index.FilterField("diacritic"),
        index.SearchField("description"),
        index.SearchField("content"),
        index.SearchField("details"),
        index.FilterField("tags"),
    ]
