# Generated by Django 3.2.5 on 2021-08-21 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=100, verbose_name='Name')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Title')),
                ('title_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('title_pt_br', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('contact_email', models.EmailField(blank=True, max_length=254, verbose_name='Contact email')),
                ('contact_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('location', models.CharField(blank=True, max_length=50, verbose_name='Location')),
                ('website', models.URLField(blank=True, max_length=256, verbose_name='Website')),
                ('birthday', models.DateField(blank=True, verbose_name='Birthday')),
                ('picture', models.ImageField(blank=True, upload_to='profile_pictures/', verbose_name='Profile picture')),
                ('summary', models.TextField(blank=True, verbose_name='Summary')),
                ('summary_en', models.TextField(blank=True, null=True, verbose_name='Summary')),
                ('summary_pt_br', models.TextField(blank=True, null=True, verbose_name='Summary')),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(blank=True, choices=[(0, 'Software'), (1, 'Programing language'), (2, 'Programing tool'), (3, 'Software framework'), (4, 'Architecture / Paradigm'), (5, 'Language'), (6, 'Soft skill')], null=True, verbose_name='Skill type')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('name_en', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('name_pt_br', models.CharField(max_length=50, null=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
                'ordering': ['type', 'name'],
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('base_url', models.URLField(verbose_name='Base URL')),
                ('icon_color', models.CharField(max_length=6, verbose_name='Color')),
                ('bi_icon', models.CharField(max_length=50, verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'Social media',
                'verbose_name_plural': 'Social medias',
            },
        ),
        migrations.CreateModel(
            name='UserSocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='Username or link')),
                ('link', models.URLField(blank=True, verbose_name='Link')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.profile', verbose_name='User profile')),
                ('socialmedia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.socialmedia', verbose_name='Social media')),
            ],
            options={
                'verbose_name': "User's social media link",
                'verbose_name_plural': "User's social media links",
            },
        ),
        migrations.CreateModel(
            name='UserSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(choices=[(0, 'Novice'), (1, 'Beginner'), (2, 'Competent'), (3, 'Proficient'), (4, 'Expert')], default=2, verbose_name='Proficiency level')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.profile', verbose_name='User profile')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.skill', verbose_name='Skill')),
            ],
            options={
                'verbose_name': "users' skill",
                'verbose_name_plural': "users' skills",
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='skill_set',
            field=models.ManyToManyField(blank=True, through='resume.UserSkill', to='resume.Skill', verbose_name='skills'),
        ),
        migrations.AddField(
            model_name='profile',
            name='socialmedia_set',
            field=models.ManyToManyField(blank=True, through='resume.UserSocialLink', to='resume.SocialMedia', verbose_name='Social media link'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.CreateModel(
            name='PortfolioEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('title_en', models.CharField(max_length=50, null=True, verbose_name='Title')),
                ('title_pt_br', models.CharField(max_length=50, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('description_pt_br', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('cover', models.ImageField(blank=True, upload_to='images/portfolio', verbose_name='Cover image')),
                ('link', models.URLField(blank=True, verbose_name='Link')),
                ('date', models.DateField(blank=True, verbose_name='Date')),
                ('type', models.IntegerField(blank=True, choices=[(0, 'Side project'), (1, 'Client project'), (2, 'Product'), (3, 'Publication')], null=True, verbose_name='Entry type')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.profile', verbose_name='User profile')),
            ],
            options={
                'verbose_name': 'portfolio entry',
                'verbose_name_plural': 'portfolio entries',
            },
        ),
        migrations.CreateModel(
            name='JobExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('description_pt_br', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('location', models.CharField(blank=True, max_length=50, verbose_name='Location')),
                ('start_date', models.DateField(verbose_name='Start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End date')),
                ('company', models.CharField(max_length=50, verbose_name='Company')),
                ('role', models.CharField(max_length=50, verbose_name='Role')),
                ('role_en', models.CharField(max_length=50, null=True, verbose_name='Role')),
                ('role_pt_br', models.CharField(max_length=50, null=True, verbose_name='Role')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.profile', verbose_name='User profile')),
                ('skills_applied', models.ManyToManyField(blank=True, to='resume.Skill', verbose_name='Skills applied')),
            ],
            options={
                'verbose_name': 'Job experience',
                'verbose_name_plural': 'Job experiences',
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('name_en', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('name_pt_br', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('link', models.URLField(blank=True, verbose_name='Certificate link')),
                ('file', models.FileField(blank=True, upload_to='storage/portfolio', verbose_name='Certificate file')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.profile', verbose_name='User profile')),
                ('skill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='resume.skill', verbose_name='Skill')),
            ],
            options={
                'verbose_name': 'certificate',
                'verbose_name_plural': 'certificates',
            },
        ),
        migrations.CreateModel(
            name='AcademicExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('description_pt_br', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('location', models.CharField(blank=True, max_length=50, verbose_name='Location')),
                ('start_date', models.DateField(verbose_name='Start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End date')),
                ('school', models.CharField(max_length=50, verbose_name='School')),
                ('course', models.CharField(max_length=50, verbose_name='Course')),
                ('course_en', models.CharField(max_length=50, null=True, verbose_name='Course')),
                ('course_pt_br', models.CharField(max_length=50, null=True, verbose_name='Course')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.profile', verbose_name='User profile')),
            ],
            options={
                'verbose_name': 'Academic experience',
                'verbose_name_plural': 'Academic experiences',
            },
        ),
    ]
