from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from .settings import MEDIA_ROOT, STATIC_ROOT

schema_view = get_schema_view(
    openapi.Info(
        title="Cars API", default_version="v1", description="API to fetch and rate cars"
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

docs_urlpatterns = [
    path(
        "docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger"
    ),
    path(
        "docs-redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]

statics_urlpatterns = [
    url(r"^media/(?P<path>.*)$", serve, {"document_root": MEDIA_ROOT}),
    url(r"^static/(?P<path>.*)$", serve, {"document_root": STATIC_ROOT}),
]

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        re_path(r"^api-auth/", include("rest_framework.urls")),
    ]
    + docs_urlpatterns
    + statics_urlpatterns
)
