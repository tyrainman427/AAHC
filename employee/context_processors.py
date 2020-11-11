def announcements(request):
    from employee.models import Announcement
    return {'announcements': Announcement.objects.all()}
