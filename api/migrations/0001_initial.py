# Generated by Django 4.1.4 on 2023-01-24 13:23

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email_is_verified', models.BooleanField(blank=True, default=False, null=True)),
                ('otp', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Contests',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('Name_Of_Contest', models.CharField(blank=True, default='-', max_length=225, null=True)),
                ('Place', models.CharField(blank=True, default='Online', max_length=225, null=True)),
                ('Start_Time', models.CharField(blank=True, default='-', max_length=225, null=True)),
                ('Name_Of_Website', models.CharField(blank=True, default='-', max_length=225, null=True)),
                ('OnGoing', models.BooleanField(blank=True, default='-', null=True)),
                ('Start_Date', models.CharField(blank=True, default='-', max_length=225, null=True)),
                ('Contest_Type', models.CharField(blank=True, default=None, max_length=225, null=True)),
                ('Contest_Mode', models.CharField(blank=True, default=None, max_length=225, null=True)),
                ('Contest_Duration', models.CharField(blank=True, default='-', max_length=225, null=True)),
                ('Remaining_Time', models.CharField(blank=True, default='-', max_length=225, null=True)),
                ('Days_Remaining_For_The_Contest_To_Start', models.CharField(blank=True, default='-', max_length=225, null=True)),
                ('Days_Remaining_To_Register', models.CharField(blank=True, default='-', max_length=225, null=True)),
                ('Entry_Price', models.IntegerField(blank=True, default=0, null=True)),
                ('Price_Pool', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_id', models.IntegerField(blank=True, default=None, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
        migrations.CreateModel(
            name='Calender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Added_To_Calender', models.BooleanField(blank=True, default=False, null=True)),
                ('contest_name', models.CharField(blank=True, default=None, max_length=225, null=True)),
                ('contest_link', models.URLField(blank=True, default=None, null=True)),
                ('contest_start_time', models.CharField(blank=True, default=None, max_length=225, null=True)),
                ('contest', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.contests')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]
