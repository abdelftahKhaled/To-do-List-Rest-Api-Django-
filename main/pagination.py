from rest_framework.pagination import PageNumberPagination


class customPageNumberPagnation(PageNumberPagination):
    max_page_size=2
    page_query_param='page'
    page_size=1 
    page_size_query_param='count'