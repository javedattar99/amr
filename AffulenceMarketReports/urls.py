"""AffulenceMarketReports URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from report.views import indexView,categoryPage,publisherPage,aboutus,contactus,latestReports,thankyouPage,searchReports

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexView, name='index'),
    path('latest-reports/', latestReports, name='latestreports'),
    path('about-us/', aboutus, name='aboutus'),
    path('contact-us/', contactus, name='contactus'),
    path('thank-you/', thankyouPage, name='thankyou'),
    path('search/', searchReports, name='searchreport'),

    path('category/<slug:slug>/', categoryPage, name='category'),
    path('publisher/<slug:slug>/', publisherPage, name='publisher'),
    path('industry-analysis/', include('report.urls', namespace='reports')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


