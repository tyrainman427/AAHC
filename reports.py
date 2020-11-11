import reporting
from django.db.models import Sum, Avg, Count
from models import Client

class ClientReport(reporting.Report):
    model = Client
    verbose_name = 'Client Report'
    annotate = (                    # Annotation fields (tupples of field, func, title)
        ('id', Count, 'Total'),     # example of custom title for column
        ('salary', Sum),            # no title - column will be "Salary Sum"
        ('expenses', Sum),
    )
    aggregate = (                   # columns that will be aggregated (syntax the same as for annotate)
        ('id', Count, 'Total'),
        ('salary', Sum, 'Salary'),
        ('expenses', Sum, 'Expenses'),
    )
    group_by = [                   # list of fields and lookups for group-by options
        'client',
        ('employee','client'), # If a tupple is defined would group by all fields in the tupple
        'department__leader',
        'occupation',
    ]
    list_filter = [                # This are report filter options (similar to django-admin)
       'address',
       'first_name',
    ]

    # if detail_list_display is defined user will be able to see how rows was grouped
    detail_list_display = [
        'first_name',
        'last_name',

    ]

    date_hierarchy = 'first_name' # the same as django-admin


reporting.register('client', ClientReport) # Do not forget to 'register' your class in reports
