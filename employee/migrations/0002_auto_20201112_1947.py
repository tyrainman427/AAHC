# Generated by Django 3.1.2 on 2020-11-13 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Application',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='employee_id',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='email_address',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='employee',
            name='anyDayAnyHour',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='been_convicted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='branch',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='college',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='contact_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='dateFrom',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='dateTo',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='date_availabl',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='date_hired',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='disclaimer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='expect_weekly_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='expected_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='explain_conviction',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='friday_from',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='friday_to',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='ged',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='gotTransportation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='gov_id',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='employee',
            name='graduated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='graduatedTrade',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='high_school',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='howDidYouHearAboutPosition',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='jobTitle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='last_collegeYear_completed',
            field=models.CharField(choices=[('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], default='9', max_length=2),
        ),
        migrations.AddField(
            model_name='employee',
            name='last_year_completed',
            field=models.CharField(choices=[('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], default='9', max_length=2),
        ),
        migrations.AddField(
            model_name='employee',
            name='list_skills',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='major',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='military_service',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='monday_from',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='monday_to',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='nameOfEmployer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='ok_to_contact',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='over18',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='pay_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='position_applying',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='reason_for_leaving',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='employee',
            name='saturday_from',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='saturday_to',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='social_security',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='employee',
            name='sunday_from',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='sunday_to',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='thursday_from',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='thursday_to',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='trade_school',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='tuesday_from',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='tuesday_to',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='us_citizen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='veteran',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='wenesday_from',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='wenesday_to',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='willingToTravel',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='workHoliday',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.FloatField(blank=True),
        ),
    ]
