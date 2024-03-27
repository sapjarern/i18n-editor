from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param='limit'

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'results': data,
        })
