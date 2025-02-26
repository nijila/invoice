"""loun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# django rest framework
from rest_framework.routers import DefaultRouter

# djoser
from djoser.views import UserViewSet

#local
from finance.views import InvoiceViewSet
from payments.views import HomePageView, stripe_config, create_checkout_session, invoicelist, sendmail, paymentsuccess

admin.site.site_header = 'Invoice Management System'
admin.site.site_title = 'Invoice Management System'
admin.site.index_title = 'Home'
admin.site.site_url = None

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('invoice', InvoiceViewSet, basename='invoice')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('djoser.urls.jwt')),
    path('api/', include('rest_framework.urls')),
    path('payment/', HomePageView, name='home'),
    path('config/', stripe_config),
    path('create-checkout-session/', create_checkout_session),
    path('invoicelist/', invoicelist),
    path('api/sendmail/', sendmail, name='sendmail'),
    path('s/', include('shortener.urls')),
    path('paymentsuccess/<invoice_id>',paymentsuccess,)
   ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
