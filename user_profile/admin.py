from django.contrib import admin
from .models import *

admin.site.register([
    UserProfile, UserSocialLink, JobExperience, AcademicExperience, UserSkill, Certificate, PortfolioEntry
])