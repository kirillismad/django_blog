from rest_framework.filters import SearchFilter as BaseSearchFilter


class SearchFilter(BaseSearchFilter):
    search_param = 'q'

    def filter_queryset(self, request, queryset, view):
        return super().filter_queryset(request, queryset, view)

    def get_search_terms(self, request):
        params = request.GET.get(self.search_param, '')
        return params.replace(',', ' ').split()
