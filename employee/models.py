from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    pass

class Employee(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    birth_date = models.DateTimeField(null=True,blank=True)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    title = models.CharField(max_length=30, blank=True)
    employee_id = models.CharField(max_length=10)
    start_date = models.DateTimeField(null=True,blank=True)
    department = models.CharField(max_length=50)
    work_location = models.CharField(max_length=50)
    supervisor = models.CharField(max_length=50)
    emergency_contact_name = models.CharField(max_length=50)
    emergency_contact_number = models.CharField(max_length=50)
    salary = models.FloatField(default=0.00, blank=True)
    phone_number = models.CharField(max_length=250, blank=True)
    email_address = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('employee:employee_detail', args=[str(self.id)])

YEARS_COMPLETED = (
    ("9","9"),
    ("10","10"),
    ("11","11"),
    ("12","12"),
)

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('employee:announcement-details', args=[str(self.id)])

class Application(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    address= models.CharField(max_length=255)
    email= models.EmailField(max_length=100)
    phone= models.CharField(max_length=10)
    us_citizen= models.BooleanField()
    over18= models.BooleanField()
    dob= models.DateField(null=True)
    # exclude below
    position= models.CharField(max_length=50)
    salary= models.FloatField(blank=True)
    date_hired=models.DateField(null=True)
    pay_rate= models.FloatField(blank=True)
    # exclude above
    been_convicted= models.BooleanField()
    explain_conviction=models.TextField(null=True)
    military_service= models.BooleanField()
    branch= models.CharField(max_length=100)
    veteran= models.BooleanField()
    position_applying= models.CharField(max_length=255)
    howDidYouHearAboutPosition= models.CharField(max_length=255)
    expected_rate= models.FloatField(blank=True)
    expect_weekly_rate= models.FloatField(blank=True)
    date_availabl= models.DateField(null=True)
    resume= models.FileField(upload_to="")
    social_security= models.FileField(upload_to="")
    gov_id= models.FileField(upload_to="")
    # education
    high_school= models.CharField(max_length=255)
    last_year_completed = models.CharField(max_length=2,choices=YEARS_COMPLETED)
    graduated= models.BooleanField()
    college= models.CharField(max_length=255)
    last_collegeYear_completed = models.CharField(max_length=2,choices=YEARS_COMPLETED)
    major= models.CharField(max_length=255)
    trade_school= models.CharField(max_length=255)
    graduatedTrade= models.BooleanField()
    ged= models.BooleanField()
    list_skills=models.TextField(null=True)
    # employment
    nameOfEmployer= models.CharField(max_length=255)
    jobTitle= models.CharField(max_length=255)
    dateFrom=models.DateField(null=True)
    dateTo =models.DateField(null=True)
    ok_to_contact= models.BooleanField()
    contact_number= models.CharField(max_length=10)
    reason_for_leaving= models.CharField(max_length=255)
    # availability
    anyDayAnyHour= models.BooleanField()
    workHoliday= models.BooleanField()
    gotTransportation= models.BooleanField()
    willingToTravel= models.BooleanField()
    # schedule
    monday_from=models.DateField(null=True)
    monday_to=models.DateField(null=True)
    tuesday_from=models.DateField(null=True)
    tuesday_to=models.DateField(null=True)
    wenesday_from=models.DateField(null=True)
    wenesday_to=models.DateField(null=True)
    thursday_from=models.DateField(null=True)
    thursday_to=models.DateField(null=True)
    friday_from=models.DateField(null=True)
    friday_to=models.DateField(null=True)
    saturday_from=models.DateField(null=True)
    saturday_to=models.DateField(null=True)
    sunday_from=models.DateField(null=True)
    sunday_to=models.DateField(null=True)
    disclaimer= models.BooleanField()

    def __str__(self):
        return f"{self.last_name},{self.first_name}"
    # Disclaimer: I certify that the information contained in this application is correct to the best of my knowledge. I understand that to falsify information is grounds for refusing to hire me, or for discharge should I be hired. I authorize any person, organization or company listed on this application to supply you any and all information concerning my previous employment, education and qualifications for employment. I also authorize you to request and receive such information. I understand I will be submitted to a background check by which the company has my permission to submit on my behalf. In consideration for my employment, I agree to abide by the rules and regulations of the company, which rules may be changed, withdrawn, added or interpreted at any time, at the company’s sole option and without prior notice to me. I also acknowledge that my employment may be terminated, or any offer or acceptance of employment withdrawn, at any time, with or without cause, and with or without
    # prior notice at the option of the company or myself.
