"""Views for ad_diwan.ui"""

from typing import Any, Dict

from django.db.models import QuerySet
from django.views import generic
from django_filters.views import FilterView
from wagtail.contrib.search_promotions.models import Query
from wagtail.models import Page

from ad_diwan.apps.poems.models import Poem


# Create your views here.
class SearchView(generic.ListView):
    """Search View"""

    model = Page
    template_name = "ad_diwan/search.html"
    context_object_name = "search_results"
    queryset = Page.objects.live().public()

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        """Search and add to context"""

        return {
            **super().get_context_data(**kwargs),
            "search_query": self.request.GET.get("search", None),
            "search_results": self.get_search_results(),
        }

    def get_search_results(self):
        """Search and return results"""

        queryset = self.get_queryset()
        search_query = self.request.GET.get("search", None)

        search_results = queryset.none()

        if search_query:
            search_results = queryset.search(search_query)

            # Log the query so Wagtail can suggest promoted results
            Query.get(search_query).add_hit()

        return search_results


class PoemSearchView(FilterView, generic.ListView):
    """Search View"""

    template_name = "ui/search.html"
    context_object_name = "search_results"
    queryset = Poem.objects.live().public()
    filterset_fields = ["letter", "diacritic", "tags"]

    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        """Search news articles"""

        query = self.request.GET.get("search", None)
        queryset = self.get_queryset()

        if query:
            queryset = self.filterset.qs.search(query)

            # Log the query so Wagtail can suggest promoted results
            Query.get(query).add_hit()

        return {
            **super().get_context_data(**kwargs),
            "search_query": query,
            "search_results": queryset,
        }

    def get_queryset(self) -> QuerySet[Poem]:
        """Check if search query is provided to return the queryset else none"""

        query = self.request.GET.get("search", None)

        if query:
            # Return filtered queryset
            return super().get_queryset()

        # No search query, no results
        else:
            return Poem.objects.none()
