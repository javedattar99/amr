




from django.shortcuts import render,get_object_or_404
from .forms import LeadForm,CheckoutForm
from .models import Category,Report,Publisher
from django_countries import countries
from django.core.mail import send_mail
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.


def indexView(request):
    reports = Report.objects.all()
    return render(request,'base/index.html',{'reports': reports})


def reportPage(request,slug):
    report = get_object_or_404(Report, slug=slug)
    return render(request,'report/reportpage.html',{'report':report})


def requestSample(request,id):
    report = get_object_or_404(Report, id=id)
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead_form=form.save(commit=False)
            lead_form.report = report
            lead_form.request_type = 'Request Sample'
            lead_form.save()
            emailBody = report.title + '\n' + 'Name:' + lead_form.full_name + '\n' + 'Phone:' + str(lead_form.phone) + 'Country:' + str(lead_form.country) + 'Company:' + lead_form.company + 'Job Title:' + lead_form.job_title + 'Price:' + report.single_user_price +'Comments:' + lead_form.comment
            send_mail(
                'Lead - Sample Request',
                 emailBody,
                'sales@4arcresearch.com',
                ['javedattar99@gmail.com'],
                fail_silently=False,
            )

        else:
            print('Form invalid')
    else:
        form = LeadForm()
    return render(request, 'report/request-sample.html', {'form':form,'report':report})


def checkout(request, id):
    report = get_object_or_404(Report, id=id)
    if request.method == 'POST':
       price = request.POST['price']

    form = CheckoutForm()
    return render(request,'report/checkout.html',{'report':report,'form':form,'price':price})


def categoryPage(request, slug):
    category = get_object_or_404(Category, slug=slug)
    reports = Report.objects.filter(category=category)
    all_categories = Category.objects.all()

    paginator = Paginator(reports, 2)
    page_number = request.GET.get('page')
    try:
        reports = paginator.page(page_number)
    except PageNotAnInteger:
        reports = paginator.page(1)
    except EmptyPage:
        reports = paginator.page(paginator.num_pages)
    return render(request, 'report/category.html', {'category': category, 'reports': reports, 'all_categories': all_categories})


def publisherPage(request, slug):
    publisher = get_object_or_404(Publisher,slug=slug)
    return render(request,'report/publisher.html', {'publisher':publisher})