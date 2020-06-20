from django.db import models

# Create your models here.






from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField


class Report(models.Model):
    # report_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    meta_title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True,null=True,max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    # image_icon = models.ForeignKey('Image', on_delete=models.CASCADE)
    publisher = models.ForeignKey('Publisher', models.CASCADE)
    summary = RichTextField()
    tabel_of_content = RichTextField()
    published_date = models.DateField(auto_now_add=True)
    no_of_pages = models.IntegerField(default=100)
    single_user_price = models.IntegerField(default=2000)
    multi_user_price = models.IntegerField(default=4000)
    corporate_user_price = models.IntegerField(default=7000)


    def __str__(self):
        return self.title

    # def save(self,*args,**kwargs):
    #     if  not self.slug and self.meta_title:
    #         url = self.meta_title + str('-1234')
    #         self.slug = slugify(url)
    #         print(self.slug)
    #     super(Report,self).save(*args,**kwargs)


def post_save_slug_generator(sender,instance, created, *args, **kwargs):
    if created:
        if not instance.slug and instance.meta_title:
            url = instance.meta_title + '-' + str(instance.id)
            instance.slug = slugify(url)
            instance.save()

post_save.connect(post_save_slug_generator,sender=Report)


class Image(models.Model):
    image = models.ImageField(upload_to='reportimage/', blank=True, null=True)

    def __str__(self):
        return str(self.image.name)


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    slug = models.SlugField(blank=True,unique=True)
    image = models.ImageField(upload_to='category/', blank=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Category,self).save(*args,**kwargs)


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    slug = models.SlugField(blank=True,unique=True)
    image = models.ImageField(upload_to='publishers/', blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        if  not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Publisher,self).save(*args,**kwargs)


from django_countries.fields import CountryField
# Create your models here.


class Lead(models.Model):
    LEAD_TYPE =(
        ('Request Sample','Request Sample'),
        ('Request Discount', 'Request Discount'),
        ('Request Inquiry', 'Request Inquiry'),

    )
    report = models.ForeignKey(Report,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    corporate_email = models.EmailField()
    country = CountryField(blank_label='Select Country')
    phone = models.IntegerField()
    job_title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    comment = models.CharField(max_length=1000,null=True,blank=True)
    request_type = models.CharField(max_length=30,choices=LEAD_TYPE,blank=True,null=True)
    lead_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Billing_Details(models.Model):

    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    corporate_email = models.EmailField()
    phone = models.CharField(max_length=14)
    company = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = CountryField(blank_label='Country')
    zipcode = models.CharField(max_length=20)
    invoice_date = models.DateField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'BillingDetails'

    def __str__(self):
        return self.first_name + self.last_name

class Contact_Us(models.Model):
    full_name = models.CharField(max_length=50)
    corporate_email = models.EmailField()
    phone = models.CharField(max_length=14)
    subject =models.CharField(max_length=500)
    message = models.TextField()
    contact_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'ContactUs'

    def __str__(self):
        return self.full_name





