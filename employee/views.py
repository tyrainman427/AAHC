from .models import Employee, Announcement, Application
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
    queryset = Employee.objects.all()
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
class EmployeeCreateView(CreateView):
    model = Application
    fields = '__all__'

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
            return HttpResponseRedirect('/announcements/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AnnouncementForm()

    return render(request, 'employee/announcement_form.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class AnnouncementDetailView(DetailView):
    template_name = "employee/announcement-details.html"
    announcements = Announce.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Announce, id=id_)

@method_decorator(login_required, name='dispatch')
class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ['first_name', 'last_name','address','city',
    'state','zip','phone_number','email_address','title',
    'department','work_location','supervisor','emergency_contact_name','emergency_contact_number',
    ]

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
