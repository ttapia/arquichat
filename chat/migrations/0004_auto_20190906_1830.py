# Generated by Django 2.2.5 on 2019-09-06 18:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20190906_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
