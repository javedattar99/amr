




from django.shortcuts import render,get_object_or_404,redirect
from .forms import LeadForm,CheckoutForm
from .models import Category,Report,Publisher
from django_countries import countries
from django.core.mail import send_mail
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage



def indexView(request):
    reports = Report.objects.all()[:3]
    categories = Category.objects.all()
    return render(request,'base/index.html',{'reports': reports,'categories':categories})


def aboutus(request):
    return render(request,'base/about-us.html')


def contactus(request):
    return render(request,'base/contact-us.html')


def reportPage(request,slug):
    report = get_object_or_404(Report, slug=slug)
    category = report.category
    return render(request,'report/reportpage.html',{'report':report,'category':category})

def thankyouPage(request):
    return render(request,'base/thank-you.html')


def requestSample(request,id):
    report = get_object_or_404(Report, id=id)
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead_form=form.save(commit=False)
            lead_form.report = report
            lead_form.request_type = 'Request Sample'
            lead_form.save()
            emailBody = 'Report Name:'+ report.title + '\n\n' + 'Client Name:' + lead_form.full_name + '\n\n' 'Client Email:'+ lead_form.corporate_email + '\n\n' + 'Phone:' + str(lead_form.phone) + '\n\n' + 'Country:' + str(lead_form.country) +'\n\n' + 'Category:'+ report.category.name +'\n\n'+'Publisher :'+report.publisher.name+ '\n\n' +'Company:' + lead_form.company + '\n\n' + 'Job Title:' + lead_form.job_title +'\n\n' +'Price:' + str(report.single_user_price) +'\n\n' +'Comments:' + lead_form.comment
            send_mail(
                'Lead - Sample Request',
                 emailBody,
                'sales@affluencemarketreports.com',
                ['sales@affluencemarketreports.com'],
                fail_silently=False,
            )
            return redirect('thankyou')
        else:
            print('Form invalid')
    else:
        form = LeadForm()
    return render(request, 'report/request-sample.html', {'form':form,'report':report})

def requestDiscount(request,id):
    report = get_object_or_404(Report, id=id)
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead_form=form.save(commit=False)
            lead_form.report = report
            lead_form.request_type = 'Request Discount'
            lead_form.save()
            emailBody = 'Report Name:'+ report.title + '\n\n' + 'Client Name:' + lead_form.full_name + '\n\n' 'Client Email:'+ lead_form.corporate_email + '\n\n' + 'Phone:' + str(lead_form.phone) + '\n\n' + 'Country:' + str(lead_form.country) +'\n\n' + 'Category:'+ report.category.name +'\n\n'+'Publisher :'+report.publisher.name+ '\n\n' +'Company:' + lead_form.company + '\n\n' + 'Job Title:' + lead_form.job_title +'\n\n' +'Price:' + str(report.single_user_price) +'\n\n' +'Comments:' + lead_form.comment
            send_mail(
                'Lead - Discount Request',
                 emailBody,
                'sales@affluencemarketreports.com',
                ['sales@affluencemarketreports.com'],
                fail_silently=False,
            )
            return redirect('thankyou')
        else:
            print('Form invalid')
    else:
        form = LeadForm()
    return render(request, 'report/request-discount.html', {'form':form,'report':report})

def requestInquiry(request,id):
    report = get_object_or_404(Report, id=id)
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead_form=form.save(commit=False)
            lead_form.report = report
            lead_form.request_type = 'Request Inquiry'
            lead_form.save()
            emailBody = 'Report Name:'+ report.title + '\n\n' + 'Client Name:' + lead_form.full_name + '\n\n' 'Client Email:'+ lead_form.corporate_email + '\n\n' + 'Phone:' + str(lead_form.phone) + '\n\n' + 'Country:' + str(lead_form.country) +'\n\n' + 'Category:'+ report.category.name +'\n\n'+'Publisher :'+report.publisher.name+ '\n\n' +'Company:' + lead_form.company + '\n\n' + 'Job Title:' + lead_form.job_title +'\n\n' +'Price:' + str(report.single_user_price) +'\n\n' +'Comments:' + lead_form.comment
            send_mail(
                'Lead - Inquiry Before Buying Request',
                 emailBody,
                'sales@affluencemarketreports.com',
                ['sales@affluencemarketreports.com'],
                fail_silently=False,
            )
            return redirect('thankyou')
        else:
            print('Form invalid')
    else:
        form = LeadForm()
    return render(request, 'report/request-inquiry.html', {'form':form,'report':report})





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
    reports = Report.objects.filter(publisher=publisher)
    all_publishers = Publisher.objects.all()
    paginator = Paginator(reports, 2)
    page_number = request.GET.get('page')
    try:
        reports = paginator.page(page_number)
    except PageNotAnInteger:
        reports = paginator.page(1)
    except EmptyPage:
        reports = paginator.page(paginator.num_pages)
    return render(request,'report/publisher.html', {'publisher':publisher,'reports': reports, 'all_publishers': all_publishers})

def latestReports(request):
    reports = Report.objects.all().order_by('-published_date')
    all_categories = Category.objects.all()
    paginator = Paginator(reports, 5)
    page_number = request.GET.get('page')
    try:
        reports = paginator.page(page_number)
    except PageNotAnInteger:
        reports = paginator.page(1)
    except EmptyPage:
        reports = paginator.page(paginator.num_pages)
    return render(request,'report/latest-report.html',{'reports':reports,'all_categories':all_categories})