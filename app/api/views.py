from rest_framework.decorators import api_view
from rest_framework.response import Response

from project.utils import Get_Urls


@api_view(["GET"])
def api_overview(request):
    urls = Get_Urls(request)
    api_urls = {
        "user friendly links": {
            "  Add  ": urls[0] + "cars/" + urls[1] + " [POST]",
            " List  ": urls[0] + "cars/" + urls[1] + " [GET]",
            " Rate  ": urls[0] + "rate/" + urls[1] + " [POST]",
            "Popular": urls[0] + "popular/" + urls[1] + " [GET]",
        },
        "Add": "cars/",
        "List": "cars/",
        "Rate": "rate/",
        "Popular": "popular/",
    }
    return Response(api_urls)
