# Generated by Django 4.1.4 on 2023-01-20 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_contests_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contests',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
