from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .utils import Get_Urls


@api_view(["GET"])
def project_overview(request):
    url = Get_Urls(request)[0]
    api_urls = {
        "user friendly links": {
            "      API     ": url + "api/",
            "docs - swagger": url + "docs/",
            "docs -  redoc ": url + "docs-redoc/",
        },
        "API": "api/",
        "docs-swagger": "docs/",
        "docs-redoc  ": "docs-redoc/",
    }
    return Response(api_urls)
