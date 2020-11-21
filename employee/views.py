from .models import *
from django.shortcuts import get_object_or_404,redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import AnnouncementForm,CustomUserCreationForm
from django.http import HttpResponseRedirect
from .models import Announcement as Announce
from django.contrib.auth import login
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

@method_decorator(login_required, name='dispatch')
class Portal(ListView):
    model = Employee
    queryset = Employee.objects.all()
    template_name = 'employee/index.html'

@method_decorator(login_required, name='dispatch')
class Announcement(ListView):
    model = Announcement
    queryset = Announce.objects.all()
    template_name = 'employee/announcements.html'

@method_decorator(login_required, name='dispatch')
class EmployeeList(ListView):
    model = Employee
    queryset = Employee.objects.filter(is_active=True)
    template_name = 'employee/employee-list.html'

    def get_queryset(self):
        result = super(EmployeeList, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(first_name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(email_address__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(city__icontains=q) for q in query_list))
            )

        return result

@method_decorator(login_required, name='dispatch')
class EmployeeDetailView(DetailView):
    template_name = "employee/employee_detail.html"
    member = Employee.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Employee, id=id_)

@method_decorator(login_required, name='dispatch')
class ApplicantDetailView(DetailView):
    template_name = "employee/applicant_detail.html"
    member = Employee.objects.filter(is_active=False)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Employee, id=id_)

# @method_decorator(login_required, name='dispatch')
class EmployeeCreateView(CreateView):
    model = Employee
    fields = ['first_name','last_name','address','email','phone',
    'dob','city','state','zip','us_citizen','over18',
    'been_convicted','explain_conviction','military_service','branch',
    'veteran','position_applying','how_Did_You_Hear_About_Position',
    'expected_rate','expect_weekly_rate','salary','date_available','resume','social_security',
    'gov_id','high_school','last_year_completed','graduated','college',
    'last_college_Year_completed','major','trade_school','graduated_Trade',
    'ged','list_skills','name_Of_Employer','job_Title','date_From',
    'date_To','ok_to_contact','contact_number','reason_for_leaving',
    'work_any_Day_Any_Hour','work_holidays','got_transportation',
    'willing_to_travel','monday_from','monday_to','tuesday_from',
    'tuesday_to','wenesday_from','wenesday_to','thursday_from',
    'thursday_to','friday_from','friday_to','saturday_from',
    'saturday_to','sunday_from','sunday_to','emergency_contact_name',
    'emergency_contact_number','disclaimer'
    ]


@login_required(login_url='/accounts/login/')
def application(request):
    employee = Employee.objects.filter(is_active=False)
    context = {'employee':employee}
    return render(request,'employee/applicants.html',context)

@login_required(login_url='/accounts/login/')
def get_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AnnouncementForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            title = form.cleaned_data['title']
            message = form.cleaned_data['message']
            ann = Announcement(title=title,message=message,)
            form.save()
            return HttpResponseRedirect('/portal/announcements/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AnnouncementForm()

    return render(request, 'employee/announcement_form.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class AnnouncementDetailView(DetailView):
    template_name = "employee/announcement-details.html"
    model = Announce

    def get_absolute_url(self):
        return reverse('employee:announcement-details', args=[str(self.id)])

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Announce, id=id_)

@method_decorator(login_required, name='dispatch')
class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = '__all__'

    def get_absolute_url(self):
        return reverse('employee:Employee_detail', args=[str(self.id)])

@method_decorator(login_required, name='dispatch')
class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = '/portal/'

def register(request):
    if request.method == "GET":
        return render(
            request, "employee/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("employee:index"))
