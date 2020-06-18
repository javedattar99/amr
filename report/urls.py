




from django.urls import path
from report.views import reportPage,requestSample,checkout,requestInquiry,requestDiscount
app_name = 'reports'

urlpatterns = [

    path('<slug:slug>/', reportPage, name='reportpage'),
    path('request-sample/<int:id>/', requestSample, name='samplerequest'),
    path('request-discount/<int:id>/', requestDiscount, name='discountrequest'),
    path('request-inquiry/<int:id>/', requestInquiry, name='inquiryrequest'),
    path('checkout/<int:id>/', checkout, name='checkout'),


]


