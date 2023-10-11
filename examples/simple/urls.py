from django.urls import include, path, re_path
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic import TemplateView

from books import urls as books_urls
from search_indexes import urls as search_index_urls

__all__ = ('urlpatterns',)

admin.autodiscover()

urlpatterns = []
urlpatterns_args = [
    path('admin/', include(admin.site.urls)),
]

urlpatterns_args += [
    # Books URLs
    path('books/', include(books_urls)),

    # Search URLs
    path('search/', include(search_index_urls)),

    # Home page
    path('', TemplateView.as_view(template_name='home.html')),
]

urlpatterns += urlpatterns_args[:]

# Serving media and static in debug/developer mode.
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

    if settings.DEBUG_TOOLBAR is True:
        import debug_toolbar

        urlpatterns = [
            path('__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
