from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_query_param = "current_page"
    page_size_query_param = "per_page"
    max_page_size = 100  # optional

    def get_paginated_response(self, data):
        return Response({
            "current_page": self.page.number,
            "per_page": self.get_page_size(self.request),
            "total_pages": self.page.paginator.num_pages,
            "total_items": self.page.paginator.count,
            "results": data,
        })
        