# Generated by Django 3.1.2 on 2021-03-09 06:50

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('mobile', models.CharField(blank=True, max_length=16, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
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
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('image', models.ImageField(upload_to='')),
                ('date', models.DateField()),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=16)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Contact Us',
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=512)),
                ('answer', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'FAQs',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.CharField(max_length=8)),
                ('message', models.TextField()),
                ('is_bug', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Feedbacks',
            },
        ),
        migrations.CreateModel(
            name='GeneralNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('link', models.URLField(blank=True, default='')),
                ('rollOut', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'General Notification',
            },
        ),
        migrations.CreateModel(
            name='MCQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('file', models.FileField(upload_to='')),
                ('image', models.ImageField(upload_to='')),
                ('preview_file', models.FileField(upload_to='')),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'MCQs',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('image', models.ImageField(upload_to='')),
                ('date', models.DateField()),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'NEWS',
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Newsletters',
            },
        ),
        migrations.CreateModel(
            name='PDF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('file', models.FileField(upload_to='')),
                ('price', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'PDFs',
            },
        ),
        migrations.CreateModel(
            name='PersonalNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Personal Notification',
            },
        ),
        migrations.CreateModel(
            name='PromoCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6)),
                ('percent', models.PositiveSmallIntegerField()),
                ('description', models.TextField(blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Promo Codes',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=128)),
                ('date', models.DateField()),
                ('demo', models.FileField(blank=True, null=True, upload_to='')),
                ('video', models.FileField(blank=True, null=True, upload_to='')),
                ('youtube_link', models.CharField(blank=True, max_length=512, null=True)),
                ('price', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Sessions',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name_plural': 'Sub-Categories',
            },
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('file', models.FileField(upload_to='')),
                ('image', models.ImageField(upload_to='')),
                ('preview_file', models.FileField(upload_to='')),
                ('price', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Summaries',
            },
        ),
        migrations.CreateModel(
            name='TeamForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=16)),
                ('cv', models.FileField(upload_to='')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('other_document', models.FileField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Team Form',
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=256)),
                ('designation', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='UserCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Promocodes Used (User)',
            },
        ),
        migrations.CreateModel(
            name='UserSubscriptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mcqs', models.ManyToManyField(blank=True, to='core.MCQ')),
                ('pdfs', models.ManyToManyField(blank=True, to='core.PDF')),
                ('sessions', models.ManyToManyField(blank=True, to='core.Session')),
                ('summaries', models.ManyToManyField(blank=True, to='core.Summary')),
            ],
            options={
                'verbose_name_plural': 'User Subscriptions',
            },
        ),
    ]
