# Generated by Django 4.1 on 2022-08-31 18:02

import app.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_job_closing_date_job_created_date_job_posting_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="posting_date",
            field=models.DateField(
                blank=True,
                default=datetime.date,
                help_text="Enter posting date",
                null=True,
                validators=[app.models.no_pass],
            ),
        ),
    ]