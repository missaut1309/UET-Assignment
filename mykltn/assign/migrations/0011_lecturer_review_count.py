# Generated by Django 4.0.6 on 2022-07-22 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assign', '0010_lecturer_committee_status_topic_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer',
            name='review_count',
            field=models.IntegerField(default=0),
        ),
    ]
