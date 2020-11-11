from django.urls import path
from .views import register,EmployeeList, EmployeeDetailView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView,Portal,Announcement,get_form,AnnouncementDetailView

app_name = 'employee'

urlpatterns = [
    path('dashboard/', Portal.as_view(), name='index'),
    path('announcements/', Announcement.as_view(), name='announcements'),
    path('announcements/<int:id>/', AnnouncementDetailView.as_view(), name='announcement-details'),
    path('employee/', EmployeeList.as_view(), name='employee-list'),
    path('<int:id>/', EmployeeDetailView.as_view(), name='employee_detail'),
    path('new/', EmployeeCreateView.as_view(), name='employee-create'),
    path('announcements/add/', get_form, name='announcement-add'),
    path('employee/<pk>/update-employee/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('employee/<pk>/delete-employee/', EmployeeDeleteView.as_view(), name='employee-delete'),
    path('register/', register, name="register"),
]
