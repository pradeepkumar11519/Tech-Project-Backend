# Generated by Django 4.1.4 on 2023-01-23 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_alter_calender_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calender',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
