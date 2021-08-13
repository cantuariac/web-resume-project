from django.contrib import admin
from .models import *

admin.site.register([
    Profile, SocialMedia, UserSocialLink, JobExperience, AcademicExperience, UserSkill, Certificate, PortfolioEntry
])


@admin.register(Skill)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "type")
