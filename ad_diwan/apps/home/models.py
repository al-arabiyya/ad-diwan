"""Home page"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.panels import FormSubmissionsPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.search import index

from ad_diwan.cms.blocks import MediaBlock


# Create your models here.
class Home(Page):
    """Home page"""

    context_object_name = "home"
    template = "ad_diwan/base.html"
    parent_page_types = ["wagtailcore.Page"]


# About and Contact pages have no migrations
# You can delete them if you do not need them, before running makemigrations.
class About(Page):
    """About page"""

    content = StreamField(
        MediaBlock(),
        null=True,
        blank=True,
        verbose_name=_("content"),
        help_text=_("Page content"),
    )

    template = "ad_diwan/about.html"
    context_object_name = "about"
    page_description = _("About us page")
    content_panels = Page.content_panels + [FieldPanel("content")]
    parent_page_types = ["home.Home"]
    subpage_types = []


class FormField(AbstractFormField):
    page = ParentalKey(
        "home.Contact",
        on_delete=models.CASCADE,
        related_name="form_fields",
    )


class Contact(AbstractEmailForm):
    """Contact page"""

    content = StreamField(
        MediaBlock(),
        null=True,
        blank=True,
        verbose_name=_("content"),
        help_text=_("Page content"),
    )
    message = RichTextField(
        null=True,
        blank=True,
        verbose_name=_("message"),
        help_text=_("Message to display after form submission"),
    )

    template = "ad_diwan/contact.html"
    context_object_name = "contact"
    page_description = _("Contact us page")
    parent_page_types = ["home.Home"]
    subpage_types = []

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("content"),
        FieldPanel("message"),
        FormSubmissionsPanel(),
        InlinePanel("form_fields"),
        MultiFieldPanel(
            [
                FieldPanel("subject"),
                FieldRowPanel([FieldPanel("from_address"), FieldPanel("to_address")]),
            ],
            "Email",
        ),
    ]
    search_fields = AbstractEmailForm.search_fields + [
        index.SearchField("content"),
        index.SearchField("message"),
    ]
