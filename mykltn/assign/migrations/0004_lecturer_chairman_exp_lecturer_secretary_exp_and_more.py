# Generated by Django 4.0.4 on 2022-06-13 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assign', '0003_alter_topictokeyword_keyword_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer',
            name='chairman_exp',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lecturer',
            name='secretary_exp',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lecturer',
            name='vice_chairman_exp',
            field=models.BooleanField(default=False),
        ),
    ]
