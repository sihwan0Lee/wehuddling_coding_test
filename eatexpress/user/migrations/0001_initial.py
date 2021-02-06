# Generated by Django 3.1.6 on 2021-02-06 19:18

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nickname', models.CharField(max_length=45, unique=True, verbose_name='회원이름')),
                ('email', models.EmailField(max_length=200, null=True, unique=True, verbose_name='이메일')),
                ('password', models.CharField(max_length=100, verbose_name='비밀번호')),
                ('phone_number', models.CharField(max_length=50, null=True, unique=True, verbose_name='전화번호')),
                ('address', models.CharField(blank=True, max_length=200, verbose_name='주소')),
                ('gender', models.CharField(blank=True, choices=[('M', '남성(Male)'), ('F', '여성(Female)')], max_length=45, verbose_name='성별')),
                ('register_date', models.DateField(auto_now_add=True, verbose_name='등록일')),
                ('level', models.CharField(choices=[('admin', 'admin'), ('user', 'user')], default='user', max_length=8, verbose_name='등급')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '회원',
                'verbose_name_plural': '회원',
                'db_table': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
