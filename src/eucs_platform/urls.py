from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.urls import include, path
from django.conf.urls import url
import profiles.urls
import accounts.urls
import projects.urls
import resources.urls
import events.urls
import contact.urls
from . import views
from rest_framework import routers


# Personalized admin site settings like title and header
admin.site.site_title = "Eucs_Platform Site Admin"
admin.site.site_header = "Eucs_Platform Administration"

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
    url(r'^rest-auth/', include('rest_auth.urls')),
    #url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    path("", views.home, name="home"),
    path("curated/", views.curated,name="curated"),
    path("imprint/", views.imprint,name="imprint"),
    path("terms/", views.terms,name="terms"),
    path("privacy/", views.privacy,name="privacy"),
    path("faq/", views.faq,name="faq"),
    path("subscribe/", views.subscribe,name="subscribe"),
    path("moderation/", views.moderation,name="moderation"),
    path("criteria/", views.criteria,name="criteria"),
    path("home_autocomplete/", views.home_autocomplete,name="home_autocomplete"),
    path("development/", views.development,name="development"),
    path("about/", views.AboutPage.as_view(), name="about"),
    path("users/", include(profiles.urls)),
    path("admin/", admin.site.urls),
    path("", include(contact.urls)),
    path("", include(accounts.urls)),
    path("", include(projects.urls)),
    path("", include(resources.urls)),
    path('', include('blog.urls')),
    path("", include(events.urls)),
    path('summernote/', include('django_summernote.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^reviews/', include('reviews.urls')),
    url(r'^citizen-science-resources-related-to-the-covid19-pandemic/', RedirectView.as_view(url='blog/2020/03/31/citizen-science-resources-related-covid19-pandemic/')),
    path('', include(router.urls)),

    path('rest-auth/password/reset/', accounts.views.PasswordResetView.as_view(), name='password_reset_confirm'),
    path(
        "rest-auth/password-reset-done/",
        accounts.views.PasswordResetDoneView.as_view(),
        name="password-reset-done",
    ),
    url(
        r"^rest-auth/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$",
        accounts.views.PasswordResetView.as_view(),
        name="password_reset_confirm",
    ),

]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Include django debug toolbar if DEBUG is on
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
