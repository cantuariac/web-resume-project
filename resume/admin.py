from django.contrib import admin
from .models import *

admin.site.register([Profile, SocialMedia, UserSocialLink, JobExperience,
                    AcademicExperience, Skill, UserSkill, Certificate, PortfolioEntry])
