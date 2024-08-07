# Generated by Django 5.0.7 on 2024-08-07 08:26

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('species', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='')),
                ('is_liked', models.BooleanField(default=False)),
                ('can_adopt', models.BooleanField(default=True)),
                ('can_volunteer', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='pets/')),
            ],
        ),
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('address', models.TextField(default='')),
                ('needs', models.TextField(default='')),
                ('website_link', models.URLField(blank=True, default='')),
                ('news_link', models.URLField(blank=True, default='')),
                ('x_coordinate', models.FloatField(default=0.0)),
                ('y_coordinate', models.FloatField(default=0.0)),
                ('image', models.ImageField(upload_to='shelter/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('groups', models.ManyToManyField(blank=True, related_name='shelters_api_users', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='shelters_api_users', to='auth.permission')),
                ('liked_pets', models.ManyToManyField(blank=True, related_name='liked_by', to='shelters_api.pet')),
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
        migrations.AddField(
            model_name='pet',
            name='shelter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='shelters_api.shelter'),
        ),
    ]
