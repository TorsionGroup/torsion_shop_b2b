"""torsion_b2b URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.apps import apps
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static


urlpatterns = [
    path('admins-view/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('api/', include(apps.get_app_config('oscarapicheckout').urls[0])), # Must be before oscar_api.urls
    path('api/', include('apps.oscarapi.urls')),
    path('creditcards/', include('apps.creditcards.urls')),
    path('', apps.get_app_config('oscar_promotions').urls),
    path('dashboard/promotions/', apps.get_app_config('oscar_promotions_dashboard').urls),
    path('', include(apps.get_app_config('oscar').urls[0])),
    path('news/', include('apps.news.urls')),
    path('aboutus/', include('apps.aboutus.urls')),
    path('contacts/', include('apps.contacts.urls')),
    path('dashboard/accounts/', apps.get_app_config('accounts_dashboard').urls),

]

urlpatterns += i18n_patterns(
    path('', apps.get_app_config('oscar_promotions').urls),
    path('', include(apps.get_app_config('oscar').urls[0])),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)