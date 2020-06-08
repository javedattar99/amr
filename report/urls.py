




from django.urls import path
from report.views import reportPage,requestSample,checkout
app_name = 'reports'

urlpatterns = [

    path('<slug:slug>/', reportPage, name='reportpage'),
    path('request-sample/<int:id>/', requestSample, name='samplerequest'),
    path('checkout/<int:id>/', checkout, name='checkout'),


]


